from twitter import bot
email = "email"
password = "***"
username = "user-name"
tag = "100Dayofcode"
twitt = bot(email, password, username)
twitt.login_page()
twitt.hashTag(tag)
