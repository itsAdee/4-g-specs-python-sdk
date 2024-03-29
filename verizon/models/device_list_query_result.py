# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_list_query_item import DeviceListQueryItem


class DeviceListQueryResult(object):

    """Implementation of the 'DeviceListQueryResult' model.

    List of devices.

    Attributes:
        account_name (str): Account identifier in "##########-#####".
        has_more_data (bool): True if there are more devices to retrieve.
        last_seen_device_id (long|int): If hasMoreData=true, the startIndex to
            use for the next request. 0 if hasMoreData=false.
        device_list (List[DeviceListQueryItem]): The list of devices in the
            account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "has_more_data": 'hasMoreData',
        "last_seen_device_id": 'lastSeenDeviceId',
        "device_list": 'deviceList'
    }

    _optionals = [
        'account_name',
        'has_more_data',
        'last_seen_device_id',
        'device_list',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 has_more_data=APIHelper.SKIP,
                 last_seen_device_id=APIHelper.SKIP,
                 device_list=APIHelper.SKIP):
        """Constructor for the DeviceListQueryResult class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if has_more_data is not APIHelper.SKIP:
            self.has_more_data = has_more_data 
        if last_seen_device_id is not APIHelper.SKIP:
            self.last_seen_device_id = last_seen_device_id 
        if device_list is not APIHelper.SKIP:
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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else APIHelper.SKIP
        last_seen_device_id = dictionary.get("lastSeenDeviceId") if dictionary.get("lastSeenDeviceId") else APIHelper.SKIP
        device_list = None
        if dictionary.get('deviceList') is not None:
            device_list = [DeviceListQueryItem.from_dictionary(x) for x in dictionary.get('deviceList')]
        else:
            device_list = APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   has_more_data,
                   last_seen_device_id,
                   device_list)
