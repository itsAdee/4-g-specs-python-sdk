# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.api_response_code import ApiResponseCode


class DeviceServiceInformation(object):

    """Implementation of the 'DeviceServiceInformation' model.

    Device service information.

    Attributes:
        response_type (ApiResponseCode): ResponseCode and/or a message
            indicating success or failure of the request.
        imei (str): The International Mobile Equipment Identifier of the
            device.
        bullseye_enable (bool): Shows if Hyper Precise is enabled (true) or
            disabled (false).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "imei": 'imei',
        "bullseye_enable": 'BullseyeEnable',
        "response_type": 'responseType'
    }

    _optionals = [
        'response_type',
    ]

    def __init__(self,
                 imei=None,
                 bullseye_enable=None,
                 response_type=APIHelper.SKIP):
        """Constructor for the DeviceServiceInformation class"""

        # Initialize members of the class
        if response_type is not APIHelper.SKIP:
            self.response_type = response_type 
        self.imei = imei 
        self.bullseye_enable = bullseye_enable 

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
        imei = dictionary.get("imei") if dictionary.get("imei") else None
        bullseye_enable = dictionary.get("BullseyeEnable") if "BullseyeEnable" in dictionary.keys() else None
        response_type = ApiResponseCode.from_dictionary(dictionary.get('responseType')) if 'responseType' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(imei,
                   bullseye_enable,
                   response_type)
