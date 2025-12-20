from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
import sqlite3
from datetime import datetime
import logging

# اتصال به دیتابیس
conn = sqlite3.connect("databasetel.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    first_name TEXT,
    username TEXT,
    start_time TEXT
)
""")
conn.commit()

# تنظیم لاگ
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# دستور start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    user_id = user.id
    first_name = user.first_name
    username = user.username
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # بررسی وجود کاربر
    cursor.execute(
        "SELECT user_id FROM users WHERE user_id = ?",
        (user_id,)
    )
    result = cursor.fetchone()

    if result:
        # کاربر قبلاً ثبت شده
        await update.message.reply_text(
            f"سلام {first_name} 👋\nشما قبلاً ثبت شده‌اید."
        )
    else:
        # ثبت کاربر جدید
        cursor.execute("""
        INSERT INTO users (user_id, first_name, username, start_time)
        VALUES (?, ?, ?, ?)
        """, (user_id, first_name, username, start_time))
        conn.commit()

        await update.message.reply_text(
            f"سلام {first_name} 👋\nاطلاعات شما با موفقیت ذخیره شد."
        )
# دستور help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Help!")

# اکو
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "hi":
        await update.message.reply_text("hello")
    elif text == "bye":
        await update.message.reply_text("bye")
    else:
        await update.message.reply_text(update.message.text)

# اجرای برنامه
def main():
    application = ApplicationBuilder().token("7660968231:AAE_zU2W0XBquoyrO22VtADv2s987v16OrM").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == "__main__":
    main()