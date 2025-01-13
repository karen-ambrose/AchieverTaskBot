from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters, ContextTypes

TOKENBOT_USER: Final = '7979508359:AAEaU9ygvbrkvvZtL4FsWKxkj-2iq9RDD-o'
BOT_NAME: Final = '@acheev_bot'

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your Daily Task Manager Bot. 🚀")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm here to help you manage your daily tasks. 📝\n\nDo you need further help on how to navigate me?")

async def new_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What is the task you want to add?")

#responses

def handle_responses(text: str) -> str:
    processed: str = text.lower()
    if processed == 'hi':
        return 'Hello! How can I help you today?'
    elif processed == 'bye':
        return 'Goodbye! Have a great day! 😊'
    else:
        return 'I am sorry, I do not understand that command. Please type /help for more information.'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message}: "{text}"')

    if message == 'private':
        response: str = handle_responses(text)
        await update.message.reply_text(response)

    if message == 'group':
        if text.startswith(BOT_NAME):
            new_text: str = text.replace(BOT_NAME, '').strip()
            response: str = handle_responses(new_text)
            await update.message.reply_text(response)
    
    print('Bot:', response)
    
    async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')

    if __name__ == "__main__":
        print("Bot is starting...")
        app = Application.builder().token(TOKENBOT_USER).build()

        #commands
        app.add_handler(CommandHandler("start", start_command))
        app.add_handler(CommandHandler("help", help_command))
        app.add_handler(CommandHandler("new", new_command))

        #responses
        app.add_handler(MessageHandler(filters.text, handle_message))

        #errors
        app.add_error_handler(error)    

        #polling
        print('Polling...')
        app.run_polling(poll_interval=3)


