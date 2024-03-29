# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_identifier import AccountIdentifier


class GenerateExternalIDRequest(object):

    """Implementation of the 'GenerateExternalIDRequest' model.

    Authenticating account ID.

    Attributes:
        accountidentifier (AccountIdentifier): The ID of the authenticating
            billing account, in the format
            `{"billingaccountid":"1234567890-12345"}`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accountidentifier": 'accountidentifier'
    }

    _optionals = [
        'accountidentifier',
    ]

    def __init__(self,
                 accountidentifier=APIHelper.SKIP):
        """Constructor for the GenerateExternalIDRequest class"""

        # Initialize members of the class
        if accountidentifier is not APIHelper.SKIP:
            self.accountidentifier = accountidentifier 

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
        accountidentifier = AccountIdentifier.from_dictionary(dictionary.get('accountidentifier')) if 'accountidentifier' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(accountidentifier)
