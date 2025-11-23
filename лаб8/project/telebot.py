from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен, полученный от BotFather
TOKEN = ''

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Приветствие", callback_data='привет'),
         InlineKeyboardButton("До свидания", callback_data='пока')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text('Выберите вариант:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'привет':
        await query.edit_message_text(text="Привет!")
    elif query.data == 'пока':
        await query.edit_message_text(text="До встречи!")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Обработчик нажатия кнопки
    application.add_handler(CallbackQueryHandler(button))
    
    print("Микробот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()