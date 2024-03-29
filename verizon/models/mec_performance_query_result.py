# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class MECPerformanceQueryResult(object):

    """Implementation of the 'MECPerformanceQueryResult' model.

    Result of the query for obtaining MEC performance metrics.

    Attributes:
        name (str): Name of the parameter.
        data (List[str]): Parameter values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "data": 'data'
    }

    _optionals = [
        'name',
        'data',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 data=APIHelper.SKIP):
        """Constructor for the MECPerformanceQueryResult class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if data is not APIHelper.SKIP:
            self.data = data 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        data = dictionary.get("data") if dictionary.get("data") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   data)
