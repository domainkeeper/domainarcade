from telegram import *
from telegram.ext import *
from telegram.constants import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot. How can I assist you today?")
    return

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are the commands you can use:\n/start - Start the bot\n/help - Get help information")
    return
