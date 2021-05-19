# Retrieve details about a webhook using its ID
import apivideo
from apivideo.apis import WebhooksApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)
webhook_id = "your webhook ID here"

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Set up to use webhooks
webhooks_api = WebhooksApi(client)

# Create a webhook
response = webhooks_api.get(webhook_id)
print(response)