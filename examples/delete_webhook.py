# Delete a webhook
import apivideo
from apivideo.apis import WebhooksApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)
webhook_id = "webhook ID here"

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

webhooks_api = WebhooksApi(client)

# Create a webhook
response = webhooks_api.delete(webhook_id)
print(response)