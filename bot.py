from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import requests
import json
from datetime import datetime

BOT_TOKEN = os.environ.get("8319464760:AAGepXLQJEJdIE8SsxEBNisEeD_gebFVr8E")

# Advanced Responses Database
RESPONSES = {
    'hello': ['Namaste!', 'Hello!', 'Hi there!', 'Kaise ho?'],
    'how are you': ['Main mast hoon!', 'Badhiya! Aap sunao?', 'Theek thak!'],
    'time': ['Abhi time hai: {time}', 'Samay: {time}'],
    'joke': ['Kyun scientist computer se naraz tha? Kyonki usne USB ko ulta lagaya!',
             'Dono eggs highway par the, ek egg ne kaha: "Chalo race karte hain!" Dusra bola: "Nahi, dar lagta hai!" Pehla bola: "Kyun?" Dusra bola: "Kyunki main andar se half boiled hoon!"'],
    'weather': ['Mujhe abhi weather ka access nahi hai, lekin aap Google par check kar sakte hain!'],
    'bye': ['Alvida!', 'Phir milenge!', 'Take care!']
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    welcome_text = f"""
🤖 *Welcome {user_name}!*

*Available Commands:*
/start - Start bot
/help - Help menu  
/time - Current time
/joke - Funny joke
/weather - Weather info
/about - About this bot

Mujhe koi bhi message bhej kar baat kar sakte hain!
    """
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🆘 *Help Guide*

*Commands List:*
/start - Bot start karein
/help - Yeh help message
/time - Current time batayega
/joke - Funny joke sunayega
/weather - Weather information
/about - Bot ke bare mein

*Normal Chat:*
- Hello, Hi, Namaste
- How are you, Kaise ho
- Time kya hai
- Joke sunao
- Weather kaisa hai
- Bye, Goodbye
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(f"🕐 Current Time: {current_time}")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    joke_text = random.choice(RESPONSES['joke'])
    await update.message.reply_text(f"😂 {joke_text}")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌤️ " + RESPONSES['weather'][0])

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = """
🤖 *Advanced AI Bot*

*Version:* 2.0
*Developer:* [Your Name]
*Features:* 
- Smart Conversations
- Multiple Commands  
- Jokes & Fun
- Time & Info
- Weather Updates

*Technology:* Python + Telegram Bot API
    """
    await update.message.reply_text(about_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    user_name = update.message.from_user.first_name
    
    # Smart Response System
    response = None
    
    if any(word in text for word in ['hello', 'hi', 'namaste', 'hey']):
        import random
        response = f"{random.choice(RESPONSES['hello'])} {user_name}!"
    
    elif any(word in text for word in ['how are you', 'kaise ho', 'kya haal']):
        import random
        response = random.choice(RESPONSES['how are you'])
    
    elif any(word in text for word in ['time', 'samay', 'kitne baje']):
        current_time = datetime.now().strftime("%H:%M:%S")
        response = f"🕐 Time: {current_time}"
    
    elif any(word in text for word in ['joke', 'chutkula', 'hasao']):
        import random
        response = "😂 " + random.choice(RESPONSES['joke'])
    
    elif any(word in text for word in ['weather', 'mausam', 'temperature']):
        response = "🌤️ " + RESPONSES['weather'][0]
    
    elif any(word in text for word in ['bye', 'goodbye', 'alvida']):
        response = "👋 " + random.choice(RESPONSES['bye'])
    
    elif any(word in text for word in ['thank', 'thanks', 'dhanyavad']):
        response = "👍 You're welcome!"
    
    elif any(word in text for word in ['i love you', 'pyaar', 'love']):
        response = "😊 Thank you! Main aapko bhi pyaar karta hoon!"
    
    else:
        response = f"🤔 Main samjha nahi '{text}'. /help type karein commands dekhne ke liye."
    
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")

if __name__ == '__main__':
    print("🤖 Advanced Bot Starting...")
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Command Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("time", time))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(CommandHandler("weather", weather))
    app.add_handler(CommandHandler("about", about))
    
    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Error Handler
    app.add_error_handler(error)
    
    print("✅ Bot Running Successfully...")
    app.run_polling()