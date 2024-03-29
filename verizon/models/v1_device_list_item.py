# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class V1DeviceListItem(object):

    """Implementation of the 'V1DeviceListItem' model.

    A JSON object for each device that was included in the request, showing
    the device IMEI, the status of the addition or removal, and additional
    information about the status.

    Attributes:
        device_id (str): Device IMEI.
        status (str): Whether the device was successfully added or removed
            from the campaign.
        reason (str): Additional details about the status.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'deviceId',
        "status": 'status',
        "reason": 'Reason'
    }

    _optionals = [
        'device_id',
        'status',
        'reason',
    ]

    def __init__(self,
                 device_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 reason=APIHelper.SKIP):
        """Constructor for the V1DeviceListItem class"""

        # Initialize members of the class
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if reason is not APIHelper.SKIP:
            self.reason = reason 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        device_id = dictionary.get("deviceId") if dictionary.get("deviceId") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        reason = dictionary.get("Reason") if dictionary.get("Reason") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_id,
                   status,
                   reason)
