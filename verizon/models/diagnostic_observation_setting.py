# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.attribute_setting import AttributeSetting
from verizon.models.device import Device


class DiagnosticObservationSetting(object):

    """Implementation of the 'DiagnosticObservationSetting' model.

    Diagnostic observation settings and attributes for a device.

    Attributes:
        account_name (str): The name of the billing account for which callback
            messages will be sent. Format: "##########-#####".
        device (Device): Identifies a particular IoT device.
        attributes (List[AttributeSetting]): Streaming RF parameters for which
            you want to retrieve diagnostic settings.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "device": 'device',
        "attributes": 'attributes'
    }

    _optionals = [
        'account_name',
        'device',
        'attributes',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 device=APIHelper.SKIP,
                 attributes=APIHelper.SKIP):
        """Constructor for the DiagnosticObservationSetting class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if device is not APIHelper.SKIP:
            self.device = device 
        if attributes is not APIHelper.SKIP:
            self.attributes = attributes 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        device = Device.from_dictionary(dictionary.get('device')) if 'device' in dictionary.keys() else APIHelper.SKIP
        attributes = None
        if dictionary.get('attributes') is not None:
            attributes = [AttributeSetting.from_dictionary(x) for x in dictionary.get('attributes')]
        else:
            attributes = APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   device,
                   attributes)
