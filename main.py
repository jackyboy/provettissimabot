import logging
from dotenv import dotenv_values
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

config = dotenv_values(".env")
def fix_string(db, comparableStr):
    new_str = db.split("\n")
    for x in new_str:
        k =x.split(",")
        print(k[0])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    #db sect
    str = f"id:{update.effective_user.id}, name: {update.effective_user.first_name} {update.effective_user.last_name}, username:{update.effective_user.username} \n"
    f = open("db.txt", "a")
    f.write(str)
    f = open("db.txt", "r")
    fix_string(f.read(), update.effective_user.id)
    #db ends
    await context.bot.send_message(chat_id=update.effective_chat.id, text="sei stato registrato >:(")

if __name__ == '__main__':
    application = ApplicationBuilder().token(config['BOT_TOKEN']).build()
    
    start_handler = CommandHandler('secs', start)
    application.add_handler(start_handler)
    
    application.run_polling()