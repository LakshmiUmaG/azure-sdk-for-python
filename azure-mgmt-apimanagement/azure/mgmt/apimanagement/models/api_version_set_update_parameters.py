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


class ApiVersionSetUpdateParameters(Model):
    """Parameters to update or create an Api Version Set Contract.

    :param description: Description of API Version Set.
    :type description: str
    :param version_query_name: Name of query parameter that indicates the API
     Version if versioningScheme is set to `query`.
    :type version_query_name: str
    :param version_header_name: Name of HTTP header parameter that indicates
     the API Version if versioningScheme is set to `header`.
    :type version_header_name: str
    :param display_name: Name of API Version Set
    :type display_name: str
    :param versioning_scheme: An value that determines where the API Version
     identifer will be located in a HTTP request. Possible values include:
     'Segment', 'Query', 'Header'
    :type versioning_scheme: str or
     ~azure.mgmt.apimanagement.models.VersioningScheme
    """

    _validation = {
        'version_query_name': {'max_length': 100, 'min_length': 1},
        'version_header_name': {'max_length': 100, 'min_length': 1},
        'display_name': {'max_length': 100, 'min_length': 1},
    }

    _attribute_map = {
        'description': {'key': 'properties.description', 'type': 'str'},
        'version_query_name': {'key': 'properties.versionQueryName', 'type': 'str'},
        'version_header_name': {'key': 'properties.versionHeaderName', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'versioning_scheme': {'key': 'properties.versioningScheme', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApiVersionSetUpdateParameters, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.version_query_name = kwargs.get('version_query_name', None)
        self.version_header_name = kwargs.get('version_header_name', None)
        self.display_name = kwargs.get('display_name', None)
        self.versioning_scheme = kwargs.get('versioning_scheme', None)
