from telethon import TelegramClient
import sys
sys.path.append('data')
from config import api_id, api_hash


client = TelegramClient('anon', api_id, api_hash)


async def main():
    await client.send_message('+79633477417', 'Hello, friend!')


with client:
    client.loop.run_until_complete(main())