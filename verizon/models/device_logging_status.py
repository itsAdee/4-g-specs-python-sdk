# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser


class DeviceLoggingStatus(object):

    """Implementation of the 'DeviceLoggingStatus' model.

    Device logging status information.

    Attributes:
        device_id (str): Device IMEI.
        expiry_date (date): The date when device logging expires.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'deviceId',
        "expiry_date": 'expiryDate'
    }

    def __init__(self,
                 device_id=None,
                 expiry_date=None):
        """Constructor for the DeviceLoggingStatus class"""

        # Initialize members of the class
        self.device_id = device_id 
        self.expiry_date = expiry_date 

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
        expiry_date = dateutil.parser.parse(dictionary.get('expiryDate')).date() if dictionary.get('expiryDate') else None
        # Return an object of this model
        return cls(device_id,
                   expiry_date)
