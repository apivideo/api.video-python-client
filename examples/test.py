import requests

url = "https://ws.api.video/auth/api-key"

payload = {"apiKey": "hmDbI6i3va9Xi98DuuoylkGhejg146TNK86FE6M8RxJ"}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
token = response.get("access_token")
print(token)
url = "https://ws.api.video/players"

payload = {
    "enableApi": True,
    "enableControls": True,
    "forceAutoplay": False,
    "hideTitle": False,
    "forceLoop": False,
    "text": "rgba(255, 255, 255, .95)",
    "link": "rgba(255, 0, 0, .95)",
    "linkHover": "rgba(255, 255, 255, .75)",
    "trackPlayed": "rgba(255, 255, 255, .95)",
    "trackUnplayed": "rgba(255, 255, 255, .1)",
    "trackBackground": "rgba(0, 0, 0, 0)",
    "backgroundTop": "rgba(72, 4, 45, 1)",
    "backgroundText": "rgba(255, 255, 255, .95)"
}
headers1 = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": token
}

response = requests.request("POST", url, json=payload, headers=headers1)

print(response.text)