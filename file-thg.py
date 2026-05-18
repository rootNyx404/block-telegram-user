import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Your bot token from BotFather
TOKEN = "YOUR_BOT_TOKEN_HERE"

# List of admin user IDs (you can get your user ID by sending /start to @userinfobot)
ADMIN_IDS = [123456789, 987654321]  # Replace with your admin user IDs

def is_admin(user_id):
    """Check if the user is an admin"""
    return user_id in ADMIN_IDS

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('হ্যালো! আমি চ্যানেল ব্যান বট। আমি সাহায্য করতে পারি চ্যানেল সদস্যদের ব্যান করতে।')

def ban_user(update: Update, context: CallbackContext) -> None:
    """Ban a user from the channel"""
    if not is_admin(update.effective_user.id):
        update.message.reply_text("আপনার এই কমান্ড ব্যবহার করার অনুমতি নেই।")
        return
    
    if len(context.args) == 0:
        update.message.reply_text("ব্যবহার: /ban @username অথবা /ban user_id")
        return
    
    user_to_ban = context.args[0]
    
    # Remove @ if it's a username
    if user_to_ban.startswith('@'):
        user_to_ban = user_to_ban[1:]
    
    try:
        # Try to get the user from the context
        chat_id = update.effective_chat.id
        
        # Try to ban by username
        if user_to_ban.isalpha():
            context.bot.ban_chat_member(chat_id, user_to_ban)
            update.message.reply_text(f"@{user_to_ban} কে চ্যানেল থেকে ব্যান করা হয়েছে।")
        # Try to ban by user ID
        else:
            context.bot.ban_chat_member(chat_id, int(user_to_ban))
            update.message.reply_text(f"User ID {user_to_ban} কে চ্যানেল থেকে ব্যান করা হয়েছে।")
            
    except Exception as e:
        update.message.reply_text(f"ব্যান করতে ত্রুটি হয়েছে: {str(e)}")

def unban_user(update: Update, context: CallbackContext) -> None:
    """Unban a user from the channel"""
    if not is_admin(update.effective_user.id):
        update.message.reply_text("আপনার এই কমান্ড ব্যবহার করার অনুমতি নেই।")
        return
    
    if len(context.args) == 0:
        update.message.reply_text("ব্যবহার: /unban @username অথবা /unban user_id")
        return
    
    user_to_unban = context.args[0]
    
    # Remove @ if it's a username
    if user_to_unban.startswith('@'):
        user_to_unban = user_to_unban[1:]
    
    try:
        chat_id = update.effective_chat.id
        
        # Try to unban by username
        if user_to_unban.isalpha():
            context.bot.unban_chat_member(chat_id, user_to_unban)
            update.message.reply_text(f"@{user_to_unban} কে চ্যানেলে আনব্যান করা হয়েছে।")
        # Try to unban by user ID
        else:
            context.bot.unban_chat_member(chat_id, int(user_to_unban))
            update.message.reply_text(f"User ID {user_to_unban} কে চ্যানেলে আনব্যান করা হয়েছে।")
            
    except Exception as e:
        update.message.reply_text(f"আনব্যান করতে ত্রুটি হয়েছে: {str(e)}")

def main() -> None:
    """Start the bot."""
    updater = Updater(TOKEN)
    
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ban", ban_user))
    dispatcher.add_handler(CommandHandler("unban", unban_user))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()