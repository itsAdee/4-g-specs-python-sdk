# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class V3DeviceStatus(object):

    """Implementation of the 'V3DeviceStatus' model.

    Device status.

    Attributes:
        device_id (str): Device IMEI.
        status (str): Success or failure.
        result_reason (str): Result reason.
        updated_time (datetime): Updated Time.
        recent_attempt_time (datetime): The most recent attempt time.
        next_attempt_time (datetime): Next attempt time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'deviceId',
        "status": 'status',
        "result_reason": 'resultReason',
        "updated_time": 'updatedTime',
        "recent_attempt_time": 'recentAttemptTime',
        "next_attempt_time": 'nextAttemptTime'
    }

    _optionals = [
        'result_reason',
        'updated_time',
        'recent_attempt_time',
        'next_attempt_time',
    ]

    def __init__(self,
                 device_id=None,
                 status=None,
                 result_reason=APIHelper.SKIP,
                 updated_time=APIHelper.SKIP,
                 recent_attempt_time=APIHelper.SKIP,
                 next_attempt_time=APIHelper.SKIP):
        """Constructor for the V3DeviceStatus class"""

        # Initialize members of the class
        self.device_id = device_id 
        self.status = status 
        if result_reason is not APIHelper.SKIP:
            self.result_reason = result_reason 
        if updated_time is not APIHelper.SKIP:
            self.updated_time = APIHelper.apply_datetime_converter(updated_time, APIHelper.RFC3339DateTime) if updated_time else None 
        if recent_attempt_time is not APIHelper.SKIP:
            self.recent_attempt_time = APIHelper.apply_datetime_converter(recent_attempt_time, APIHelper.RFC3339DateTime) if recent_attempt_time else None 
        if next_attempt_time is not APIHelper.SKIP:
            self.next_attempt_time = APIHelper.apply_datetime_converter(next_attempt_time, APIHelper.RFC3339DateTime) if next_attempt_time else None 

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
        updated_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("updatedTime")).datetime if dictionary.get("updatedTime") else APIHelper.SKIP
        recent_attempt_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("recentAttemptTime")).datetime if dictionary.get("recentAttemptTime") else APIHelper.SKIP
        next_attempt_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("nextAttemptTime")).datetime if dictionary.get("nextAttemptTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_id,
                   status,
                   result_reason,
                   updated_time,
                   recent_attempt_time,
                   next_attempt_time)
