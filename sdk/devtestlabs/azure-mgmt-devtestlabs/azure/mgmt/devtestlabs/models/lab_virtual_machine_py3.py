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

from .resource_py3 import Resource


class LabVirtualMachine(Resource):
    """A virtual machine.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param notes: The notes of the virtual machine.
    :type notes: str
    :param owner_object_id: The object identifier of the owner of the virtual
     machine.
    :type owner_object_id: str
    :param owner_user_principal_name: The user principal name of the virtual
     machine owner.
    :type owner_user_principal_name: str
    :param created_by_user_id: The object identifier of the creator of the
     virtual machine.
    :type created_by_user_id: str
    :param created_by_user: The email address of creator of the virtual
     machine.
    :type created_by_user: str
    :param created_date: The creation date of the virtual machine.
    :type created_date: datetime
    :param compute_id: The resource identifier (Microsoft.Compute) of the
     virtual machine.
    :type compute_id: str
    :param custom_image_id: The custom image identifier of the virtual
     machine.
    :type custom_image_id: str
    :param os_type: The OS type of the virtual machine.
    :type os_type: str
    :param size: The size of the virtual machine.
    :type size: str
    :param user_name: The user name of the virtual machine.
    :type user_name: str
    :param password: The password of the virtual machine administrator.
    :type password: str
    :param ssh_key: The SSH key of the virtual machine administrator.
    :type ssh_key: str
    :param is_authentication_with_ssh_key: Indicates whether this virtual
     machine uses an SSH key for authentication.
    :type is_authentication_with_ssh_key: bool
    :param fqdn: The fully-qualified domain name of the virtual machine.
    :type fqdn: str
    :param lab_subnet_name: The lab subnet name of the virtual machine.
    :type lab_subnet_name: str
    :param lab_virtual_network_id: The lab virtual network identifier of the
     virtual machine.
    :type lab_virtual_network_id: str
    :param disallow_public_ip_address: Indicates whether the virtual machine
     is to be created without a public IP address.
    :type disallow_public_ip_address: bool
    :param artifacts: The artifacts to be installed on the virtual machine.
    :type artifacts:
     list[~azure.mgmt.devtestlabs.models.ArtifactInstallProperties]
    :param artifact_deployment_status: The artifact deployment status for the
     virtual machine.
    :type artifact_deployment_status:
     ~azure.mgmt.devtestlabs.models.ArtifactDeploymentStatusProperties
    :param gallery_image_reference: The Microsoft Azure Marketplace image
     reference of the virtual machine.
    :type gallery_image_reference:
     ~azure.mgmt.devtestlabs.models.GalleryImageReference
    :param plan_id: The id of the plan associated with the virtual machine
     image
    :type plan_id: str
    :ivar compute_vm: The compute virtual machine properties.
    :vartype compute_vm: ~azure.mgmt.devtestlabs.models.ComputeVmProperties
    :param network_interface: The network interface properties.
    :type network_interface:
     ~azure.mgmt.devtestlabs.models.NetworkInterfaceProperties
    :ivar applicable_schedule: The applicable schedule for the virtual
     machine.
    :vartype applicable_schedule:
     ~azure.mgmt.devtestlabs.models.ApplicableSchedule
    :param expiration_date: The expiration date for VM.
    :type expiration_date: datetime
    :param allow_claim: Indicates whether another user can take ownership of
     the virtual machine
    :type allow_claim: bool
    :param storage_type: Storage type to use for virtual machine (i.e.
     Standard, Premium).
    :type storage_type: str
    :param virtual_machine_creation_source: Tells source of creation of lab
     virtual machine. Output property only. Possible values include:
     'FromCustomImage', 'FromGalleryImage'
    :type virtual_machine_creation_source: str or
     ~azure.mgmt.devtestlabs.models.VirtualMachineCreationSource
    :param environment_id: The resource ID of the environment that contains
     this virtual machine, if any.
    :type environment_id: str
    :param data_disk_parameters: New or existing data disks to attach to the
     virtual machine after creation
    :type data_disk_parameters:
     list[~azure.mgmt.devtestlabs.models.DataDiskProperties]
    :param schedule_parameters: Virtual Machine schedules to be created
    :type schedule_parameters:
     list[~azure.mgmt.devtestlabs.models.ScheduleCreationParameter]
    :param last_known_power_state: Last known compute power state captured in
     DTL
    :type last_known_power_state: str
    :ivar provisioning_state: The provisioning status of the resource.
    :vartype provisioning_state: str
    :ivar unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :vartype unique_identifier: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'compute_vm': {'readonly': True},
        'applicable_schedule': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'unique_identifier': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'notes': {'key': 'properties.notes', 'type': 'str'},
        'owner_object_id': {'key': 'properties.ownerObjectId', 'type': 'str'},
        'owner_user_principal_name': {'key': 'properties.ownerUserPrincipalName', 'type': 'str'},
        'created_by_user_id': {'key': 'properties.createdByUserId', 'type': 'str'},
        'created_by_user': {'key': 'properties.createdByUser', 'type': 'str'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'compute_id': {'key': 'properties.computeId', 'type': 'str'},
        'custom_image_id': {'key': 'properties.customImageId', 'type': 'str'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'size': {'key': 'properties.size', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'ssh_key': {'key': 'properties.sshKey', 'type': 'str'},
        'is_authentication_with_ssh_key': {'key': 'properties.isAuthenticationWithSshKey', 'type': 'bool'},
        'fqdn': {'key': 'properties.fqdn', 'type': 'str'},
        'lab_subnet_name': {'key': 'properties.labSubnetName', 'type': 'str'},
        'lab_virtual_network_id': {'key': 'properties.labVirtualNetworkId', 'type': 'str'},
        'disallow_public_ip_address': {'key': 'properties.disallowPublicIpAddress', 'type': 'bool'},
        'artifacts': {'key': 'properties.artifacts', 'type': '[ArtifactInstallProperties]'},
        'artifact_deployment_status': {'key': 'properties.artifactDeploymentStatus', 'type': 'ArtifactDeploymentStatusProperties'},
        'gallery_image_reference': {'key': 'properties.galleryImageReference', 'type': 'GalleryImageReference'},
        'plan_id': {'key': 'properties.planId', 'type': 'str'},
        'compute_vm': {'key': 'properties.computeVm', 'type': 'ComputeVmProperties'},
        'network_interface': {'key': 'properties.networkInterface', 'type': 'NetworkInterfaceProperties'},
        'applicable_schedule': {'key': 'properties.applicableSchedule', 'type': 'ApplicableSchedule'},
        'expiration_date': {'key': 'properties.expirationDate', 'type': 'iso-8601'},
        'allow_claim': {'key': 'properties.allowClaim', 'type': 'bool'},
        'storage_type': {'key': 'properties.storageType', 'type': 'str'},
        'virtual_machine_creation_source': {'key': 'properties.virtualMachineCreationSource', 'type': 'str'},
        'environment_id': {'key': 'properties.environmentId', 'type': 'str'},
        'data_disk_parameters': {'key': 'properties.dataDiskParameters', 'type': '[DataDiskProperties]'},
        'schedule_parameters': {'key': 'properties.scheduleParameters', 'type': '[ScheduleCreationParameter]'},
        'last_known_power_state': {'key': 'properties.lastKnownPowerState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, notes: str=None, owner_object_id: str=None, owner_user_principal_name: str=None, created_by_user_id: str=None, created_by_user: str=None, created_date=None, compute_id: str=None, custom_image_id: str=None, os_type: str=None, size: str=None, user_name: str=None, password: str=None, ssh_key: str=None, is_authentication_with_ssh_key: bool=None, fqdn: str=None, lab_subnet_name: str=None, lab_virtual_network_id: str=None, disallow_public_ip_address: bool=None, artifacts=None, artifact_deployment_status=None, gallery_image_reference=None, plan_id: str=None, network_interface=None, expiration_date=None, allow_claim: bool=None, storage_type: str=None, virtual_machine_creation_source=None, environment_id: str=None, data_disk_parameters=None, schedule_parameters=None, last_known_power_state: str=None, **kwargs) -> None:
        super(LabVirtualMachine, self).__init__(location=location, tags=tags, **kwargs)
        self.notes = notes
        self.owner_object_id = owner_object_id
        self.owner_user_principal_name = owner_user_principal_name
        self.created_by_user_id = created_by_user_id
        self.created_by_user = created_by_user
        self.created_date = created_date
        self.compute_id = compute_id
        self.custom_image_id = custom_image_id
        self.os_type = os_type
        self.size = size
        self.user_name = user_name
        self.password = password
        self.ssh_key = ssh_key
        self.is_authentication_with_ssh_key = is_authentication_with_ssh_key
        self.fqdn = fqdn
        self.lab_subnet_name = lab_subnet_name
        self.lab_virtual_network_id = lab_virtual_network_id
        self.disallow_public_ip_address = disallow_public_ip_address
        self.artifacts = artifacts
        self.artifact_deployment_status = artifact_deployment_status
        self.gallery_image_reference = gallery_image_reference
        self.plan_id = plan_id
        self.compute_vm = None
        self.network_interface = network_interface
        self.applicable_schedule = None
        self.expiration_date = expiration_date
        self.allow_claim = allow_claim
        self.storage_type = storage_type
        self.virtual_machine_creation_source = virtual_machine_creation_source
        self.environment_id = environment_id
        self.data_disk_parameters = data_disk_parameters
        self.schedule_parameters = schedule_parameters
        self.last_known_power_state = last_known_power_state
        self.provisioning_state = None
        self.unique_identifier = None