from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to NitinTubeBot\n\n"
        "🎬 YouTube & Instagram Video Downloader\n\n"
        "बस वीडियो का link भेजो\n"
        "या वेबसाइट खोलो 👇\n\n"
        "🌐 https://thenitin54.github.io/youtube-downloader/\n\n"
        "✅ Fast • Free • No Login\n\n"
        "⚠️ Public content only"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "youtube.com" in text or "youtu.be" in text or "instagram.com" in text:
        await update.message.reply_text(
            "⬇️ Download करने के लिए वेबसाइट खोलो:\n"
            "https://thenitin54.github.io/youtube-downloader/"
        )
    else:
        await update.message.reply_text(
            "❌ Please valid YouTube / Instagram link भेजो"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

app.run_polling()
