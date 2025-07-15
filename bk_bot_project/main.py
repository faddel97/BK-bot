import os
import discord
import random

# سحب التوكن ومعرّف القناة من المتغيرات البيئية
TOKEN = os.getenv("TOKEN")
CHANNEL_ID_STR = os.getenv("CHANNEL_ID")

# تحقق من أن المتغيرات موجودة
if not TOKEN or not CHANNEL_ID_STR:
    raise ValueError("❌ تأكد من أنك أضفت TOKEN و CHANNEL_ID في المتغيرات البيئية.")

CHANNEL_ID = int(CHANNEL_ID_STR)

# قائمة روابط الفيديوهات
video_links = [
    "https://www.youtube.com/@bkarchive/featured",
    "https://www.youtube.com/@BasimKarbalaei",
    "https://www.youtube.com/channel/UCH1nJIlCPQ7QAIItVrpr7WA",
    "https://www.youtube.com/playlist?list=PLXzJdQFBKapkgwtIad7QPs8jk1OmCsbPX",
    "https://www.youtube.com/playlist?list=PLjtjRVhLz_nxyvsPA0_9VtV8isPA-uWdE"
]

# إعدادات البوت
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot is running as {client.user}")

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and message.content.strip().lower() == "مقطع":
        video = random.choice(video_links)
        await message.channel.send(f"🎥 مقطع عشوائي:\n{video}")

# تشغيل البوت
client.run(TOKEN)
