# OAuth Authorization

```python
oauth_authorization_controller = client.oauth_authorization
```

## Class Name

`OauthAuthorizationController`

## Methods

* [Request Token OAuth 2](../../doc/controllers/oauth-authorization.md#request-token-oauth-2)
* [Request Token Thingspace Oauth](../../doc/controllers/oauth-authorization.md#request-token-thingspace-oauth)


# Request Token OAuth 2

Create a new OAuth 2 token.

:information_source: **Note** This endpoint does not require authentication.

```python
def request_token_oauth_2(self,
                         authorization,
                         scope=None,
                         _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Authorization header in Basic auth format |
| `scope` | `str` | Form, Optional | Requested scopes as a space-delimited list. |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`OauthToken`](../../doc/models/oauth-token.md).

## Example Usage

```python
authorization = 'Authorization8'

_optional_form_parameters = {
    'key0': 'additionalFieldParams9'
}

result = oauth_authorization_controller.request_token_oauth_2(
    authorization,
    _optional_form_parameters=_optional_form_parameters
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | OAuth 2 provider returned an error. | [`OauthProviderException`](../../doc/models/oauth-provider-exception.md) |
| 401 | OAuth 2 provider says client authentication failed. | [`OauthProviderException`](../../doc/models/oauth-provider-exception.md) |


# Request Token Thingspace Oauth

Create a new OAuth 2 token.

:information_source: **Note** This endpoint does not require authentication.

```python
def request_token_thingspace_oauth(self,
                                  authorization,
                                  scope=None,
                                  _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Authorization header in Basic auth format |
| `scope` | `str` | Form, Optional | Requested scopes as a space-delimited list. |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`OauthToken`](../../doc/models/oauth-token.md).

## Example Usage

```python
authorization = 'Authorization8'

_optional_form_parameters = {
    'key0': 'additionalFieldParams9'
}

result = oauth_authorization_controller.request_token_thingspace_oauth(
    authorization,
    _optional_form_parameters=_optional_form_parameters
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | OAuth 2 provider returned an error. | [`OauthProviderException`](../../doc/models/oauth-provider-exception.md) |
| 401 | OAuth 2 provider says client authentication failed. | [`OauthProviderException`](../../doc/models/oauth-provider-exception.md) |

