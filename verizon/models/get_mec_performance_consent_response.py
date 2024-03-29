# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class GetMECPerformanceConsentResponse(object):

    """Implementation of the 'GetMECPerformanceConsentResponse' model.

    MEC Performance Consent Response

    Attributes:
        consent (str): MEC Performance Consent Response.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "consent": 'consent'
    }

    _optionals = [
        'consent',
    ]

    def __init__(self,
                 consent=APIHelper.SKIP):
        """Constructor for the GetMECPerformanceConsentResponse class"""

        # Initialize members of the class
        if consent is not APIHelper.SKIP:
            self.consent = consent 

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
        consent = dictionary.get("consent") if dictionary.get("consent") else APIHelper.SKIP
        # Return an object of this model
        return cls(consent)
