import discord
from discord import app_commands
from discord.ext import commands
import random


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.operations = ["-", "*", "/", "+"]
        super().__init__()

    # SLASH COMMANDS #
    @app_commands.command(description="repete a mensagem que o ususario enviou")
    @app_commands.describe(expressao="a expressao a ser calculada")
    async def calcular(self, interaction: discord.Interaction, expressao: str):
        control = 0
        valid_expression = True
        for char in expressao:
            if char not in self.operations:
                control += 1
                if control == len(expressao):
                    valid_expression = False

            if char.isalpha():
                valid_expression = False
                break

        if valid_expression:
            try:
                await interaction.response.send_message(eval(expressao))
            except:
                await interaction.response.send_message("ayyy que besteira")
        else:
            await interaction.response.send_message("ayyyyyyyy que besteira")

    @app_commands.command(description="responde um numero inteiro dentro de um intervalo")
    @app_commands.describe(n1="Inicio do intervalo", n2="Final do intervalo")
    async def random(self, interact: discord.Interaction, n1: int = None, n2: int = None):
        try:
            num1 = min(n1, n2)
            n2 = max(n1, n2)
            result = random.randint(int(num1), int(n2))
            await interact.response.send_message(f"seu numero eh: {result}")

        except:
            n1, n2 = 0, 10
            result = random.randint(n1, n2)
            await interact.response.send_message(f"seu numero eh: {result}")


async def setup(bot):
    await bot.add_cog(Slash(bot))
