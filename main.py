from telegram import Update, Chat, ChatMember, ChatMemberUpdated
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ChatMemberHandler, filters, MessageHandler
from dotenv import dotenv_values
import logging

config = dotenv_values(".env")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    await update.message.reply_text(f'Hello {update}')

async def get_members(chatMebersUpdate: ChatMemberUpdated, context: ContextTypes.DEFAULT_TYPE) -> None:
    #members = context.bot.getFullChat(chatMebersUpdate.effective_chat.id)
    members = await context.bot.get_chat_member_count(chatMebersUpdate.effective_chat.id)
    #members = await context.bot.get_chat_member(chatMebersUpdate.effective_chat.id, chatMebersUpdate.effective_user.id)
    print(members)
    await chatMebersUpdate.message.reply_text(f'Siete in {members}')
    #await update.getFullChat(update.effective_chat.id)

if __name__ == '__main__':
    application = ApplicationBuilder().token(config["BOT_TOKEN"]).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    hello_handler = CommandHandler('hello', hello)
    application.add_handler(hello_handler)

    get_members_handler = CommandHandler('get_members', get_members)
    application.add_handler(get_members_handler)

    application.run_polling()