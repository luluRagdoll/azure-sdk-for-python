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


class ReservationMergeProperties(Model):
    """ReservationMergeProperties.

    :param merge_destination: Reservation Resource Id Created due to the
     merge. Format of the resource Id is
     /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
    :type merge_destination: str
    :param merge_sources: Resource Ids of the Source Reservation's merged to
     form this Reservation. Format of the resource Id is
     /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
    :type merge_sources: list[str]
    """

    _attribute_map = {
        'merge_destination': {'key': 'mergeDestination', 'type': 'str'},
        'merge_sources': {'key': 'mergeSources', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ReservationMergeProperties, self).__init__(**kwargs)
        self.merge_destination = kwargs.get('merge_destination', None)
        self.merge_sources = kwargs.get('merge_sources', None)
