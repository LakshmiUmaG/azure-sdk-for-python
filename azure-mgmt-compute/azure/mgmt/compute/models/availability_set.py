# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class AvailabilitySet(Resource):
    """Create or update Availability Set parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param platform_update_domain_count: Update Domain count.
    :type platform_update_domain_count: int
    :param platform_fault_domain_count: Fault Domain count.
    :type platform_fault_domain_count: int
    :param virtual_machines: a list containing reference to all Virtual
     Machines created under this Availability Set.
    :type virtual_machines: list of :class:`SubResource
     <azure.mgmt.compute.models.SubResource>`
    :param statuses: the resource status information.
    :type statuses: list of :class:`InstanceViewStatus
     <azure.mgmt.compute.models.InstanceViewStatus>`
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'platform_update_domain_count': {'key': 'properties.platformUpdateDomainCount', 'type': 'int'},
        'platform_fault_domain_count': {'key': 'properties.platformFaultDomainCount', 'type': 'int'},
        'virtual_machines': {'key': 'properties.virtualMachines', 'type': '[SubResource]'},
        'statuses': {'key': 'properties.statuses', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, location, tags=None, platform_update_domain_count=None, platform_fault_domain_count=None, virtual_machines=None, statuses=None):
        super(AvailabilitySet, self).__init__(location=location, tags=tags)
        self.platform_update_domain_count = platform_update_domain_count
        self.platform_fault_domain_count = platform_fault_domain_count
        self.virtual_machines = virtual_machines
        self.statuses = statuses