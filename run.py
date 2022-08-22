from twitter import bot
email = ""
password = ""
username = ""
tag = "100Dayofcode"
twitt = bot(email, password, username)
# twitt.login_page()
twitt.hashTag(tag)
twitt.auto_like()
