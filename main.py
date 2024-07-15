import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable the MESSAGE_CONTENT intent
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("The Bot is ready !")
    print("--------------------------------")

async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author.bot:
        return

    # Define a list of keywords
    keywords = ["name", "username", "nickname"]

    # Check if the message contains any of the keywords
    if any(keyword in message.content.lower() for keyword in keywords):
        await message.channel.send("What's your name? ")
    
        def check(m):
            # Check if the message is from the same user and in the same channel
            return m.author == message.author and m.channel == message.channel
    
        try:
            msg = await client.wait_for('message', check=check, timeout=30.0)  # 30 seconds to reply
        except asyncio.TimeoutError:
            await message.channel.send("Sorry, you took too long to reply.")
        else:
            await message.channel.send(f"Hello {msg.content}!")

    # Add this line to allow other commands to be processed
    await client.process_commands(message)

@client.command()
@commands.is_owner()  # This ensures only the owner of the bot can use this command
async def logout(ctx):
    await ctx.send("Logging out...")
    await client.logout()

client.run('DISCORD_BOT_TOKEN')