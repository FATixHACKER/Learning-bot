import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from lessons import python_lesson


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalam-o-Alaikum! 👋🐍\n\n"
        "Main tumhara Python Teacher hoon.\n\n"
        "📚 Python lesson start karne ke liye:\n"
        "/lesson\n\n"
        "Hum Python basic se properly seekhenge. ❤️"
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(
        "ERROR:",
        exc_info=context.error
    )


async def startup(application: Application):
    # Purana webhook remove karo
    await application.bot.delete_webhook(drop_pending_updates=True)

    # Telegram se bot information check karo
    bot_info = await application.bot.get_me()

    logger.info(
        "BOT CONNECTED SUCCESSFULLY: @%s",
        bot_info.username
    )


def main():
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(startup)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("lesson", python_lesson)
    )

    app.add_error_handler(error_handler)

    logger.info("STARTING PYTHON TEACHER BOT...")

    app.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
