import asyncio
import discord
from discord import Webhook
import aiohttp
from rutils import wspammer, wnitro, wdeleter
import os
import time
import random

def main():
        os.system('title "rTools | made by romrobluk#0 | https://github.com/romrobluk/rTools"')
        os.system('cls')
        print("""
              
###############################################
### This is a simple tool made by romrobluk ###
############ Discord: romrobluk#0 #############
##### https://github.com/romrobluk/rTools #####
###############################################
                                                

        [1] - Discord Webhook Spammer   

        [2] - Discord Webhook Nitro                                                                               

        [3] - Discord Webhook Deleter                                                                          
""")
        ans = input()
        ans = int(ans)
        if ans == 1:
                wspammer.wspammer()
                main()
        elif ans == 2:
                wnitro.wnitro()
                main()
        elif ans == 3:
                wdeleter.wdeleter()
                main()
        else:
                main()
main()