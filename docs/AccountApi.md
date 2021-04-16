# apivideo.AccountApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](AccountApi.md#get) | **GET** /account | Show account


# **get**
> Account get()

Show account

Deprecated. Authenticate and get a token, then you can use the bearer token here to retrieve details about your account.

### Example

```python
import apivideo
from apivideo.api import account_api
from apivideo.model.not_found import NotFound
from apivideo.model.account import Account
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Show account
        api_response = api_instance.get()
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AccountApi->get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

