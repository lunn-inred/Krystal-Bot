import discord
from discord import app_commands
from discord.ext import commands
import random


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.operations = ["-", "*", "/", "+"]
        super().__init__()

    # CHAT COMMANDS #
    @commands.command()
    async def calcular(self, ctx: commands.Context, *, expression):
        control = 0
        valid_expression = True
        for char in expression:
            if char not in self.operations:
                control += 1
                if control == len(expression):
                    valid_expression = False

            if char.isalpha():
                valid_expression = False
                break

        if valid_expression:
            try:
                await ctx.send(eval(expression))
            except:
                await ctx.send("ayyy que besteira")
        else:
            await ctx.send("ayyyyyyyy que besteira")

    @commands.command()
    async def random(self, ctx: commands.Context, n1: int = None, n2: int = None):
        try:
            num1 = min(n1, n2)
            n2 = max(n1, n2)
            result = random.randint(int(num1), int(n2))
            await ctx.send(f"seu numero eh: {result}")

        except:
            n1, n2 = 0, 10
            result = random.randint(n1, n2)
            await ctx.send(f"seu numero eh: {result}")


async def setup(bot):
    await bot.add_cog(Math(bot))

