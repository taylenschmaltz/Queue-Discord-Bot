from discord.ext import commands
from discord import utils
import discord
import asyncio
import random
import math
import time
from random import choice


bot = commands.Bot(command_prefix = "!")
client = discord.Client()



class queue(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.qcount = 0
        self.total = []
        self.mention = []
         

    @commands.command()
    async def q(self, ctx):
        if self.qcount < 6:
           self.total
           self.mention
           guild = ctx.guild

           if ctx.author.mention in self.mention:
            await ctx.send('You\'re already queued.')
            return
           else: 
             #checking if the channel id matches the id allowed.
            if ctx.channel.id == 818292898067382297:
             self.qcount += 1
             await ctx.send('Added to the queue!' + ' ' + f'{ctx.author.mention}')
             #adds users to the queue
             self.total.append(ctx.author)
             self.mention.append(ctx.author.mention)
             if self.qcount == 6:

               #Takes the teams and shuffles, then splits into two teams.
               random.shuffle(self.total)
               blue = self.mention[:3]
               orange = self.mention [3:6] 
               blueDM = self.total[:3]
               orangeDM = self.total [3:6]
               #set p to equal a random user in the queue
               p = random.choice(self.total)
               username = str((random.randint(1,9999)))
               password = str((random.randint(1,9999)))

               #Embedded info via dms
               HostEmbed = discord.Embed(
                 title = '6Mans',
                 description = 'You\'re the host so create the lobby and let the other team know once the lobby is up.\n ' + '**Lobby Name:**  OU' + username + '\n' + '**Password:** OU' + password,
                 colour = discord.Colour.green()
               )

               BlueEmbed = discord.Embed(
                 title = '6Mans',
                 description = '**Host:** ' + f'{p}\n' + 'You\'re on the blue team, please keep an eye on the 6mans channel for an update from the host as to when the lobby is up.\n' + '**Lobby Name:** OU ' + username + '\n' + '**Password:** OU' + password,
                 colour = discord.Colour.blue()
               )

               OrangeEmbed = discord.Embed(
                 title = '6Mans',
                 description = '**Host:** ' + f'{p}\n' + 'You\'re on the orange team, please keep an eye on the 6mans channel for an update from the  host as to when the lobby is up.\n' + '**Lobby Name:** OU' + username + '\n' + '**Password:** OU' + password,
                 colour = discord.Colour.orange()
               )

               #dm a random person to be the host + dm other members the lobby info

               await p.send(embed = HostEmbed)
               
               for i in blueDM:
                 await i.send(embed = BlueEmbed)

               for i in orangeDM:
                 await i.send(embed = OrangeEmbed)

               #tags the users when queue is ready
               await ctx.send('Queue is ready, view the teams below. Check your DMs for lobby info.')

               #Voice Channels Created
               overwrites = {
                guild.default_role: discord.PermissionOverwrite    (read_messages=True),
                guild.me: discord.PermissionOverwrite(read_messages=True)
               }
               teamNumber = (random.randint(1,999))
               blueVoice = await guild.create_voice_channel('Blue Team' + ' ' +    str (teamNumber), user_limit = 3, overwrites=overwrites)
               orangeVoice = await guild.create_voice_channel('Orange Team' + ' '    +   str(teamNumber), user_limit = 3,overwrites=overwrites) 

               #Embedded Teams Info
               embed1 = discord.Embed(
                 title = 'Blue Team',
                 description = 'Your voice channel is: ' + str(blueVoice) + '\n'   +   f'{blue}',
                 colour = discord.Colour.blue()
               )
               await ctx.send(embed=embed1)
               embed2 = discord.Embed(
                 title = 'Orange Team',
                 description = 'Your voice channel is: ' + str(orangeVoice) +  '\n'   + f'{orange}',
                 colour = discord.Colour.orange()
               )

               await ctx.send(embed=embed2)

               #Queue resets, voice channels get deleted
               await ctx.send('Setting up the next queue, please wait 5 seconds.')
               await asyncio.sleep(3)
               self.total.clear()
               await asyncio.sleep(3)
               self.qcount = 0

               await asyncio.sleep(3400)
               await blueVoice.delete()
               await orangeVoice.delete()
        else:
            await ctx.send('Please wait a few seconds before trying to queue.')
            await asyncio.sleep(3)
            self.total.clear()
            self.mention.clear()
            await asyncio.sleep(3)
            self.qcount = 0      
        return 

    @commands.command()
    async def leave(self, ctx):
      if len(self.total) > 1:
       if ctx.author.mention in self.mention:
         self.total.remove(ctx.author)
         self.mention.remove(ctx.author.mention)
         await ctx.send('You\'ve left the queue.')
         self.qcount -= 1
      elif len(self.total) == 1:
        if ctx.author.mention in self.mention:
          self.total.remove(ctx.author)
          self.mention.remove(ctx.author.mention)
          await ctx.send('You\'ve left the queue.')
          self.total = []
          self.mention = []
          self.qcount = 0
      #elif len(self.total) > 1:    
        #if ctx.author.mention in self.mention:
          #self.total = self.total.remove(ctx.author)
          #self.mention = self.mention.remove(ctx.author.mention)
          #await ctx.send('You\'ve left the queue.')
      else: 
        await ctx.send('You\'re not in the queue.')
        return

    @commands.command()
    async def status(self, ctx):
      if self.total == None:
        await ctx.send('The queue is empty.')
        self.total = []
        self.mention = []
        self.qcount = 0
      elif len(self.total) > 0:
        StatusEmbed = discord.Embed(
          title = '6Mans Status',
          description = 'View the current queue below: \n' + f'{self.mention}',
          colour = discord.Colour.gold()
        )
        await ctx.send(embed = StatusEmbed)
        return
      elif self.total == 0:
        await ctx.send('The queue is empty.')
        return

    @commands.command()
    async def commands(self, ctx):
      HelpEmbed = discord.Embed(
        title = '6Mans Commands',
        description = '**Prefix:** ! \n' + '**q:** Adds you to the queue. \n' + '**leave:** Removes you from the queue. \n' + '**status:** Displays who\'s in the queue.',
        colour = discord.Colour.gold()
        )
      await ctx.send(embed = HelpEmbed)

      



def setup(bot):
  bot.add_cog(queue(bot))


