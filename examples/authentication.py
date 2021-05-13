# Use your api.video api key to retrieve an access token for use with the api.video
# API. Access tokens are good for one hour.

import apivideo

api_key = "your api key here"
client = apivideo.AuthenticatedApiClient(api_key)

# If you prefer to use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# You can view the object like this. Use this for reference and testing only.

print(client.__dict__)
