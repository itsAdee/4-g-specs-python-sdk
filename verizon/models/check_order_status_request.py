# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_list import DeviceList


class CheckOrderStatusRequest(object):

    """Implementation of the 'CheckOrderStatusRequest' model.

    The request body identifies the devices to upload.

    Attributes:
        account_name (str): The name of a billing account. An account name is
            usually numeric, and must include any leading zeros.
        order_request_id (str): The request id from the activation order.
        devices (List[DeviceList]): The devices to upload, specified by device
            IDs in a format matching uploadType.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "devices": 'devices',
        "order_request_id": 'orderRequestId'
    }

    _optionals = [
        'order_request_id',
    ]

    def __init__(self,
                 account_name=None,
                 devices=None,
                 order_request_id=APIHelper.SKIP):
        """Constructor for the CheckOrderStatusRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        if order_request_id is not APIHelper.SKIP:
            self.order_request_id = order_request_id 
        self.devices = devices 

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
        devices = None
        if dictionary.get('devices') is not None:
            devices = [DeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        order_request_id = dictionary.get("orderRequestId") if dictionary.get("orderRequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   devices,
                   order_request_id)
