import instaloader

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()

# Loading a profile from an Instagram handle
handle_name = "leomessi"
profile = instaloader.Profile.from_username(bot.context, handle_name)
print("Username: ", profile.username)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
