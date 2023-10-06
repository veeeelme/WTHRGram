from telebot import *
import weather
import sys
import os

weatherAPI = weather.API('weather api api key') 


def get_weather(city):
    weather = weatherAPI.current(city)
    return f"\nToday`s temperature is {weather['current']['temp_c']} and kind of weather is {weather['current']['condition']['text']}. Wind speed is {weather['current']['wind_kph']} kph and direction is {weather['current']['wind_dir']}.\n\n" \
        f"Other info: \nPressure: {weather['current']['humidity']}%\nFeels like: {weather['current']['feelslike_c']}\nVisibility: {weather['current']['vis_km']} km\nUltraviolet index: {weather['current']['uv']}\nGust: {weather['current']['gust_kph']} kph\n(Info for {weather['current']['last_updated']})"


bot = telebot.TeleBot('telegram bot api key')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'{message.from_user.first_name}'
    bot.send_message(message.chat.id, f'Hi, <b>{mess}</b>', parse_mode='html')


@bot.message_handler()
def get_city_weather(message):
    bot.send_message(
        message.chat.id, f'Done! {get_weather(message.text)}')


bot.polling(none_stop=True)
