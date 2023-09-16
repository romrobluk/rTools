import asyncio
import discord
from discord import Webhook
from discord_webhook import DiscordWebhook
import aiohttp
import os
import time
import random

def wdeleter():
    os.system('cls')
    webhookurl = str(input(f'Webhook Url: '))
    os.system(f"curl -X DELETE {webhookurl}")