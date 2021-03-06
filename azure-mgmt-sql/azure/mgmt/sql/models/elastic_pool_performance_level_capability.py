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


class ElasticPoolPerformanceLevelCapability(Model):
    """The Elastic Pool performance level capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar performance_level: The performance level for the pool.
    :vartype performance_level:
     ~azure.mgmt.sql.models.PerformanceLevelCapability
    :ivar sku: The sku.
    :vartype sku: ~azure.mgmt.sql.models.Sku
    :ivar supported_license_types: List of supported license types.
    :vartype supported_license_types:
     list[~azure.mgmt.sql.models.LicenseTypeCapability]
    :ivar max_database_count: The maximum number of databases supported.
    :vartype max_database_count: int
    :ivar included_max_size: The included (free) max size for this performance
     level.
    :vartype included_max_size: ~azure.mgmt.sql.models.MaxSizeCapability
    :ivar supported_max_sizes: The list of supported max sizes.
    :vartype supported_max_sizes:
     list[~azure.mgmt.sql.models.MaxSizeRangeCapability]
    :ivar supported_per_database_max_sizes: The list of supported per database
     max sizes.
    :vartype supported_per_database_max_sizes:
     list[~azure.mgmt.sql.models.MaxSizeRangeCapability]
    :ivar supported_per_database_max_performance_levels: The list of supported
     per database max performance levels.
    :vartype supported_per_database_max_performance_levels:
     list[~azure.mgmt.sql.models.ElasticPoolPerDatabaseMaxPerformanceLevelCapability]
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :param reason: The reason for the capability not being available.
    :type reason: str
    """

    _validation = {
        'performance_level': {'readonly': True},
        'sku': {'readonly': True},
        'supported_license_types': {'readonly': True},
        'max_database_count': {'readonly': True},
        'included_max_size': {'readonly': True},
        'supported_max_sizes': {'readonly': True},
        'supported_per_database_max_sizes': {'readonly': True},
        'supported_per_database_max_performance_levels': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'performance_level': {'key': 'performanceLevel', 'type': 'PerformanceLevelCapability'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'supported_license_types': {'key': 'supportedLicenseTypes', 'type': '[LicenseTypeCapability]'},
        'max_database_count': {'key': 'maxDatabaseCount', 'type': 'int'},
        'included_max_size': {'key': 'includedMaxSize', 'type': 'MaxSizeCapability'},
        'supported_max_sizes': {'key': 'supportedMaxSizes', 'type': '[MaxSizeRangeCapability]'},
        'supported_per_database_max_sizes': {'key': 'supportedPerDatabaseMaxSizes', 'type': '[MaxSizeRangeCapability]'},
        'supported_per_database_max_performance_levels': {'key': 'supportedPerDatabaseMaxPerformanceLevels', 'type': '[ElasticPoolPerDatabaseMaxPerformanceLevelCapability]'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ElasticPoolPerformanceLevelCapability, self).__init__(**kwargs)
        self.performance_level = None
        self.sku = None
        self.supported_license_types = None
        self.max_database_count = None
        self.included_max_size = None
        self.supported_max_sizes = None
        self.supported_per_database_max_sizes = None
        self.supported_per_database_max_performance_levels = None
        self.status = None
        self.reason = kwargs.get('reason', None)
