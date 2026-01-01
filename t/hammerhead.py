import requests
class signin:
    def __init__(self, key, url):
        global apiurl
        global apikey
        apiurl = url
        apikey = key
        if not apiurl.startswith("https://"):
            apiurl = "https://" + url
        print(apiurl + " " + apikey)
class createpost:
    def __init__(self, post_content):
            print(signin.apiurl)
            apiurl = signin.apiurl
            apikey = signin.apikey
            if apiurl.endswith("/"):
                posturl = apiurl + "api/notes/create"
            else:
                posturl = apiurl + "/api/notes/create"
            null = None
            header = {'Authorization': 'Bearer ' + apikey}
            payload = {"text": post_content,"poll": null,"cw": null,"localOnly": False,"visibility": "public","reactionAcceptance": "nonSensitiveOnly"}
            rep = requests.post(posturl, headers=header, json=payload)
            return rep.status_code