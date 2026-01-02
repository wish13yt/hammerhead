import requests
class SignIn:
    def __init__(self, key, url):
        self.apiurl = url.rstrip("/")
        self.apikey = key
class CreatePost:
    def __init__(self, Session: SignIn):
            self.apiurl = Session.apiurl
            self.apikey = Session.apikey

    def create(self, post_content):
        posturl = self.apiurl + "/api/notes/create"
        headers = {
              "Authorization" : f"Bearer {self.apikey}"
         }

        payload = {
            "text": post_content,
            "poll": None,
            "cw": None,
            "localOnly": False,
            "visibility": "public",
            "reactionAcceptance": "nonSensitiveOnly"
        }
        request = requests.post(posturl, headers=headers, json=payload)
        return request.status_code
    
"""
ok so now that i fixed it wish this is how you use it since you're dumb hahaha

from hammerhead import SignIn, CreatePost

session = SignIn(
    key="key",
    url="https://sharkey.nomaakip.xyz"
)
poster = CreatePost(session)
test = poster.create("test")
print(test)
"""
