import discord
import responses
import os
from cthulhu import MAIN_URL

TOKEN = os.getenv('TOKEN')


async def send_message(message, user_message):
    try:
        response = responses.handle_response_command(user_message)
        if response:
            await message.channel.send(response)
        else:
            await send_armello_message(message, user_message)

    except Exception as e:
        print(e)


async def send_armello_message(message, user_message):
    response = responses.handle_response_text(user_message)
    response_image = responses.handle_response_image(user_message)
    if response:
        embed = discord.Embed(title=user_message, description=response)
        embed.set_image(url=response_image)
        embed.set_footer(text="Source: " + MAIN_URL)
        await message.channel.send(embed=embed)


def run_bot():
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # print(f"{username} said: '{user_message}' ({channel})")

        await send_message(message, user_message)

    client.run(TOKEN)


