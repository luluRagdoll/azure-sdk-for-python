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

from .dataset_py3 import Dataset


class AzureBlobDataset(Dataset):
    """The Azure Blob storage.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Dataset description.
    :type description: str
    :param structure: Columns that define the structure of the dataset. Type:
     array (or Expression with resultType array), itemType: DatasetDataElement.
    :type structure: object
    :param linked_service_name: Required. Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param parameters: Parameters for dataset.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param folder: The folder that this Dataset is in. If not specified,
     Dataset will appear at the root level.
    :type folder: ~azure.mgmt.datafactory.models.DatasetFolder
    :param type: Required. Constant filled by server.
    :type type: str
    :param folder_path: The path of the Azure Blob storage. Type: string (or
     Expression with resultType string).
    :type folder_path: object
    :param table_root_location: The root of blob path. Type: string (or
     Expression with resultType string).
    :type table_root_location: object
    :param file_name: The name of the Azure Blob. Type: string (or Expression
     with resultType string).
    :type file_name: object
    :param format: The format of the Azure Blob storage.
    :type format: ~azure.mgmt.datafactory.models.DatasetStorageFormat
    :param compression: The data compression method used for the blob storage.
    :type compression: ~azure.mgmt.datafactory.models.DatasetCompression
    """

    _validation = {
        'linked_service_name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'structure': {'key': 'structure', 'type': 'object'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'folder': {'key': 'folder', 'type': 'DatasetFolder'},
        'type': {'key': 'type', 'type': 'str'},
        'folder_path': {'key': 'typeProperties.folderPath', 'type': 'object'},
        'table_root_location': {'key': 'typeProperties.tableRootLocation', 'type': 'object'},
        'file_name': {'key': 'typeProperties.fileName', 'type': 'object'},
        'format': {'key': 'typeProperties.format', 'type': 'DatasetStorageFormat'},
        'compression': {'key': 'typeProperties.compression', 'type': 'DatasetCompression'},
    }

    def __init__(self, *, linked_service_name, additional_properties=None, description: str=None, structure=None, parameters=None, annotations=None, folder=None, folder_path=None, table_root_location=None, file_name=None, format=None, compression=None, **kwargs) -> None:
        super(AzureBlobDataset, self).__init__(additional_properties=additional_properties, description=description, structure=structure, linked_service_name=linked_service_name, parameters=parameters, annotations=annotations, folder=folder, **kwargs)
        self.folder_path = folder_path
        self.table_root_location = table_root_location
        self.file_name = file_name
        self.format = format
        self.compression = compression
        self.type = 'AzureBlob'
