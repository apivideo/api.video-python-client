# Get information about a single token using the token ID
import apivideo
from apivideo.apis import UploadTokensApi
from apivideo.exceptions import ApiAuthException

# Set variables
api_key = "your api key here"
token = "your token ID here"

# Set up the client
client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Set up to use tokens
tokens_api = UploadTokensApi(client)

# Send your request to retrieve information about a specific token
response = tokens_api.get_token(token)
print(response)