# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.notification import Notification
from verizon.models.trigger_attributes_options import TriggerAttributesOptions
from verizon.models.usage_anomaly_attributes import UsageAnomalyAttributes


class TriggersListOptions(object):

    """Implementation of the 'TriggersListOptions' model.

    TODO: type model description here.

    Attributes:
        trigger_id (str): The system assigned name of the trigger being
            updated.
        trigger_name (str): The user defined name of the trigger.
        organization_name (str): The user assigned name of the organization
            associated with the trigger.
        trigger_category (str): This is the value to use in the request body
            to detect anomalous behaivior. The values in this table will only
            be relevant when this parameter is set to this value.
        trigger_attributes (List[TriggerAttributesOptions]): Additional
            details and keys for the trigger.
        created_at (str): Timestamp for whe the trigger was created.
        modified_at (str): Timestamp for the most recent time the trigger was
            modified.
        anomalyattributes (UsageAnomalyAttributes): The details of the
            UsageAnomaly trigger.
        notification (Notification): The notification details of the trigger.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "trigger_id": 'triggerId',
        "trigger_name": 'triggerName',
        "organization_name": 'organizationName',
        "trigger_category": 'triggerCategory',
        "trigger_attributes": 'triggerAttributes',
        "created_at": 'createdAt',
        "modified_at": 'modifiedAt',
        "anomalyattributes": 'anomalyattributes',
        "notification": 'notification'
    }

    _optionals = [
        'trigger_id',
        'trigger_name',
        'organization_name',
        'trigger_category',
        'trigger_attributes',
        'created_at',
        'modified_at',
        'anomalyattributes',
        'notification',
    ]

    def __init__(self,
                 trigger_id=APIHelper.SKIP,
                 trigger_name=APIHelper.SKIP,
                 organization_name=APIHelper.SKIP,
                 trigger_category=APIHelper.SKIP,
                 trigger_attributes=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 modified_at=APIHelper.SKIP,
                 anomalyattributes=APIHelper.SKIP,
                 notification=APIHelper.SKIP):
        """Constructor for the TriggersListOptions class"""

        # Initialize members of the class
        if trigger_id is not APIHelper.SKIP:
            self.trigger_id = trigger_id 
        if trigger_name is not APIHelper.SKIP:
            self.trigger_name = trigger_name 
        if organization_name is not APIHelper.SKIP:
            self.organization_name = organization_name 
        if trigger_category is not APIHelper.SKIP:
            self.trigger_category = trigger_category 
        if trigger_attributes is not APIHelper.SKIP:
            self.trigger_attributes = trigger_attributes 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if modified_at is not APIHelper.SKIP:
            self.modified_at = modified_at 
        if anomalyattributes is not APIHelper.SKIP:
            self.anomalyattributes = anomalyattributes 
        if notification is not APIHelper.SKIP:
            self.notification = notification 

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
        trigger_id = dictionary.get("triggerId") if dictionary.get("triggerId") else APIHelper.SKIP
        trigger_name = dictionary.get("triggerName") if dictionary.get("triggerName") else APIHelper.SKIP
        organization_name = dictionary.get("organizationName") if dictionary.get("organizationName") else APIHelper.SKIP
        trigger_category = dictionary.get("triggerCategory") if dictionary.get("triggerCategory") else APIHelper.SKIP
        trigger_attributes = None
        if dictionary.get('triggerAttributes') is not None:
            trigger_attributes = [TriggerAttributesOptions.from_dictionary(x) for x in dictionary.get('triggerAttributes')]
        else:
            trigger_attributes = APIHelper.SKIP
        created_at = dictionary.get("createdAt") if dictionary.get("createdAt") else APIHelper.SKIP
        modified_at = dictionary.get("modifiedAt") if dictionary.get("modifiedAt") else APIHelper.SKIP
        anomalyattributes = UsageAnomalyAttributes.from_dictionary(dictionary.get('anomalyattributes')) if 'anomalyattributes' in dictionary.keys() else APIHelper.SKIP
        notification = Notification.from_dictionary(dictionary.get('notification')) if 'notification' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(trigger_id,
                   trigger_name,
                   organization_name,
                   trigger_category,
                   trigger_attributes,
                   created_at,
                   modified_at,
                   anomalyattributes,
                   notification)