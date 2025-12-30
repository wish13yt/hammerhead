import requests
print("Please note: This is designed for Sharkey, a fork of Misskey. Some functions may work with Misskey, but support is not provided for Misskey.")
print("please enter your Sharkey instance without a / at the end, starting with https://")
sharkeyint = input()
url = sharkeyint + '/api/notes/create'
print("great! The API URL I made for you is: " + url)
print("if this is incorrect, please try again")
print("enter an API token you obtained by logging into the bot account and going to: " + sharkeyint + "/settings/connect")
bearer = input()
header = {'Authorization': 'Bearer ' + bearer}
print("what do you want to send? this will be visible publicily !!!")
sendthis = input()
null = None
payload = {"text": sendthis,"poll": null,"cw": null,"localOnly": False,"visibility": "public","reactionAcceptance": "nonSensitiveOnly"}
x = requests.post(url, headers=header, json=payload)
if x.status_code == 200:
    print("success with response: " + x.text)
else:
    print("ow there was error")
# MAKE THIS USE MODULE :soon: