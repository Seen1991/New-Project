import logging
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Create an Updater object
updater = Updater(token='6030321994:AAEXahowm2jcwTTO8b-5jS4hSmmWdx1a8rs', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Define a handler for the /cast command
def broadcast_message(update, context):
    # Ask for the message to broadcast
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter the message you want to broadcast:")

    # Set up a message handler to receive the broadcast message
    context.bot.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, confirm_broadcast_message))

def confirm_broadcast_message(update, context):
    # Get the message to broadcast from the user's input
    message_text = update.message.text

    # Ask for confirmation before broadcasting
    confirmation_message = f"You are about to broadcast the following message:\n\n{message_text}\n\nPlease confirm (yes/no):"
    context.bot.send_message(chat_id=update.effective_chat.id, text=confirmation_message)

    # Set up a message handler to receive the confirmation
    context.bot.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_broadcast_confirmation))

def process_broadcast_confirmation(update, context):
    # Get the confirmation from the user's input
    confirmation = update.message.text.lower()

    if confirmation == "yes":
        # Get a list of all active chats
        active_chats = context.bot.get_updates()[-1].message.chat

        # Send the message to each chat
        for chat in active_chats:
            context.bot.send_message(chat_id=chat.id, text=message_text, parse_mode=ParseMode.HTML)

        context.bot.send_message(chat_id=update.effective_chat.id, text="Message successfully broadcasted!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Broadcast canceled.")

    # Remove the temporary message handler
    context.bot.dispatcher.remove_handler(process_broadcast_confirmation)

# Register the command handlers
broadcast_handler = CommandHandler('cast', broadcast_message)
dispatcher.add_handler(broadcast_handler)

# Start the bot
updater.start_polling()
