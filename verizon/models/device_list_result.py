# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.models.v3_device import V3Device


class DeviceListResult(object):

    """Implementation of the 'DeviceListResult' model.

    Device list information.

    Attributes:
        account_name (str): Account name.
        device_count (int): Total device count.
        device_list (List[V3Device]): List of devices with id in IMEI.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "device_count": 'deviceCount',
        "device_list": 'deviceList'
    }

    def __init__(self,
                 account_name=None,
                 device_count=None,
                 device_list=None):
        """Constructor for the DeviceListResult class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.device_count = device_count 
        self.device_list = device_list 

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
        device_count = dictionary.get("deviceCount") if dictionary.get("deviceCount") else None
        device_list = None
        if dictionary.get('deviceList') is not None:
            device_list = [V3Device.from_dictionary(x) for x in dictionary.get('deviceList')]
        # Return an object of this model
        return cls(account_name,
                   device_count,
                   device_list)
