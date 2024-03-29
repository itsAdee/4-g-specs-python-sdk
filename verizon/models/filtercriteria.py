# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.ready_sim_service_plan import ReadySimServicePlan


class Filtercriteria(object):

    """Implementation of the 'filtercriteria' model.

    TODO: type model description here.

    Attributes:
        filter_criteria (List[ReadySimServicePlan]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filter_criteria": 'filterCriteria'
    }

    _optionals = [
        'filter_criteria',
    ]

    def __init__(self,
                 filter_criteria=APIHelper.SKIP):
        """Constructor for the Filtercriteria class"""

        # Initialize members of the class
        if filter_criteria is not APIHelper.SKIP:
            self.filter_criteria = filter_criteria 

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
        filter_criteria = None
        if dictionary.get('filterCriteria') is not None:
            filter_criteria = [ReadySimServicePlan.from_dictionary(x) for x in dictionary.get('filterCriteria')]
        else:
            filter_criteria = APIHelper.SKIP
        # Return an object of this model
        return cls(filter_criteria)
