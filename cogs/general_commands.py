import discord
from discord.ext import commands

import ujson

import aiohttp

from currency_convert import CurrencyConvertor
from secret import weather_token


async def get_weather_json(city):
    async with aiohttp.ClientSession(
            json_serialize=ujson.dumps) as session:
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
    return weather_in_the_city


class GeneralCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx):
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

        await ctx.send(embed=embed)
        return city

    @commands.command()
    async def convert(self, ctx):
        url = str.__add__('http://data.fixer.io/api/latest?access_key=', "d387292f1ba52feb8e1055840e9aea59")
        c = CurrencyConvertor(url)
        message_to_split = ctx.message.content[8::]
        spit_message = message_to_split.split()
        from_country = spit_message[0]
        to_country = spit_message[1]
        initial_amount = int(spit_message[2])
        res = c.convert(from_country, to_country, initial_amount)
        result_message = f"{initial_amount} {from_country} = {res} {to_country}"
        await ctx.send(result_message)




def setup(client):
    client.add_cog(GeneralCommands(client))
