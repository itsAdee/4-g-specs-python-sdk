# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class V2DeviceStatus(object):

    """Implementation of the 'V2DeviceStatus' model.

    Device with id in IMEI.

    Attributes:
        device_id (str): Device IMEI.
        status (str): Success or failure.
        result_reason (str): Result reason.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'deviceId',
        "status": 'status',
        "result_reason": 'resultReason'
    }

    _optionals = [
        'result_reason',
    ]

    def __init__(self,
                 device_id=None,
                 status=None,
                 result_reason=APIHelper.SKIP):
        """Constructor for the V2DeviceStatus class"""

        # Initialize members of the class
        self.device_id = device_id 
        self.status = status 
        if result_reason is not APIHelper.SKIP:
            self.result_reason = result_reason 

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
        device_id = dictionary.get("deviceId") if dictionary.get("deviceId") else None
        status = dictionary.get("status") if dictionary.get("status") else None
        result_reason = dictionary.get("resultReason") if dictionary.get("resultReason") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_id,
                   status,
                   result_reason)
