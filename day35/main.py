import os
import requests, base64
from dotenv import load_dotenv
import json
import telegram
import asyncio
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

load_dotenv()

OW_API_KEY = os.getenv('OW_API')

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
GEO_CODE_URL = f"http://api.openweathermap.org/geo/1.0/direct?"
TELEGRAM_URL = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/getUpdates"

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text('Bye! Hope to talk to you again soon.', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

# Dictionary to store user states
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_data[chat_id] = {"awaiting_input": "location"}
    
    # Ask the user for the location
    await update.message.reply_text("Hi there! Please enter your location to get the current weather.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    # Check if the user is expected to provide input
    if chat_id in user_data and user_data[chat_id].get("awaiting_input") == "location":
        location = update.message.text
        user_data[chat_id]["location"] = location
        
        weather_data = get_current_weather(location)

        # Respond with a personalized message
        await update.message.reply_text(weather_data)
        
        # Clear the input state
        user_data[chat_id]["awaiting_input"] = None
    else:
        await update.message.reply_text("I didn't understand that. Please use /start to begin.")

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    application = ApplicationBuilder().token(os.getenv('TELEGRAM_TOKEN')).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    application.run_polling()

def get_lat_lon(location):
    geo_url = GEO_CODE_URL + f"q={location}&limit=5&appid={OW_API_KEY}"
    response = requests.get(geo_url)
    geo_data = json.loads(response.text)
    return geo_data[0]['lat'], geo_data[0]['lon']

def kelvin_to_fahrenheit(kelvin_temp):
    fahrenheit_temp = (kelvin_temp - 273.15) * 9/5 + 32
    return round(fahrenheit_temp, 2)

def get_current_weather(location):
    lat, lon = get_lat_lon(location)
    URL = BASE_URL + f"lat={lat}&lon={lon}&appid={OW_API_KEY}"
    
    response = requests.get(URL)
    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return f"""
        🌍 The current weather in {location}
        Main: {weather_conditions_emojis(weather_data['weather'][0]['main'])} {weather_data['weather'][0]['main']}
        Description: {weather_data['weather'][0]['description']}
        - Details
            🌡️ Temp: {kelvin_to_fahrenheit(weather_data['main']['temp'])} °F
            🌡️ Feels_like: {kelvin_to_fahrenheit(weather_data['main']['feels_like'])} °F
            🔻 Min Temp: {kelvin_to_fahrenheit(weather_data['main']['temp_min'])} °F
            🔺 Max Temp: {kelvin_to_fahrenheit(weather_data['main']['temp_max'])} °F
            💧 Humidity: {weather_data['main']['humidity']}
            📉 Pressure: {weather_data['main']['pressure']}  
        http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}.png
        """
    else:
        return "Sorry, I couldn't retrieve the weather information. Please try another location."

def weather_conditions_emojis(condition):
    weather_emojis = {
        "Rain": "🌧️",
        "Thunderstorm": "⛈️",
        "Drizzle": "🌦️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Smoke": "💨",
        "Haze": "🌤️",
        "Fog": "🌁",
        "Sand": "🏜️",
        "Dust": "🌪️",
        "Ash": "🌋",
        "Squall": "🌬️",
        "Tornado": "🌪️",
        "Clouds": "☁️",
        "Clear": "☀️"
    }

    return weather_emojis[condition]

def get_telegram_chat_id():
    response = requests.get(TELEGRAM_URL)
    tg_data = json.loads(response.text)
    return tg_data['result'][0]['message']['chat']['id']

def get_icon_data(icon_id):
    url = f'http://openweathermap.org/img/wn/{icon_id}.png'
    response = requests.get(url, stream=True)
    return base64.encodebytes(response.raw.read())

if __name__ == "__main__":
    main()
    #location = 'Raleigh'
    #data = get_current_weather(location)
    #weather_data = extract_weather_condition(data)
    #icon_data = get_icon_data(icon)

    #chat_id = get_telegram_chat_id()
    #bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))

    #asyncio.run(bot.send_message(chat_id=chat_id, text=f'Weather: {weather_data["main"]} \n Description: {weather_data["description"]} \n http://openweathermap.org/img/wn/{weather_data["icon"]}.png',  parse_mode='Markdown'))
