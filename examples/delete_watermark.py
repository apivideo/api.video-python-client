# Delete a watermark using its ID
import apivideo
from apivideo.apis import WaterkmarksApi
from apivideo.exceptions import ApiAuthException

api_key = "your api key here"
watermark = "your watermark ID here"

client = apivideo.AuthenticatedApiClient(api_key)

# If you'd rather use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

watermarks_api = WatermarksApi(client)

# Delete the watermark
response = watermarks_api.delete(watermark)
print(response)
