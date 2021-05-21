# List all webhooks
import apivideo
from apivideo.apis import WebhooksApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

webhooks_api = WebhooksApi(client)

# Create a webhook
response = webhooks_api.list()
print(response)