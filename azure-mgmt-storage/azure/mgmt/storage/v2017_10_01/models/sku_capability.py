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


class SKUCapability(Model):
    """The capability information in the specified sku, including file encryption,
    network acls, change notification, etc.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of capability, The capability information in the
     specified sku, including file encryption, network acls, change
     notification, etc.
    :vartype name: str
    :ivar value: A string value to indicate states of given capability.
     Possibly 'true' or 'false'.
    :vartype value: str
    """

    _validation = {
        'name': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self):
        super(SKUCapability, self).__init__()
        self.name = None
        self.value = None