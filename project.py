from instabot import bot as bot

# Create a new bot instance
x=str("enter ur username");
y=str("enter ur password")



# Login to your Instagram account
bot.login(username="", password="your_password")

# Like a specific post
bot.like(media_id="media_id_of_the_post")

# Comment on a specific post
bot.comment(media_id="media_id_of_the_post", comment_text="Your comment text")

# Follow a specific user
bot.follow(user_id="user_id_of_the_user")

# Unfollow a specific user
bot.unfollow(user_id="user_id_of_the_user")

# Logout of your Instagram account
bot.logout()

