# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.custom_fields import CustomFields
from verizon.models.device_id import DeviceId


class DevicePrlListRequest(object):

    """Implementation of the 'DevicePrlListRequest' model.

    Requests the current PRL (Preferred Roaming List) version for 2G or 3G
    devices, which can help determine which devices need a PRL update. (4G and
    GSM devices do not have a PRL.).

    Attributes:
        device_ids (List[DeviceId]): The devices for which you want the PRL
            version, specified by device identifier. You only need to provide
            one identifier per device. Do not use any of the other parameters
            if you specify device IDs.
        account_name (str): The name of a billing account. This parameter is
            only required if you are passing groupName and the UWS account
            used for the current API session has access to multiple billing
            accounts, because the same device group name can exist in multiple
            accounts.An account name is usually numeric, and must include any
            leading zeros.
        custom_fields (List[CustomFields]): The names and values of custom
            fields, if you want to only include devices that have matching
            custom fields.
        group_name (str): The name of a device group, if you want to only
            include devices in that group.
        service_plan (str): The name of a service plan, if you want to only
            include devices that have that service plan.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_ids": 'deviceIds',
        "account_name": 'accountName',
        "custom_fields": 'customFields',
        "group_name": 'groupName',
        "service_plan": 'servicePlan'
    }

    _optionals = [
        'device_ids',
        'account_name',
        'custom_fields',
        'group_name',
        'service_plan',
    ]

    def __init__(self,
                 device_ids=APIHelper.SKIP,
                 account_name=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP):
        """Constructor for the DevicePrlListRequest class"""

        # Initialize members of the class
        if device_ids is not APIHelper.SKIP:
            self.device_ids = device_ids 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 

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
        device_ids = None
        if dictionary.get('deviceIds') is not None:
            device_ids = [DeviceId.from_dictionary(x) for x in dictionary.get('deviceIds')]
        else:
            device_ids = APIHelper.SKIP
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [CustomFields.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_ids,
                   account_name,
                   custom_fields,
                   group_name,
                   service_plan)
