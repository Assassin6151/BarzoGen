print("\n" * 100) #clears console
import os
import ctypes
import requests
import random
import string
import time
from pystyle import Center,Colors,Colorate

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
                      ┇      [Discord] https://discord.gg/qykGpz9XeC       ┇
                      ┇      [Github]  https://github.com/iwishkem         ┇
                      ┇      [Youtube] https://youtube.com/c/iwishkem      ┇
                      ┇           Never Forget Codes Are Random            ┇
                      ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
                      """)))
time.sleep(0.1)
time.sleep(0.1)

num = int(input('how much Crunchyroll Mega Fan code?'))

with open("Crunchyroll.txt", "w", encoding='utf-8') as file:
    print(
        "ur codes r created in Crunchyroll.txt!"
    )

    start = time.time()

    for i in range(num):
        code = "".join(
            random.choices(string.ascii_uppercase + string.digits,
                           k=16))

        file.write(f"{code}\n")

    print(f"{num} codes created, tooked time: {time.time() - start}\n")

with open("Crunchyroll.txt") as file:
    for line in file.readlines():
        croll = line.strip("\n")

        url = "https://www.crunchyroll.com/campaign-discord?coupon_code=" + croll + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"work | {croll}")
            break
        else:
            print(f"nope | {croll}")



input("\n Good Luck! ")
