import discord
from discord.ext import commands
import aiohttp
import ujson
from secret import weather_token
from aiogoogletrans import Translator
from aiogoogletrans.constants import LANGUAGES
import asyncio


async def get_weather_json(city):
    async with aiohttp.ClientSession(
            json_serialize=ujson.dumps) as session:
        try:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={weather_token}'

            await session.post(url,
                               json={'test': 'object'})
            async with session.get(
                    url) as resp:
                result = await resp.json()

                weather_desc = result['weather']
                for weather_list in weather_desc:
                    description = weather_list['description']
                    weather_vis = result['visibility']
                    weather_temp = result['main']
                    current_temp = weather_temp['temp']
                    feels_like = weather_temp['feels_like']
                    temp_min = weather_temp['temp_min']
                    temp_max = weather_temp['temp_max']
                    current_pressure = weather_temp['pressure']
                    current_humidity = weather_temp['humidity']
                    weather_wd = result['wind']
                    weather_wind_speed = weather_wd['speed']

                    weather_in_the_city = description, current_temp, feels_like, temp_min, temp_max, \
                                          current_pressure, current_humidity, weather_vis, weather_wind_speed
        except:
            return 'None'
        else:
            return weather_in_the_city


class GeneralCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx, city):
        try:
            city = ctx.message.content.lower().split()[1]
            data = await get_weather_json(city)
            embed = discord.Embed(title=data[0].capitalize(), color=0xd81313)
            embed.set_author(name=city.capitalize())
            embed.add_field(name='Current temperature', value=str(data[1]) + '°C', inline=True)
            embed.add_field(name="Feels like", value=str(data[2]) + '°C', inline=True)
            embed.add_field(name='Humidity', value=str(data[6]) + '°%', inline=True)
            embed.add_field(name="Pressure", value=str(data[5]) + 'mbars', inline=True)
            embed.add_field(name="Wind", value=str(data[-1]) + 'm/s', inline=True)
            embed.add_field(name="Visibility", value=str(data[-2]), inline=True)
            embed.set_footer(text="OpenWeather")
        except:
            await ctx.send('None')
        else:
            await ctx.send(embed=embed)
            return city

    @commands.command()
    async def convert(self, ctx, from_currency, to_currency, amount):
        try:
            message_to_split = ctx.message.content[8::]
            spit_message = message_to_split.split()
            from_currency = spit_message[0]
            to_currency = spit_message[1]
            initial_amount = int(spit_message[2])
            async with aiohttp.ClientSession(
                    json_serialize=ujson.dumps) as session:
                url = str("http://data.fixer.io/api/latest?access_key=d387292f1ba52feb8e1055840e9aea59")
                await session.post(url, json={'test': 'object'})
                async with session.get(url) as resp:
                    data = await resp.json()

                rates = data["rates"]

                initial_amount = amount
                if from_currency != 'EUR':
                    amount = int(amount) / rates[from_currency]
                amount = round(amount * rates[to_currency], 2)
                result_message = f"{initial_amount} {from_currency} = {amount} {to_currency}"
                await ctx.send(result_message)
        except:
            await ctx.send('None')

    @commands.command()
    async def translate(self, ctx):
        try:
            translator = Translator()
            dest_lang = ctx.message.content.split()[1]
            if dest_lang in LANGUAGES.keys():
                result = await translator.translate(ctx.message.content[14::], dest=dest_lang)
            else:
                result = await translator.translate(ctx.message.content[10::], dest='ru')

            await ctx.send(result.text)
        except:
            await ctx.send('None')


def setup(client):
    client.add_cog(GeneralCommands(client))
