        secruity = bot.find_element(By.NAME, "text")
        print(secruity)
        if secruity.text == "":
            secruity.send_keys(self.user_name)
            secruity.send_keys(Keys.RETURN)