# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class RetrievesAvailableFilesResponse(object):

    """Implementation of the 'RetrievesAvailableFilesResponse' model.

    TODO: type model description here.

    Attributes:
        file_name (str): ThingSpace-generated name of the file. You will use
            this name when listing or scheduling campaigns for the file.
        file_version (str): Version of the file.
        release_note (str): Software release note.
        make (str): The software-applicable device make.
        model (str): The software-applicable device model.
        local_target_path (str): Local target path on the device.
        distribution_type (str): Valid values
        device_platform_id (str): The platform (Android, iOS, etc.,) that the
            software can be applied to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_name": 'fileName',
        "file_version": 'fileVersion',
        "release_note": 'releaseNote',
        "make": 'make',
        "model": 'model',
        "local_target_path": 'localTargetPath',
        "distribution_type": 'distributionType',
        "device_platform_id": 'devicePlatformId'
    }

    _optionals = [
        'file_name',
        'file_version',
        'release_note',
        'make',
        'model',
        'local_target_path',
        'distribution_type',
        'device_platform_id',
    ]

    def __init__(self,
                 file_name=APIHelper.SKIP,
                 file_version=APIHelper.SKIP,
                 release_note=APIHelper.SKIP,
                 make=APIHelper.SKIP,
                 model=APIHelper.SKIP,
                 local_target_path=APIHelper.SKIP,
                 distribution_type=APIHelper.SKIP,
                 device_platform_id=APIHelper.SKIP):
        """Constructor for the RetrievesAvailableFilesResponse class"""

        # Initialize members of the class
        if file_name is not APIHelper.SKIP:
            self.file_name = file_name 
        if file_version is not APIHelper.SKIP:
            self.file_version = file_version 
        if release_note is not APIHelper.SKIP:
            self.release_note = release_note 
        if make is not APIHelper.SKIP:
            self.make = make 
        if model is not APIHelper.SKIP:
            self.model = model 
        if local_target_path is not APIHelper.SKIP:
            self.local_target_path = local_target_path 
        if distribution_type is not APIHelper.SKIP:
            self.distribution_type = distribution_type 
        if device_platform_id is not APIHelper.SKIP:
            self.device_platform_id = device_platform_id 

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
        file_name = dictionary.get("fileName") if dictionary.get("fileName") else APIHelper.SKIP
        file_version = dictionary.get("fileVersion") if dictionary.get("fileVersion") else APIHelper.SKIP
        release_note = dictionary.get("releaseNote") if dictionary.get("releaseNote") else APIHelper.SKIP
        make = dictionary.get("make") if dictionary.get("make") else APIHelper.SKIP
        model = dictionary.get("model") if dictionary.get("model") else APIHelper.SKIP
        local_target_path = dictionary.get("localTargetPath") if dictionary.get("localTargetPath") else APIHelper.SKIP
        distribution_type = dictionary.get("distributionType") if dictionary.get("distributionType") else APIHelper.SKIP
        device_platform_id = dictionary.get("devicePlatformId") if dictionary.get("devicePlatformId") else APIHelper.SKIP
        # Return an object of this model
        return cls(file_name,
                   file_version,
                   release_note,
                   make,
                   model,
                   local_target_path,
                   distribution_type,
                   device_platform_id)
