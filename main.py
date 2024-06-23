import logging
from dotenv import dotenv_values
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

config = dotenv_values(".env")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    #db sect
    print("upd",update)
    strPP = f"id:{update.effective_user.id}, name: {update.effective_user.first_name} {update.effective_user.last_name}, username:{update.effective_user.username} \n"
    file = open("db.txt", "a")
    file = open("db.txt", "r")
    db= file.read()
    new_str = db.split("\n")
    arr=[]
    for x in new_str:
        k =x.split(",")
        arr.append(k[0].replace("id:",""))
    msg = "sei stato registrato >:("
    if str(update.effective_user.id) in arr:
        msg="sei already registrato!"
    else:
        print("miaoo")
        file = open("db.txt", "a")
        file.write(strPP)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    


if __name__ == '__main__':
    application = ApplicationBuilder().token(config['BOT_TOKEN']).build()
    
    start_handler = CommandHandler('secs', start)
    application.add_handler(start_handler)
    
    application.run_polling()