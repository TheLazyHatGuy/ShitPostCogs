import discord
from discord.ext import commands
from random import choice
import requests
import json

Auth = ('KEY', 'SECRET')
headers = {'Authorization': 'Basic'}

class VidMe():
    """A few commands powered by the VidMe API"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, hidden=True)
    async def VMCheck(self,ctx):
        """Check VidMe API is working"""
        await self.bot.send_typing(ctx.message.channel)
        url = 'https://api.vid.me/auth/check'


        r = requests.post(url, headers=headers, auth=Auth)

        if(r.status_code == 200):
            await self.bot.say("VidMe API is working")
        elif(r.status_code != 200):
            await self.bot.say("Something with VidMe fucked up")
        else:
            await self.bot.say("Something fucked up \n <@117416885871443974> What did you do?")

    @commands.command(pass_context=True)
    async def VMRandom(self,ctx):
        """Find a random video from VidMe"""
        await self.bot.send_typing(ctx.message.channel)
        url = 'https://api.vid.me/video/random'
        r = requests.get(url, headers=headers, auth=Auth)

        GetVid = r.text
        Parsedvid = json.loads(GetVid)

        DisplayName = Parsedvid['video']['user']['displayname']
        print ("Display Name - ",DisplayName)
        UserName = Parsedvid['video']['user']['username']
        print ("User Name - ",UserName)
        VidName = Parsedvid['video']['title']
        print ("Video Name - ",VidName)
        VidUrl = Parsedvid['video']['full_url']
        print ("Video URL - ",VidUrl)
        VidImage = Parsedvid['video']['thumbnail_url']
        print("Video Image - ", VidImage)

        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        toembed = discord.Embed(
            colour=discord.Colour(value=color),
            author="Random VidMe Video",
            icon_url='https://github.com/TheLazyHatGuy/VidMe.Py/raw/master/vidme_logos/logo_light_bg_powered_by.png')
        toembed.add_field(name="Video Name", value=VidName)
        toembed.add_field(name="Uploaded by", value=DisplayName)
        toembed.add_field(name="Video URL", value=VidUrl)
        toembed.set_footer(text="A cog created by TheLazyHatGuy. Powered by VidMe")
        toembed.set_thumbnail(url=VidImage)
        await self.bot.say(embed=toembed)

def setup(bot):
    bot.add_cog(VidMe(bot))