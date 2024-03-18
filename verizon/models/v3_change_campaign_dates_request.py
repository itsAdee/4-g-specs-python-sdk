# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from verizon.api_helper import APIHelper
from verizon.models.v3_time_window import V3TimeWindow


class V3ChangeCampaignDatesRequest(object):

    """Implementation of the 'V3ChangeCampaignDatesRequest' model.

    Campaign dates and time windows.

    Attributes:
        start_date (date): Campaign start date.
        end_date (date): Campaign end date.
        campaign_time_window_list (List[V3TimeWindow]): List of allowed
            campaign time windows.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_date": 'startDate',
        "end_date": 'endDate',
        "campaign_time_window_list": 'campaignTimeWindowList'
    }

    _optionals = [
        'campaign_time_window_list',
    ]

    def __init__(self,
                 start_date=None,
                 end_date=None,
                 campaign_time_window_list=APIHelper.SKIP):
        """Constructor for the V3ChangeCampaignDatesRequest class"""

        # Initialize members of the class
        self.start_date = start_date 
        self.end_date = end_date 
        if campaign_time_window_list is not APIHelper.SKIP:
            self.campaign_time_window_list = campaign_time_window_list 

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
        start_date = dateutil.parser.parse(dictionary.get('startDate')).date() if dictionary.get('startDate') else None
        end_date = dateutil.parser.parse(dictionary.get('endDate')).date() if dictionary.get('endDate') else None
        campaign_time_window_list = None
        if dictionary.get('campaignTimeWindowList') is not None:
            campaign_time_window_list = [V3TimeWindow.from_dictionary(x) for x in dictionary.get('campaignTimeWindowList')]
        else:
            campaign_time_window_list = APIHelper.SKIP
        # Return an object of this model
        return cls(start_date,
                   end_date,
                   campaign_time_window_list)