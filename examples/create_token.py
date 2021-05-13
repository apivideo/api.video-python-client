# Create a token for use with delegate uploads
import apivideo
from apivideo.apis import UploadTokensApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# List the time to live (ttl) in seconds for the token you create.
token_creation_payload = {"ttl": 1000}

tokens_api = UploadTokensApi(client)

# Create the token
response = tokens_api.create_token(token_creation_payload)
print(response)
