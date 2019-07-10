# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServiceTypeHealthPolicyMapItem(Model):
    """Defines an item in ServiceTypeHealthPolicyMap.

    All required parameters must be populated in order to send to Azure.

    :param key: Required. The key of the service type health policy map item.
     This is the name of the service type.
    :type key: str
    :param value: Required. The value of the service type health policy map
     item. This is the ServiceTypeHealthPolicy for this service type.
    :type value: ~azure.servicefabric.models.ServiceTypeHealthPolicy
    """

    _validation = {
        'key': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'key': {'key': 'Key', 'type': 'str'},
        'value': {'key': 'Value', 'type': 'ServiceTypeHealthPolicy'},
    }

    def __init__(self, **kwargs):
        super(ServiceTypeHealthPolicyMapItem, self).__init__(**kwargs)
        self.key = kwargs.get('key', None)
        self.value = kwargs.get('value', None)