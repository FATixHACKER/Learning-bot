import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from lessons import python_lesson


# Logging on
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "السلام علیکم ASAD! 👋🐍\n\n"
        "میں تمہارا Python Teacher ہوں۔\n\n"
        "📚 Lesson شروع کرنے کے لیے:\n"
        "/lesson\n\n"
        "ہم Python بالکل basic سے سیکھیں گے۔ ❤️"
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(
        "Update handle karte waqt error aaya:",
        exc_info=context.error,
    )


async def post_init(application: Application):
    # Agar purana webhook laga hua ho to remove kar do
    await application.bot.delete_webhook(drop_pending_updates=False)

    me = await application.bot.get_me()

    logger.info("Bot connected: @%s", me.username)


def main():

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lesson", python_lesson))

    # Errors
    app.add_error_handler(error_handler)

    logger.info("Python Teacher Bot starting...")

    app.run_polling()


if __name__ == "__main__":
    main()
