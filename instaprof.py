import instaloader
import pyfiglet
# bannenr
ban = pyfiglet.figlet_format("instaprof")
print(ban)
print("--------------------------------")
print(" By Mobin.Zed from Artakava")
print(" Usage : Just Enter the username")
print("---------------------------------\n")
mod = instaloader.Instaloader()
user = input('Enter the user name -->  ')
mod.download_profile(user,profile_pic_only=True)