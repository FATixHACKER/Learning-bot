from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN
from lessons import python_lesson


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "السلام علیکم! 👋\n\n"
        "میں آپ کا Python Teacher ہوں۔ 🐍\n"
        "Python سیکھنے کے لیے /lesson لکھیں۔"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lesson", python_lesson))

    print("Python Teacher Bot چل رہا ہے...")

    app.run_polling()


if __name__ == "__main__":
    main()