# List all delegated tokens that are active
import apivideo
from apivideo.apis import UploadTokensApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Set up to use delegated tokens
tokens_api = UploadTokensApi(client)

# List all delegated tokens
response = tokens_api.list()
print(response)
