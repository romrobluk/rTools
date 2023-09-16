import asyncio
import discord
from discord import Webhook
from discord_webhook import DiscordWebhook
import aiohttp
import os
import time

def wspammer():
    os.system('cls')
    webhookurl = input('Webhook Url: ')
    webhookdesc = input('Message: ')
    webhook_msg = input('Ammount of messages: ')
    webhook_msg = int(webhook_msg)
    i = 0
    i = int(i)
    for i in range(webhook_msg):
        webhook = DiscordWebhook(url=webhookurl, content=webhookdesc)
        response = webhook.execute()
    print("""
██████╗░░█████╗░███╗░░██╗███████╗██╗
██╔══██╗██╔══██╗████╗░██║██╔════╝██║
██║░░██║██║░░██║██╔██╗██║█████╗░░██║
██║░░██║██║░░██║██║╚████║██╔══╝░░╚═╝
██████╔╝╚█████╔╝██║░╚███║███████╗██╗
╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝""")