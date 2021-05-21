# Delete a token using the token ID 
import apivideo
from apivideo.apis import UploadTokensApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
token = "token ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

tokens_api = UploadTokensApi(client)

response = tokens_api.delete_token(token)
print(response)