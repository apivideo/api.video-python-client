# Webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** | A unique identifier of the webhook you subscribed to. | [optional] 
**created_at** | **datetime** | The time and date when you created this webhook subscription, in ATOM UTC format. | [optional] 
**events** | **[str]** | A list of events that you subscribed to. When these events occur, the API triggers a webhook call to the URL you provided. | [optional] 
**url** | **str** | The URL where the API sends the webhook. | [optional] 
**signature_secret** | **str** | A secret key for the webhook you subscribed to. You can use it to verify the origin of the webhook call that you receive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


