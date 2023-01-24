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

num = int(input('how much Picsart Gold codes?'))

with open("picsart.txt", "w", encoding='utf-8') as file:
    print(
        "ur codes r created in picsart.txt!"
    )

    start = time.time()

    for i in range(num):
        code = "".join(
            random.choices(string.ascii_uppercase + string.digits +
                           string.ascii_lowercase,
                           k=4))
                         
    
        code1 = "".join(
            random.choices(string.ascii_uppercase + string.digits +
                           string.ascii_lowercase,
                           k=4))
        code4 = "".join(
            random.choices(string.ascii_uppercase + string.digits +
                           string.ascii_lowercase,
                           k=4))
        code2 = "".join(
            random.choices(string.ascii_uppercase + string.digits +
                           string.ascii_lowercase,
                           k=4))
        code3 = "".join(
            random.choices(string.ascii_uppercase + string.digits +
                           string.ascii_lowercase,
                           k=1))

        file.write(f"dscrd-{code1}-{code2}-{code3}\n")
        
        print(f"{num} codes created, tooked time: {time.time() - start}\n")

with open("picsart.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"work | {nitro}")
            break
        else:
            print(f"nope | {nitro}")



input("\n good luck! ")
    
