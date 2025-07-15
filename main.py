
import os
import discord
import random

TOKEN = os.getenv("TOKEN")
CHANNEL_ID_ENV = os.getenv("CHANNEL_ID")

if not TOKEN or not CHANNEL_ID_ENV:
    raise ValueError("TOKEN or CHANNEL_ID environment variable is missing.")

CHANNEL_ID = int(CHANNEL_ID_ENV)

video_links = [
    "https://www.youtube.com/@bkarchive/featured",
    "https://www.youtube.com/@BasimKarbalaei",
    "https://www.youtube.com/channel/UCH1nJIlCPQ7QAIItVrpr7WA",
    "https://www.youtube.com/playlist?list=PLXzJdQFBKapkgwtIad7QPs8jk1OmCsbPX",
    "https://www.youtube.com/playlist?list=PLjtjRVhLz_nxyvsPA0_9VtV8isPA-uWdE"
]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot is running as {{client.user}}")

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and message.content.strip().lower() == "مقطع":
        video = random.choice(video_links)
        await message.channel.send(f"🎥 مقطع عشوائي:\n{{video}}")

client.run(TOKEN)
