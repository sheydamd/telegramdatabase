from telegram import Update, ForceReply
from telegram.ext importApplicationBuilder, CommmandHandler, ContextTypes,  MessageHandler, filters
import sqlite3
from datatime
import logging
import requests
conn=sqlite3.connect("databasetel.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id INTEGER,
               first_name TEXT,
               username TEXT,
               start_time)""")
conn.commit()


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
    )
    user_name= update.effective_user.full_name
    with open("username.txt", "a", encoding="utf-8-sig") as f1:
        f1.write(f"{user_name}\n")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text == "Help":
        await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text == "hi":
        await update.message.reply_text("hello")
 
    elif update.message.text == "bye":
        await update.message.reply_text("bye")
       
    else:
        await update.message.reply_text(update.message.text)



def main() -> None:
    application = Application.builder().token("your token").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()