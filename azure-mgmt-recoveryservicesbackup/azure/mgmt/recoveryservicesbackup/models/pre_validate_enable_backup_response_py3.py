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


class PreValidateEnableBackupResponse(Model):
    """Response contract for enable backup validation request.

    :param status: Validation Status. Possible values include: 'Invalid',
     'Succeeded', 'Failed'
    :type status: str or
     ~azure.mgmt.recoveryservicesbackup.models.ValidationStatus
    :param error_code: Response error code
    :type error_code: str
    :param error_message: Response error message
    :type error_message: str
    :param recommendation: Recommended action for user
    :type recommendation: str
    :param container_name: Specifies the product specific container name. E.g.
     iaasvmcontainer;iaasvmcontainer;rgname;vmname. This is required for portal
    :type container_name: str
    :param protected_item_name: Specifies the product specific ds name. E.g.
     vm;iaasvmcontainer;rgname;vmname. This is required for portal
    :type protected_item_name: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'recommendation': {'key': 'recommendation', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'protected_item_name': {'key': 'protectedItemName', 'type': 'str'},
    }

    def __init__(self, *, status=None, error_code: str=None, error_message: str=None, recommendation: str=None, container_name: str=None, protected_item_name: str=None, **kwargs) -> None:
        super(PreValidateEnableBackupResponse, self).__init__(**kwargs)
        self.status = status
        self.error_code = error_code
        self.error_message = error_message
        self.recommendation = recommendation
        self.container_name = container_name
        self.protected_item_name = protected_item_name
