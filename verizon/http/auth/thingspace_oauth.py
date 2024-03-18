# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth
from verizon.api_helper import APIHelper
from verizon.models.oauth_token import OauthToken
from apimatic_core.utilities.auth_helper import AuthHelper
from verizon.controllers.oauth_authorization_controller import\
    OauthAuthorizationController


class ThingspaceOauth(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in ThingspaceOauth

        """
        return "ThingspaceOauth: OAuthToken is undefined or expired."

    def __init__(self, thingspace_oauth_credentials, config):
        auth_params = {}
        self._oauth_client_id = thingspace_oauth_credentials.oauth_client_id \
            if thingspace_oauth_credentials is not None else None
        self._oauth_client_secret = thingspace_oauth_credentials.oauth_client_secret \
            if thingspace_oauth_credentials is not None else None
        if thingspace_oauth_credentials is not None \
                and isinstance(thingspace_oauth_credentials.oauth_token, OauthToken):
            self._oauth_token = OauthToken.from_dictionary(
                APIHelper.to_dictionary(thingspace_oauth_credentials.oauth_token))
        else:
            self._oauth_token = thingspace_oauth_credentials.oauth_token \
                if thingspace_oauth_credentials is not None else None
        self._o_auth_api = OauthAuthorizationController(config)
        if isinstance(self._oauth_token, OauthToken) and hasattr(self._oauth_token, 'access_token'):
            auth_params["Authorization"] = "Bearer {}".format(self._oauth_token.access_token)
        super().__init__(auth_params=auth_params)

    def is_valid(self):
        return self._oauth_token and not self.is_token_expired()

    def build_basic_auth_header(self):
        """ Builds the basic auth header for endpoints in the
            OAuth Authorization Controller.

        Returns:
            str: The value of the Authentication header.

        """
        return "Basic {}".format(AuthHelper.get_base64_encoded_value(
            self._oauth_client_id, self._oauth_client_secret))

    def fetch_token(self, additional_params=None):
        """ Authorizes the client.

            
            additional_params (dict):  Any additional form parameters.

        Returns:
            OAuthToken: The OAuth token.

        """
        token = self._o_auth_api.request_token_thingspace_oauth(
            self.build_basic_auth_header(),
            _optional_form_parameters=additional_params
        ).body
        if hasattr(token, 'expires_in'):
            current_utc_timestamp = AuthHelper.get_current_utc_timestamp()
            token.expiry = AuthHelper.get_token_expiry(current_utc_timestamp, token.expires_in)
        return token

    def is_token_expired(self):
        """ Checks if OAuth token has expired.

        Returns:
            bool: True if OAuth token has expired, False otherwise.

        """
        return hasattr(self._o_auth_token, 'expiry') and AuthHelper.is_token_expired(
            self._o_auth_token.expiry)


class ThingspaceOauthCredentials:

    @property
    def oauth_client_id(self):
        return self._oauth_client_id

    @property
    def oauth_client_secret(self):
        return self._oauth_client_secret

    @property
    def oauth_token(self):
        return self._oauth_token

    def __init__(self, oauth_client_id, oauth_client_secret, oauth_token=None):
        if oauth_client_id is None:
            raise ValueError('oauth_client_id cannot be None')
        self._oauth_client_id = oauth_client_id
        if oauth_client_secret is None:
            raise ValueError('oauth_client_secret cannot be None')
        self._oauth_client_secret = oauth_client_secret
        self._oauth_token = oauth_token

    def clone_with(self, oauth_client_id=None, oauth_client_secret=None,
                   oauth_token=None):
        return ThingspaceOauthCredentials(
            oauth_client_id or self.oauth_client_id,
            oauth_client_secret or self.oauth_client_secret,
            oauth_token or self.oauth_token)
