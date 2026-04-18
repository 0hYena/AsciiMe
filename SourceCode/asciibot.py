import discord
from discord.ext import commands
from discord import app_commands
from pyfiglet import Figlet, FigletFont

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=SERVER-ID)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'ERROR!! syncing command failed: {e}')

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=SERVER-ID)

all_fonts = FigletFont.getFonts()

async def font_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=font, value=font)
        for font in all_fonts if current.lower() in font.lower()
    ][:25]  # Discord limit = 25 choices


@client.tree.command(name="ascii", description="Convert Text to ASCII", guild=GUILD_ID)
@app_commands.describe(input1="Text to convert", font="Choose a font")
@app_commands.autocomplete(font=font_autocomplete)
async def AsciiConvert(
    interaction: discord.Interaction,
    input1: str,
    font: str
):
    try:
        f = Figlet(font=font)
        ascii_text = f.renderText(input1)

        await interaction.response.send_message(f"```{ascii_text}```")

    except Exception as e:
        await interaction.response.send_message(f"Error:\n```{str(e)}```")



@client.tree.command(name="ascii2", description="Convert Text using Custom Font", guild=GUILD_ID)
@app_commands.describe(input1="Text to convert")
async def AsciiConvertCustom(interaction: discord.Interaction, input1: str):
    try:
    
        FigletFont.FONT_DIR = r'CUSTOM-FONT-DIRECTORY'

        f = Figlet(font='CUSTOM-FONT-NAME')

        ascii_text = f.renderText(input1)

        await interaction.response.send_message(f"```{ascii_text}```")

    except Exception as e:
        await interaction.response.send_message(f"Error:\n```{str(e)}```")

client.run("TOKEN")
