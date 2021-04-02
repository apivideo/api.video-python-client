# AccessToken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token containing security credentials allowing you to acccess the API. The token lasts for one hour. | [optional] 
**token_type** | **str** | The type of token you have. | [optional]  if omitted the server will use the default value of "bearer"
**refresh_token** | **str** | A token you can use to get the next access token when your current access token expires. | [optional] 
**expires_in** | **int** | Lists the time in seconds when your access token expires. It lasts for one hour. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


