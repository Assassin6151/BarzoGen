print("\n" * 100) #clears console
import requests
import re
import string
import os
from pystyle import Center,Colors,Colorate
from pystyle import System
import threading
import random
import time
from queue import Queue

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

outputfile = open("cookies.txt", "a")

x = 0
cookies = []
intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
n = 0
print('[RECOMMENDED: Pick a high amount for better odds of generating a valid cookie]')
c = int(input("How many cookies do you want to generate? \n"))
print('Generating random cookies... please be patient! \n')
letters = 'ABCDEF'

while x < c:


    cookies =  intro +  ''.join(random.choices(letters + string.digits, k=732))

    x = x + 1
    
    f = open('Cookies.txt', "a+")
    f.write(f'{cookies}\n')
    f.close()
    

if __name__ == '__main__':

    number_of_threads = 900
    print_lock = threading.Lock()
    cookie_queue = Queue()
    url = 'https://accountinformation.roblox.com/v1/birthdate'

        
    cookie_queue.join()

outputfile.close()

t1 = time.time()
print('Done! IF any valid cookies were found, they have been added to the hits.txt file!')
input("Press enter to exit.")
