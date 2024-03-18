# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from verizon.api_helper import APIHelper
from verizon.configuration import Server
from verizon.http.api_response import ApiResponse
from verizon.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from verizon.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from verizon.models.request_response import RequestResponse
from verizon.exceptions.rest_error_response_exception import RestErrorResponseException


class DeviceProfileManagementController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(DeviceProfileManagementController, self).__init__(config)

    def activate_device_through_profile(self,
                                        body):
        """Does a POST request to /m2m/v1/devices/profile/actions/activate_enable.

        Uses the profile to bring the device under management.

        Args:
            body (ActivateDeviceProfileRequest): Device Profile Query

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/activate_enable')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('thingspace_oauth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', RestErrorResponseException)
        ).execute()

    def profile_to_activate_device(self,
                                   body):
        """Does a POST request to /m2m/v1/devices/profile/actions/activate.

        Uses the profile to activate the device.

        Args:
            body (ProfileRequest): Device Profile Query

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/activate')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('thingspace_oauth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', RestErrorResponseException)
        ).execute()

    def profile_to_deactivate_device(self,
                                     body):
        """Does a POST request to /m2m/v1/devices/profile/actions/deactivate.

        Uses the profile to deactivate the device.

        Args:
            body (DeactivateDeviceProfileRequest): Device Profile Query

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/deactivate')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('thingspace_oauth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', RestErrorResponseException)
        ).execute()

    def profile_to_set_fallback_attribute(self,
                                          body):
        """Does a POST request to /m2m/v1/devices/profile/actions/setfallbackattribute.

        Allows the profile to set the fallback attribute to the device.

        Args:
            body (SetFallbackAttributeRequest): Device Profile Query

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/setfallbackattribute')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('thingspace_oauth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', RestErrorResponseException)
        ).execute()
