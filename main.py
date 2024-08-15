import os

import discord
import dotenv
from discord.ext import commands
from discord import Intents
from discord import app_commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix="^^", intents=intents)


async def load_cogs():
    for cog in os.listdir("cogs"):
        if cog.endswith(".py"):
            await bot.load_extension(f"cogs.{cog[:-3]}")


@bot.command()
async def sync(ctx: commands.Context):
    if ctx.author.id == 750201601314259008:
        sincs = await bot.tree.sync()
        await ctx.send(f"{len(sincs)} comandos sincronizados")
    else:
        await ctx.send(f"so a luna pode usar esse comando grrrrr")


@bot.command()
async def echo(ctx: commands.Context, *, msg: str = None):
    if not msg:
        await ctx.send("nao tem oq eu repetir :rage:")
    try:
        args = ctx.message.content.split()
        channelName = args[-1]
        channel = discord.utils.get(ctx.guild.channels, name=channelName)

        message = msg.removesuffix(channelName)

        await channel.send(message)
        await ctx.message.delete()

    except:
        await ctx.send(f"{msg}")
        await ctx.message.delete()

@bot.tree.command(description="repete a mensagem que o ususario enviou")
async def echo(interaction: discord.Interaction, msg:str):
    try:

        args = interaction.message.content.split()
        channelName = args[-1]
        channel = discord.utils.get(interaction.guild.channels, name=channelName)

        message = msg.removesuffix(channelName)

        await channel.send(f"{message}")
    except:

        await interaction.response.send_message(f"{msg}")


@bot.tree.command()
@app_commands.choices(cor=[
    app_commands.Choice(name="Vemelho",value="#ff0000"),
    app_commands.Choice(name="Amarelo",value="#ffff00"),
    app_commands.Choice(name="Verde",value="#00ff00"),
    app_commands.Choice(name="Azul",value="#0000ff ")
])
async def cor(interact:discord.Interaction, cor:app_commands.Choice[str]):
    await interact.response.send_message(f"o hex dessa cor eh: {cor.value}")


@bot.command()
async def botao(ctx:commands.Context):
    async def resposta(interact:discord.Interaction):
        await interact.response.send_message("fasoeli", ephemeral=True)

    view = discord.ui.View()
    botao = discord.ui.Button(label="botao",style=discord.ButtonStyle.blurple)
    botao.callback = resposta

    botao_url = discord.ui.Button(label="botao2",url="https://youtu.be/qIPqbUyM2VI?si=sDQifBK8TsQnS-jM")

    view.add_item(botao)
    view.add_item(botao_url)
    await ctx.reply(view=view)

@bot.command()
async def selecionar(ctx:commands.Context):
    async def resposta(interact:discord.Interaction):
        escolha = interact.data["values"][0]
        dict = {"0":"opcao 1","1":"opcao 2","2":"opcao 3","3":"opcao 4"}
        escolhido = dict[escolha]
        await interact.response.send_message(f"vose escolheu: {escolhido}")


    menu = discord.ui.Select(placeholder="Escolha")
    opcoes = [
        discord.SelectOption(label="opcao1",value="0"),
        discord.SelectOption(label="opcao2",value="1"),
        discord.SelectOption(label="opcao3",value="2"),
        discord.SelectOption(label="opcao4",value="3")
    ]
    menu.options = opcoes

    menu.callback = resposta
    view = discord.ui.View()
    view.add_item(menu)

    await ctx.send(view=view)

@bot.command()
async def enviar_embed(ctx:commands.Context,membro:discord.Member = None):
    try:
        meu_embed = discord.Embed(title="testestestes", description="oizinho!!")
        meu_embed.set_thumbnail(url=membro.avatar)
        meu_embed.color = discord.Color.from_rgb(176, 148, 166)
        meu_embed.set_image(url=membro.banner)

        await ctx.reply(embed=meu_embed)
    except:
        membro = ctx.message.author
        meu_embed = discord.Embed(title="testestestes", description="oizinho!!")
        meu_embed.set_thumbnail(url=membro.avatar)
        meu_embed.color = discord.Color.from_rgb(176, 148, 166)
        meu_embed.set_image(url=membro.banner)

        await ctx.reply(embed=meu_embed)

@bot.event
async def on_ready():
    await load_cogs()
    await bot.change_presence(status=discord.Status.idle,activity=discord.CustomActivity(name= "pipipi popopo"))


bot.run(TOKEN)
