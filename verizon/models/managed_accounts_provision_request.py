# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ManagedAccountsProvisionRequest(object):

    """Implementation of the 'ManagedAccountsProvisionRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (str): Managed account identifier
        paccount_name (str): Primary Account identifier
        service_name (ServiceNameEnum): Service name
        mtype (str): SKU name
        txid (str): Transaction identifier returned by add request

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "paccount_name": 'paccountName',
        "service_name": 'serviceName',
        "mtype": 'type',
        "txid": 'txid'
    }

    def __init__(self,
                 account_name=None,
                 paccount_name=None,
                 service_name='Location',
                 mtype=None,
                 txid=None):
        """Constructor for the ManagedAccountsProvisionRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.paccount_name = paccount_name 
        self.service_name = service_name 
        self.mtype = mtype 
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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        paccount_name = dictionary.get("paccountName") if dictionary.get("paccountName") else None
        service_name = dictionary.get("serviceName") if dictionary.get("serviceName") else 'Location'
        mtype = dictionary.get("type") if dictionary.get("type") else None
        txid = dictionary.get("txid") if dictionary.get("txid") else None
        # Return an object of this model
        return cls(account_name,
                   paccount_name,
                   service_name,
                   mtype,
                   txid)
