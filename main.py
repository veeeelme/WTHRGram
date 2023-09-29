from telebot import *
import python_weather
import sys
import asyncio
import os


async def get_weather(city):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)

        return f'Current kind: {weather.current.kind}\nCurrent temperture: {weather.current.temperature}℃\nCurrent humidty: {weather.current.humidity}%\nCurrent pressure: {weather.current.pressure}hPa\nCurrent visibility: {weather.current.visibility} km\nCurrent wind speed: {weather.current.wind_speed} km/h\nCurrent wind direction: {weather.current.wind_direction} deg.\nUltraviolet rate: {weather.current.ultraviolet.name}\nCurrent date: {weather.current.date}\n'

# for next versions:
# async def get_forecast(city):
#     async with python_weather.Client(unit=python_weather.METRIC) as client:
#         weather = await client.get(city)
#         choice = input('Forecast or hourly forecast? 1/2 >> ')
#         if choice == '1':
#             for forecast in weather.forecasts:
#                 print(f'Date: {forecast.date}\n'
#                       f'Primary temperature: {forecast.temperature}℃\nLowest temperature: {forecast.lowest_temperature}℃\nHighest temperature: {forecast.highest_temperature}℃')

#         if choice == '2':
#             for forecast in weather.forecasts:
#                 forecast

#             for hour in forecast.hourly:
#                 print(
#                     f'\nTime: {hour.time.hour!r}:{hour.time.minute!r}\nTemperature: {hour.temperature!r}℃\nKind: {hour.description!r}\nFeels like: {hour.feels_like!r}℃\nWind direction: {hour.wind_direction.name!r} or {hour.wind_direction.degrees!r} deg.\nWind speed: {hour.wind_speed!r} km/h\nWind gusts: {hour.wind_gust!r} km/h\nPressure: {hour.pressure!r} hPa\nVisibility: {hour.visibility!r}\nUltraviolet rate: {hour.ultraviolet.name}\n')


bot = telebot.TeleBot('api key here')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'{message.from_user.first_name}'
    bot.send_message(message.chat.id, f'Hi, <b>{mess}</b>', parse_mode='html')


@bot.message_handler()
def get_city_weather(message):
    bot.send_message(
        message.chat.id, f'Done! {asyncio.run(get_weather(message.text))}')


bot.polling(none_stop=True)
