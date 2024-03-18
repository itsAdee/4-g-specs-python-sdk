# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_id import DeviceId


class NotificationReportStatusRequest(object):

    """Implementation of the 'NotificationReportStatusRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (str): The name of a billing account.
        device (DeviceId): An identifier for a single device.
        request_type (str): The type of request.
        request_expiration_time (str): The time at which the request expires.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "device": 'device',
        "request_type": 'requestType',
        "request_expiration_time": 'requestExpirationTime'
    }

    _optionals = [
        'request_expiration_time',
    ]

    def __init__(self,
                 account_name=None,
                 device=None,
                 request_type=None,
                 request_expiration_time=APIHelper.SKIP):
        """Constructor for the NotificationReportStatusRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.device = device 
        self.request_type = request_type 
        if request_expiration_time is not APIHelper.SKIP:
            self.request_expiration_time = request_expiration_time 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        device = DeviceId.from_dictionary(dictionary.get('device')) if dictionary.get('device') else None
        request_type = dictionary.get("requestType") if dictionary.get("requestType") else None
        request_expiration_time = dictionary.get("requestExpirationTime") if dictionary.get("requestExpirationTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   device,
                   request_type,
                   request_expiration_time)
