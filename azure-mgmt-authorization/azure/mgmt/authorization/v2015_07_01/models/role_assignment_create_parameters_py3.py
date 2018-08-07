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


class RoleAssignmentCreateParameters(Model):
    """Role assignment create parameters.

    :param properties: Role assignment properties.
    :type properties:
     ~azure.mgmt.authorization.v2015_07_01.models.RoleAssignmentProperties
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'RoleAssignmentProperties'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(RoleAssignmentCreateParameters, self).__init__(**kwargs)
        self.properties = properties