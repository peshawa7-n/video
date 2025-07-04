from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from tqdm import tqdm
import os


TELEGRAMAPI_ID = os.getenv("APITELEGRAM_ID")
TELEGRAMAPI_HASH = os.getenv("APITELEGRAM_HASH")
TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
with TelegramClient('name', TELEGRAMAPI_ID, TELEGRAMAPI_HASH) as client:
    # Connect to Telegram (if not already connected)
    # client.connect() test75.py allcodes for sending* HAZIR <=

    result = client(
        GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer="username", # Corrected: InputPeerEmpty needs to be instantiated
            limit=500,                    # Corrected: 'linit' should be 'limit'
            hash=0
        )
    )

    tittle = "chiyrokiy shewek چیرۆکی شەوێک"
    idpostchennal = 2384585674
    channelmy = client(GetFullChannelRequest(idpostchennal))
    # print(channelmy.full_chat)

    messages = client.get_messages(channelmy.full_chat, limit=2000)
    number_message = 662
    number = 0

    for message in tqdm(messages):
        # message.download_media('./' + tittle + f'/{number_message}')
        message.download_media('./' + tittle + f'/')
        number_message += 1
        if number == 15:

            break
