from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    ContextTypes,
)

print('Starting up bot...')

TOKEN: Final = '6157232210:AAH0PwvUxKYdZEuSANDlXyn_h8KDh8DeiNQ'
BOT_USERNAME: Final = '@AvgTrader_Bot'

# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("The VIX Ultimate Guide", callback_data="vix_guide")],
        [InlineKeyboardButton("Back 2 Basics Course", callback_data="back2basics")],
        [InlineKeyboardButton("YouTube Channel", url="https://www.youtube.com/channel/UC6ONF2ZuVJTzXmsqPoWfP8Q?sub_confirmation=1")],
        [InlineKeyboardButton("Free Telegram Channe l", url="https://t.me/UrAvgTraderVixOnly")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hi There!\nThank you for choosing UrAvgTrader!\n\n"
        "Are you Interested in purchasing the Vix Ultimate Guide, the Back 2 Basics Course, "
        "or would you like to check out our YouTube and Telegram channels?",
        reply_markup=reply_markup
    )


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Try typing anything and I will do my best to respond!')

# The handler for button clicks
async def handle_button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    query.answer()  # Acknowledge the button click

    if query.data == "vix_guide":
        response = (
            "1. The VIX Ultimate Guide 📝\n"
            "2. VIX Only Setups and Analysis Group 🤓👔\n"
            "3. Access to my Exclusive Trading Strategy 💹\n"
            "   (Including my Vix Risk Calculator)\n"
            "4. Educational Content / Trading Tips ✍🏽\n"
            "5. Limited 1 on 1 access to me for any help 💪🏾💪🏾\n"
            "One-time payment of $59\n\n"
            "Please send confirmation to @UrAvgTrader on Telegram after payment is made.\n"
            "Payment Methods Include:"
        )
        keyboard = [
            [InlineKeyboardButton("PayPal", url="https://www.paypal.me/ShannonSolomon")],
            [InlineKeyboardButton("JMMB Bank", callback_data="jmmb_bank")],
            [InlineKeyboardButton("ScotiaBank", callback_data="scotiabank")],
            [InlineKeyboardButton("Zelle", callback_data="zelle")],
            [InlineKeyboardButton("crypto", url="https://t.me/UrAvgTrader")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    elif query.data == "back2basics":
        response = (
            "1. Back to Basics PDF Guide to Trading Synthetic Indices 📝\n"
            "2. Access to the Back 2 Basics Video Library 💹✍🏽\n"
            "3. The Basics of Technical Analysis✍🏽\n"
            "4. My Exclusive Trading Strategy🤓👔\n"
            "5. Lifetime Access to my VIX Only Setups and Analysis Groups💪🏾💪🏾\n"
            "6. Limited 1 on 1 Access to me for any help with the content. ✍🏽\n"
            "One-time payment of $199\n\n"
            "Please send confirmation to @UrAvgTrader on Telegram after payment is made.\n"
            "Payment Methods Include:"
        )
        keyboard = [
            [InlineKeyboardButton("PayPal", url="https://www.paypal.me/ShannonSolomon")],
            [InlineKeyboardButton("JMMB Bank", callback_data="jmmb_bank")],
            [InlineKeyboardButton("ScotiaBank", callback_data="scotiabank")],
            [InlineKeyboardButton("Zelle", callback_data="zelle")],
            [InlineKeyboardButton("crypto", url="https://t.me/UrAvgTrader")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    elif query.data == "jmmb_bank":
        response = (
            "\n \n JMMB Bank-\n"
            "Name: Shannon Solomon\n"
            "Branch: Fairview Montego Bay\n\n"
            "JA$ (Chequing Account)\n"
            "0086-0000-2598 JA ($ 9,000)\n\n"
            "US$ (Chequing Account)\n"
            "0086-0000-2829 US ($ 59) \n"
            " \nPlease send confirmation to @UrAvgTrader on Telegram after payment is made.\n"
        )
        await query.message.reply_text(response)
    elif query.data == "scotiabank":
        response = (
            "\n \n ScotiaBank-\n"
            "Name: Shannon Solomon\n"
            "Branch: Falmouth\n"
            "Acct #: 000426236 ($ JA Savings)\n"
            "$ 9,000 \n"
            "\nPlease send confirmation to @UrAvgTrader on Telegram after payment is made.\n"
        )

        await query.message.reply_text(response)
    elif query.data == "zelle":
        response = "\nZelle payment can be made to the following email address: \n \n Shansolomon93@gmail.com \n \n Please send confirmation to @UrAvgTrader on Telegram after payment is made."
        await query.message.reply_text(response)

    else:
        response = "Invalid selection"
        reply_markup = None

    await query.message.reply_text(response, reply_markup=reply_markup)

# The handler for messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Rest of the handle_message logic

# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(CallbackQueryHandler(handle_button_click, pattern="^(vix_guide|back2basics|jmmb_bank|scotiabank|zelle|crypto)$"))


    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)
