
# pip install pyrogram


from pyrogram import Client, filters
from config import Config
import logging
import asyncio  # Import asyncio for adding delay

# Insert your bot token directly here
BOT_TOKEN = "your_bot_token_here"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot = Client(
    "my_bot",
    bot_token=Config.TELEGRAM_TOKEN
)

@bot.on_message(filters.group)
async def handle_message(client, message):
    try:
        logging.info(f"New message in chat {message.chat.id}")

        # Add a 10-second delay before deleting the message
        await asyncio.sleep(10)
        
        # Delete the incoming message after the delay
        await bot.delete_messages(message.chat.id, message.id)
        logging.info(f"Deleted message {message.id} from chat {message.chat.id}")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    bot.run()
