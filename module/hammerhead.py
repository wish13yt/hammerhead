import requests
apikey = None
apiurl = None
def sign_in(key, url):
    apikey = key
    if apiurl.startswith("https://"):
        apiurl = url
    else:
        apiurl = "https://" + url
def create_post(post_content):
    if apiurl.endswith("/"):
        posturl = apiurl + "api/notes/create"
    else:
        posturl = apiurl + "/api/notes/create"
    null = None
    header = {'Authorization': 'Bearer ' + apikey}
    payload = {"text": post_content,"poll": null,"cw": null,"localOnly": False,"visibility": "public","reactionAcceptance": "nonSensitiveOnly"}
    x = requests.post(posturl, headers=header, json=payload)
    return x.status_code