from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from asgiref.sync import sync_to_async
from telegram_bot.models import TelegramUser

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Saves the user to the database on /start command."""
    chat_id = update.effective_chat.id
    username = update.effective_chat.username

    @sync_to_async
    def save_user():
        user, created = TelegramUser.objects.get_or_create(
            chat_id=str(chat_id),
            defaults={'username': username}
        )
        if created:
            message = f"Welcome, {username}! Your info has been saved."
        else:
            if user.username != username:
                user.username = username
                user.save()
            message = f"Welcome back, {username}!"
        return message

    message = await save_user()
    await update.message.reply_text(message)

class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **options):
        """The main entry point for the management command."""
        self.stdout.write(self.style.SUCCESS('Starting bot...'))
        
        application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
        
        application.add_handler(CommandHandler("start", start))
        
        application.run_polling()
        
        self.stdout.write(self.style.SUCCESS('Bot stopped.')) 