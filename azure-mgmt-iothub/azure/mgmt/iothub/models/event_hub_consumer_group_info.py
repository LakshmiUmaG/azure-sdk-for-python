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


class EventHubConsumerGroupInfo(Model):
    """The properties of the EventHubConsumerGroupInfo object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param properties: The tags.
    :type properties: dict[str, str]
    :ivar id: The Event Hub-compatible consumer group identifier.
    :vartype id: str
    :ivar name: The Event Hub-compatible consumer group name.
    :vartype name: str
    :ivar type: the resource type.
    :vartype type: str
    :ivar etag: The etag.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EventHubConsumerGroupInfo, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)
        self.id = None
        self.name = None
        self.type = None
        self.etag = None
