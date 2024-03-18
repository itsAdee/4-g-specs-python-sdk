# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.esi_msubrequest import ESIMsubrequest


class ESIMStatusResponse(object):

    """Implementation of the 'eSIMStatusResponse' model.

    TODO: type model description here.

    Attributes:
        request_id (str): TODO: type description here.
        status (str): TODO: type description here.
        subrequests (List[ESIMsubrequest]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'requestId',
        "status": 'status',
        "subrequests": 'subrequests'
    }

    _optionals = [
        'request_id',
        'status',
        'subrequests',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 subrequests=APIHelper.SKIP):
        """Constructor for the ESIMStatusResponse class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if subrequests is not APIHelper.SKIP:
            self.subrequests = subrequests 

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
        request_id = dictionary.get("requestId") if dictionary.get("requestId") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        subrequests = None
        if dictionary.get('subrequests') is not None:
            subrequests = [ESIMsubrequest.from_dictionary(x) for x in dictionary.get('subrequests')]
        else:
            subrequests = APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   status,
                   subrequests)
