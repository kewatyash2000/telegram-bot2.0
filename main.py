import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("7021370884:AAFSZzau0P0UxD0mk5vKhznodSGR-6HFKK4")  # Token will come from Railway variables

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ Join Group", url="@AmazonFlipkartLootAlerts_bot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome!\n\n💸 Earn ₹50 by completing simple steps:\n"
        "1️⃣ Join our Telegram Group\n"
        "2️⃣ Share your referral link\n"
        "3️⃣ Follow our WhatsApp Channel\n"
        "4️⃣ Get ₹50 via UPI!",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
