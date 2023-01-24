import os
import ctypes
import requests
import random
import string
import time
import sys
from pystyle import Center,Colors,Colorate
import getpass
import webbrowser
from pystyle import System
from ctypes import windll


def clear():
	print("\n" * 100)

clear()

os.system("title iWishkem - BarzoGen ┇ Made by https://youtube.com/c/iwishkem")

print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter("""
   /$$ /$$      /$$ /$$           /$$       /$$                              
  |__/| $$  /$ | $$|__/          | $$      | $$                              
   /$$| $$ /$$$| $$ /$$  /$$$$$$$| $$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$/$$$$ 
  | $$| $$/$$ $$ $$| $$ /$$_____/| $$__  $$| $$  /$$/ /$$__  $$| $$_  $$_  $$
  | $$| $$$$_  $$$$| $$|  $$$$$$ | $$  \ $$| $$$$$$/ | $$$$$$$$| $$ \ $$ \ $$
  | $$| $$$/ \  $$$| $$ \____  $$| $$  | $$| $$_  $$ | $$_____/| $$ | $$ | $$
  | $$| $$/   \  $$| $$ /$$$$$$$/| $$  | $$| $$ \  $$|  $$$$$$$| $$ | $$ | $$
  |__/|__/     \__/|__/|_______/ |__/  |__/|__/  \__/ \_______/|__/ |__/ |__/
                                                                           
                                                                           
                                                                           

   
                      ⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
                      ┇      [Discord] Soon                                ┇
                      ┇      [Github]  https://github.com/iwishkem         ┇
                      ┇      [Youtube] https://youtube.com/c/iwishkem      ┇
                      ┇           Never Forget Codes Are Random            ┇
                      ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
                      """)))

ans=True
while ans:
    print(Colorate.Vertical(Colors.blue_to_white, Center.XCenter("""
      1- Discord Nitro                          2- Xbox Gamepass
      3- Picsart Gold                           4- Crunchyroll Mega Fan
      5- Roblox Cookie                          6- Spotify Account
      7- Exit""")))
    ans=input("choice a number - ")
    if ans=="1":
      import Generator.nitro
    elif ans=="2":
      import Generator.xbox
    elif ans=="3":
      import Generator.picsart
    elif ans=="4":
      import Generator.crunchyroll
    elif ans=="5":
      import Generator.robloxcookie
    elif ans=="6":
      import Generator.spotify
    elif ans=="7":
      ans = None
    else:
       print("\n Not Valid Choice Try again")


#ans = None
