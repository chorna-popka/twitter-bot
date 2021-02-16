from istb import InternetSpeedBot

bot = InternetSpeedBot()
speed = bot.get_speed()

if bot.up > speed[0] or bot.down > speed[1]:
    bot.create_tweet(
        f"Upload speed is {speed[0]}Mbit/s when {bot.up} promised, "
        f"download speed is {speed[1]}Mbit/s when {bot.down} promised"
    )
