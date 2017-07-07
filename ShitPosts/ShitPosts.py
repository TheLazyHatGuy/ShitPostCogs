import discord
from discord.ext import commands
from random import choice

class ShitPosts():
    """Some shitpost commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dong(self):
        """Dong Shitpost"""
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        dongers = discord.Embed(description="ヽ༼ຈل͜ຈ༽ﾉ RAISE YOUR DONGERS ヽ༼ຈل͜ຈ༽ﾉ ", colour=discord.Colour(value=color))
        await self.bot.say(embed=dongers)

    @commands.command()
    async def blob(self):
        """I am blob"""
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        toembed = discord.Embed(description="I am one with the blob, the blob is with me. ༼ つ ◕_◕ ༽つ",
                                colour=discord.Colour(value=color))
        await self.bot.say(embed=toembed)

    @commands.command()
    async def repeat(self, times: int, content='repeating...'):
        """Repeats a message multiple times."""
        for i in range(times):
            await self.bot.say(content)

    @commands.command()
    async def bee(self, part: int):
        """Prints bee movie script. Requires script part number e.g ?bee 1"""
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        print(part)
        if part == 1:
            Bee1 = "According to all known laws of aviation,\n there is no way a bee should be able to fly.\n Its wings are too small to get its fat little body off the ground.\n The bee, of course, flies anyway because bees don't care what humans think is impossible.\nYellow, black. Yellow, black.\nYellow, black. Yellow, black.\nOoh, black and yellow!\nLet's shake it up a little.\nBarry! Breakfast is ready!\nOoming!\nHang on a second.\n"
            BeeScript = discord.Embed(description=Bee1, colour=discord.Colour(value=color), title="Bee Movie Pt.1")
        elif part == 2:
            Bee2 = "- Hey, Adam.\n- Hey, Barry.\n- Is that fuzz gel?\n- A little. Special day, graduation.\nNever thought I'd make it.\nThree days grade school, three days high school.\nThose were awkward.\nThree days college. I'm glad I took a day and hitchhiked around the hive.\nYou did come back different.\n- Hi, Barry.\n- Artie, growing a mustache? Looks good.\n- Hear about Frankie?\n- Yeah.\n- You going to the funeral?\n- No, I'm not going.\nEverybody knows, sting someone, you die.\nDon't waste it on a squirrel.\nSuch a hothead.\nI guess he could have just gotten out of the way.\nI love this incorporating an amusement park into our day.\nThat's why we don't need vacations.\nBoy, quite a bit of pomp... under the circumstances.\n- Well, Adam, today we are men.\n- We are!\n- Bee-men.\n- Amen!\nHallelujah!\nStudents, faculty, distinguished bees, please welcome Dean Buzzwell.\nWelcome, New Hive Oity graduating class of...\n...9:15.\nThat concludes our ceremonies.\nAnd begins your career at Honex Industries!\nWill we pick our job today?\nI heard it's just orientation.\nHeads up! Here we go.\nKeep your hands and antennas inside the tram at all times.\n"
            BeeScript = discord.Embed(description=Bee2, colour=discord.Colour(value=color), title="Bee Movie Pt.2")
        else:
            BeeScript = discord.Embed(description="Part doesn't exist", colour=discord.Colour(value=color),
                                      title="Ha lul")

        await self.bot.say(embed=BeeScript)


def setup(bot):
    bot.add_cog(ShitPosts(bot))