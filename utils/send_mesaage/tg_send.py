from telethon import TelegramClient
from data import config


client = TelegramClient('anon', config.api_id, config.api_hash)


async def main():
    await client.send_message('+79817382780', 'Hello, friend!')


with client:
    client.loop.run_until_complete(main())