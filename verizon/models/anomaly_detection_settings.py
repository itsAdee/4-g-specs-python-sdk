# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.sensitivity_parameters import SensitivityParameters


class AnomalyDetectionSettings(object):

    """Implementation of the 'AnomalyDetectionSettings' model.

    Settings for anomaly detection.

    Attributes:
        account_name (str): Indicates if the account name used has anomaly
            detection.<br />Success - The account has anomaly detection.<br
            />Failure - The account does not have anomaly detection.
        sensitivity_parameter (SensitivityParameters): Details for sensitivity
            parameters.
        status (str): Indicates if anomaly detection is active on the
            account<br />Active - Anomaly detection is active<br />Disabled-
            Anomaly detection is not active.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "sensitivity_parameter": 'sensitivityParameter',
        "status": 'status'
    }

    _optionals = [
        'account_name',
        'sensitivity_parameter',
        'status',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 sensitivity_parameter=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the AnomalyDetectionSettings class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if sensitivity_parameter is not APIHelper.SKIP:
            self.sensitivity_parameter = sensitivity_parameter 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        sensitivity_parameter = SensitivityParameters.from_dictionary(dictionary.get('sensitivityParameter')) if 'sensitivityParameter' in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   sensitivity_parameter,
                   status)
