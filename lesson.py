from telegram import Update
from telegram.ext import ContextTypes


async def python_lesson(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "🐍 Python Lesson 1\n\n"

        "📚 Topic: print()\n\n"

        "💡 print() kya hota hai?\n\n"

        "Python mein print() ka use "
        "screen par text, number ya value "
        "dikhane ke liye hota hai.\n\n"

        "🧠 Example:\n"
        'print("Hello World")\n\n'

        "Output:\n"
        "Hello World\n\n"

        "🔹 Example:\n"
        "print(5)\n\n"

        "Output:\n"
        "5\n\n"

        "📌 Yaad rakho:\n"
        "Text ko quotes ke andar likhte hain.\n\n"

        'Example: print("Python")\n\n'

        "✍️ Ab tumhari baari!\n\n"

        "Apne words mein batao:\n"
        "print() ka use kis liye hota hai?"
    )
