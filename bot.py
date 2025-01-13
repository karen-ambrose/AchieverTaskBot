from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, ContextTypes, MessageHandler, filters

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I'm your Daily Task Manager Bot. 🚀")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm here to help you manage your daily tasks. 📝\n\nHere are the commands you can use:\n"
        "/start - Welcome message\n"
        "/help - List of commands\n"
        "/new - Add a new task\n"
        "/viewtasks - View all tasks\n"
        "/completed - Mark a task as completed\n"
        "/deletetask - Delete a task\n"
        "/reminder - Set a task reminder\n"
        "/clear - Clear all tasks\n")

async def new_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What is the task you want to add?")

async def view_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Here is the list of tasks you have for today!")

async def complete_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Please input the ID of the task completed.")

async def delete_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Please input the ID of the task you want to delete.")

async def reminder_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Please input the ID of the task you want a reminder for.")

async def clear_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Your tasks have been cleared!")

def handle_responses(text: str) -> str:
    processed: str = text.lower()
    if processed == 'hi' or processed == 'hello' or processed == 'hey':
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

    print('Bot:', response)

def main() -> None:
    # Replace 'YOUR_TOKEN' with the token you received from BotFather
    TOKEN = "7979508359:AAEaU9ygvbrkvvZtL4FsWKxkj-2iq9RDD-o"
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("new", new_command))
    app.add_handler(CommandHandler("viewtasks", view_command))
    app.add_handler(CommandHandler("completed", complete_command))
    app.add_handler(CommandHandler("deletetask", delete_command))
    app.add_handler(CommandHandler("reminder", reminder_command))
    app.add_handler(CommandHandler("clear", clear_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
