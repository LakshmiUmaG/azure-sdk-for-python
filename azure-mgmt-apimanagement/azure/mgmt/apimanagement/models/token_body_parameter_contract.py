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


class TokenBodyParameterContract(Model):
    """OAuth acquire token request body parameter (www-url-form-encoded).

    All required parameters must be populated in order to send to Azure.

    :param name: Required. body parameter name.
    :type name: str
    :param value: Required. body parameter value.
    :type value: str
    """

    _validation = {
        'name': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TokenBodyParameterContract, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.value = kwargs.get('value', None)
