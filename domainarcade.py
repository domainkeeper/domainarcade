from telegram import *
from telegram.ext import *
from telegram.constants import *
from basic import start,help


app = ApplicationBuilder().token('8376711623:AAGl7Hj39AV-egDQPQlXnLN1qLsqLeKwyYI').build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.run_polling()

