# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ManagedAccAddedList(object):

    """Implementation of the 'ManagedAccAddedList' model.

    TODO: type model description here.

    Attributes:
        id (str): Account name
        txid (str): Transaction identifier

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "txid": 'txid'
    }

    _optionals = [
        'id',
        'txid',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 txid=APIHelper.SKIP):
        """Constructor for the ManagedAccAddedList class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if txid is not APIHelper.SKIP:
            self.txid = txid 

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
        txid = dictionary.get("txid") if dictionary.get("txid") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   txid)