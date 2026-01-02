from hammerhead import SignIn, CreatePost

session = SignIn(
    key="key",
    url="https://sharkey.nomaakip.xyz"
)
poster = CreatePost(session)
test = poster.create("test")
print(test)
