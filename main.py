from pyrogram import Client
from config import Config

app = Client(
    "FileStoreBot",
    api_id    = Config.API_ID,
    api_hash  = Config.API_HASH,
    bot_token = Config.BOT_TOKEN,
    plugins   = dict(root="plugins")
)

async def on_startup():
    from database import create_indexes
    await create_indexes()
    print("✅ MongoDB indexes ready.")

if __name__ == "__main__":
    import asyncio
    print("🤖 File Store Bot starting...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(on_startup())
    app.run()
    print("✅ Bot stopped.")
