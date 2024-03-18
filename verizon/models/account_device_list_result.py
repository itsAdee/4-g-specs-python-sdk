# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.thingspace_device import ThingspaceDevice


class AccountDeviceListResult(object):

    """Implementation of the 'AccountDeviceListResult' model.

    Response for a request to list down account devices.

    Attributes:
        devices (List[ThingspaceDevice]): Up to 10,000 devices that you want
            to move to a different account, specified by device identifier.
        has_more_data (bool): False for a status 200 response.True for a
            status 202 response, indicating that there is more data to be
            retrieved.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "devices": 'devices',
        "has_more_data": 'hasMoreData'
    }

    _optionals = [
        'devices',
        'has_more_data',
    ]

    def __init__(self,
                 devices=APIHelper.SKIP,
                 has_more_data=APIHelper.SKIP):
        """Constructor for the AccountDeviceListResult class"""

        # Initialize members of the class
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if has_more_data is not APIHelper.SKIP:
            self.has_more_data = has_more_data 

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
        devices = None
        if dictionary.get('devices') is not None:
            devices = [ThingspaceDevice.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(devices,
                   has_more_data)
