from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 APNA TOKEN DAAL
import os
TOKEN = os.getenv("TOKEN")

# 🌐 TERA MINES SITE LINK
MINES_LINK = "https://sensational-gnome-c56763.netlify.app"

# 📦 VERIFIED USERS
verified_users = set()

# 🚀 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Welcome to AI Mines VIP\n\n"
        "🚀 START EARNING NOW\n\n"
        "💎 BIG UPDATE:\n"
        "• Advanced prediction system\n"
        "• New algorithms\n"
        "• Bug fixes\n"
        "• Win rate ≈ 90%+\n\n"
        "👉 Send your 1Win ID to verify access"
    )

# ✅ VERIFY (ONLY NUMBER)
async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # ❌ ignore non-number
    if not user_text.isdigit():
        return

    user_id = update.effective_user.id

    # ❌ already verified
    if user_id in verified_users:
        return

    verified_users.add(user_id)

    keyboard = [["⭐ Mines"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "✅ Verified Successfully!\n\n🎮 Choose Game:",
        reply_markup=reply_markup
    )

# 💣 MINES (MINI APP OPEN)
async def mines(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # ❌ not verified
    if user_id not in verified_users:
        await update.message.reply_text(
            "❌ Not Verified\n\n"
            "👉 Register & Deposit first"
        )
        return

    keyboard = [
        [InlineKeyboardButton(
            "🚀 OPEN MINES PREDICTOR",
            web_app=WebAppInfo(url=MINES_LINK)
        )]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "💣 Mines Predictor Activated\n\n"
        "⚡ Use signals every 2-3 minutes\n\n"
        "👇 Click below:",
        reply_markup=reply_markup
    )

# 🤖 MAIN
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

# VERIFY ONLY NUMBER
app.add_handler(MessageHandler(filters.Regex(r'^\d+$'), verify))

# MINES BUTTON
app.add_handler(MessageHandler(filters.Regex("⭐ Mines"), mines))

print("🤖 Bot Running...")
app.run_polling()