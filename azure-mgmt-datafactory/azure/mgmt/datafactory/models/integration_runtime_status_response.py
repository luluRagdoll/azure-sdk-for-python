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


class IntegrationRuntimeStatusResponse(Model):
    """Integration runtime status response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The integration runtime name.
    :vartype name: str
    :param properties: Integration runtime properties.
    :type properties: :class:`IntegrationRuntimeStatus
     <azure.mgmt.datafactory.models.IntegrationRuntimeStatus>`
    """

    _validation = {
        'name': {'readonly': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'IntegrationRuntimeStatus'},
    }

    def __init__(self, properties):
        self.name = None
        self.properties = properties