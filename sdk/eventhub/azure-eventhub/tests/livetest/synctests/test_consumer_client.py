import time
import pytest
import threading
import sys
from azure.eventhub import EventData
from azure.eventhub import EventHubConsumerClient
from azure.eventhub._eventprocessor.local_checkpoint_store import InMemoryCheckpointStore
from azure.eventhub._constants import ALL_PARTITIONS


@pytest.mark.liveTest
def test_receive_no_partition(connstr_senders):
    connection_str, senders = connstr_senders
    senders[0].send(EventData("Test EventData"))
    senders[1].send(EventData("Test EventData"))
    client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group='$default', receive_timeout=1)

    def on_event(partition_context, event):
        on_event.received += 1

    on_event.received = 0
    with client:
        worker = threading.Thread(target=client.receive,
                                  args=(on_event,),
                                  kwargs={"starting_position": "-1"})
        worker.start()
        time.sleep(10)
        assert on_event.received == 2


@pytest.mark.liveTest
def test_receive_partition(connstr_senders):
    connection_str, senders = connstr_senders
    senders[0].send(EventData("Test EventData"))
    client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group='$default')

    def on_event(partition_context, event):
        on_event.received += 1
        on_event.partition_id = partition_context.partition_id
        on_event.consumer_group = partition_context.consumer_group
        on_event.fully_qualified_namespace = partition_context.fully_qualified_namespace
        on_event.eventhub_name = partition_context.eventhub_name

    on_event.received = 0
    with client:
        worker = threading.Thread(target=client.receive,
                                  args=(on_event,),
                                  kwargs={"starting_position": "-1",
                                          "partition_id": "0"})
        worker.start()
        time.sleep(10)
        assert on_event.received == 1
        assert on_event.partition_id == "0"
        assert on_event.consumer_group == "$default"
        assert on_event.fully_qualified_namespace in connection_str
        assert on_event.eventhub_name == senders[0]._client.eventhub_name


@pytest.mark.liveTest
def test_receive_load_balancing(connstr_senders):
    if sys.platform.startswith('darwin'):
        pytest.skip("Skipping on OSX - test code using multiple threads. Sometimes OSX aborts python process")

    connection_str, senders = connstr_senders
    cs = InMemoryCheckpointStore()
    client1 = EventHubConsumerClient.from_connection_string(
        connection_str, consumer_group='$default', checkpoint_store=cs, load_balancing_interval=1)
    client2 = EventHubConsumerClient.from_connection_string(
        connection_str, consumer_group='$default', checkpoint_store=cs, load_balancing_interval=1)

    def on_event(partition_context, event):
        pass

    with client1, client2:
        worker1 = threading.Thread(target=client1.receive,
                                   args=(on_event,),
                                   kwargs={"starting_position": "-1"})

        worker2 = threading.Thread(target=client2.receive,
                                   args=(on_event,),
                                   kwargs={"starting_position": "-1"})

        worker1.start()
        time.sleep(3.3)
        worker2.start()
        time.sleep(10)
        assert len(client1._event_processors[("$default", ALL_PARTITIONS)]._consumers) == 1
        assert len(client2._event_processors[("$default", ALL_PARTITIONS)]._consumers) == 1
