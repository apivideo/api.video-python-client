# Create a webhook 
import apivideo
from apivideo.apis import WebhooksApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

webhooks_api = WebhooksApi(client)

# Create the webhooks payload
webhooks_creation_payload = {
    "events": ["video.encoding.quality.completed"],
    "url": "https://example.com/webhooks"
}

# Create a webhook
response = webhooks_api.create(webhooks_creation_payload)
print(response)