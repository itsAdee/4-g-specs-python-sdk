# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class Region(object):

    """Implementation of the 'Region' model.

    Information representing a certain geographical or logical area where MEC
    resources and services are provided.

    Attributes:
        region_id (str): The unique identifier of the region.
        name (str): A relevant and identifiable region name.
        country_code (str): A two-character alpha code for a country, based on
            ISO 3166-1 alpha-2. This is future functionality, so the value
            returned is 'null'.
        metro (str): The metropolitan area or 'City' value.  This is future
            functionality, so the value returned is 'null'.
        area (str): This is a sub-set of 'City' and is similar to 'Zone'. This
            is future functionality, so the value returned is 'null'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "region_id": 'regionId',
        "name": 'name',
        "country_code": 'countryCode',
        "metro": 'metro',
        "area": 'area'
    }

    _optionals = [
        'region_id',
        'name',
        'country_code',
        'metro',
        'area',
    ]

    _nullables = [
        'region_id',
        'name',
        'country_code',
        'metro',
        'area',
    ]

    def __init__(self,
                 region_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 country_code=APIHelper.SKIP,
                 metro=APIHelper.SKIP,
                 area=APIHelper.SKIP):
        """Constructor for the Region class"""

        # Initialize members of the class
        if region_id is not APIHelper.SKIP:
            self.region_id = region_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if country_code is not APIHelper.SKIP:
            self.country_code = country_code 
        if metro is not APIHelper.SKIP:
            self.metro = metro 
        if area is not APIHelper.SKIP:
            self.area = area 

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
        region_id = dictionary.get("regionId") if "regionId" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        country_code = dictionary.get("countryCode") if "countryCode" in dictionary.keys() else APIHelper.SKIP
        metro = dictionary.get("metro") if "metro" in dictionary.keys() else APIHelper.SKIP
        area = dictionary.get("area") if "area" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(region_id,
                   name,
                   country_code,
                   metro,
                   area)
