# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.firmware_upgrade_device_list_item import FirmwareUpgradeDeviceListItem


class FirmwareUpgrade(object):

    """Implementation of the 'FirmwareUpgrade' model.

    Array of upgrade objects with the specified status.

    Attributes:
        id (str): The unique identifier for this upgrade.
        account_name (str): Account identifier in "##########-#####".
        firmware_name (str): The name of the firmware image that will be used
            for the upgrade.
        firmware_to (str): The name of the firmware version that will be on
            the devices after a successful upgrade.
        start_date (str): The intended start date for the upgrade.
        status (str): The current status of the upgrade.
        device_list (List[FirmwareUpgradeDeviceListItem]): A JSON object for
            each device that was included in the upgrade, showing the device
            IMEI, the status of the upgrade, and additional information about
            the status.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "account_name": 'accountName',
        "firmware_name": 'firmwareName',
        "firmware_to": 'firmwareTo',
        "start_date": 'startDate',
        "status": 'status',
        "device_list": 'deviceList'
    }

    _optionals = [
        'id',
        'account_name',
        'firmware_name',
        'firmware_to',
        'start_date',
        'status',
        'device_list',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 account_name=APIHelper.SKIP,
                 firmware_name=APIHelper.SKIP,
                 firmware_to=APIHelper.SKIP,
                 start_date=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 device_list=APIHelper.SKIP):
        """Constructor for the FirmwareUpgrade class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if firmware_name is not APIHelper.SKIP:
            self.firmware_name = firmware_name 
        if firmware_to is not APIHelper.SKIP:
            self.firmware_to = firmware_to 
        if start_date is not APIHelper.SKIP:
            self.start_date = start_date 
        if status is not APIHelper.SKIP:
            self.status = status 
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        firmware_name = dictionary.get("firmwareName") if dictionary.get("firmwareName") else APIHelper.SKIP
        firmware_to = dictionary.get("firmwareTo") if dictionary.get("firmwareTo") else APIHelper.SKIP
        start_date = dictionary.get("startDate") if dictionary.get("startDate") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        device_list = None
        if dictionary.get('deviceList') is not None:
            device_list = [FirmwareUpgradeDeviceListItem.from_dictionary(x) for x in dictionary.get('deviceList')]
        else:
            device_list = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   account_name,
                   firmware_name,
                   firmware_to,
                   start_date,
                   status,
                   device_list)
