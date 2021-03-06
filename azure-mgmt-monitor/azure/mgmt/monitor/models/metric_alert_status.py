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


class MetricAlertStatus(Model):
    """An alert status.

    :param name: The status name.
    :type name: str
    :param id: The alert rule arm id.
    :type id: str
    :param type: The extended resource type name.
    :type type: str
    :param properties: The alert status properties of the metric alert status.
    :type properties: ~azure.mgmt.monitor.models.MetricAlertStatusProperties
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'MetricAlertStatusProperties'},
    }

    def __init__(self, **kwargs):
        super(MetricAlertStatus, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.id = kwargs.get('id', None)
        self.type = kwargs.get('type', None)
        self.properties = kwargs.get('properties', None)
