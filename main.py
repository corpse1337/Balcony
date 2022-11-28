import imghdr
import os
import sys
import asyncio
import random
import re
import discord
from discord.ext import commands
from discord import app_commands
import aiohttp
import httpx
#discord.utils.setup_logging()
import traceback
import os
#os.system("pip install psutil")
import json
import jishaku
import asyncio, random, time, psutil
import os
import websv
from websv import keep_alive
from datetime import datetime
import datetime as datetime
from datetime import date
os.system("pip install date")
import time

#os.system("pip install wavelink")
import wavelink

#from discord_ui import UI, LinkButton, Button
#os.system("pip install git+https://github.com/NotHerHacker/discord.py")

os.system("clear")

def get_prefix(client, message): 
    role = discord.utils.get(message.guild.roles, id=1039182682044780564)
    nopref = message.guild.get_role(noprefix)
    member = message.author
    if role in member.roles or nopref in member.roles:
   # if member.id == 921357941725093889:
      return (["-", "*","+", ".", ";", "?", ""])
    elif member.id == 960004669109846046:
      return (["-", "*",";", ".", ">", "?", ""])
   # elif message.author.id == 799927959569956904:
  #    return ""
   # elif message.author.id == 921357941725093889:
    #  return ""
    return (["-", "*","+", ".", ">", ";"])

prefix = ";"
pforp = False
intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix,
                      intents=intents,
                      case_insensitive=True)
client.remove_command('help')
#client.load_extension('jishaku')
client.owner_ids=[960004669109846046]
headers = {"Authorization": "token"}

async def corpse():
  await client.load_extension("jishaku")
asyncio.run(corpse())

os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"



#####sexmoke-ke-b00bs####

modemo = "<:SD_black_icons_vip:1038458070692528159>"
utiemo = "<:icons_loading:1038658107166957709>"
vanrlemo = "<:icons_ping:1038657792988422215>"
autorlemo = "<:dark_a:1038656702184173568>"
loggingemo = "<:icons_list:1038657884470399038>"
antinukeemo = "<:icons_ban:1038658008743432242>"
cross = "<:stolen_emoji:1038421649701212180>"
tick = "<:stolen_emoji:1038421762553155625>"
reply2 = "<:mn_reply:1041281064758419527>"
reply1 = "<:reply:1038822076372488302>"
loading = 123
teamid = 1033959368196112425
svvanity = "nuker"
staremo = "<a:StarBlackStar:1038477202850861116>"
guildnm = "corpse"
guildid = 940271171415461898
noprefix = 1039182682044780564
txtid = 1033959401310146560
modid = 1033959366296076328
picid = 1033959402576822272
cmdid = 1033959403562479666
anncnm = "psa"
annclk = False
anncbyp = 1038494716670517299
rulesid = 1033959392678268958
vanvc = 1038033047179763712
fanrole = 1033959372277174272
wallrole = 1033959348289937578
modlogs = 1033959416015368262
girlrole = 1033959371408932904
boostrole = 940635154404233327
ghufiplayzid = 960004669109846046
ghufiplayzaltid = 1032960549916516384
darkholdid = 1032960549916516384
pfpschn = 1038453656850280529
admid = 1033959344817045504
admrole = 1033959349103628308
color = 0x2f3136
welcid = 1033959391726149652
vanityxd = "/nuker"
statusxd = "Algorithm"
vanch = 1038033047179763712




@client.event
async def on_ready():
   # channel = client.get_channel(vanch)
    #await channel.connect()
    print(f"\033[92m Connected {client.user} ; {client.user.id}")

  
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=statusxd))




#####cmd-error#####



##imagine cmd error hi error kar raha#######



##HELP-CMD######



class Dropdown(discord.ui.Select):
    def __init__(self):
        


        
        options = [
            discord.SelectOption(label='Moderation', description='Commands Of Moderation', emoji=modemo),
            discord.SelectOption(label='Utility', description='Commands Of Utility', emoji=utiemo),
            discord.SelectOption(label='Vanity Roles', description='Commands Of Vanity Roles', emoji=vanrlemo),

            discord.SelectOption(label='AutoRole', description='Commands Of Autorole', emoji=autorlemo),

            discord.SelectOption(label='Logging', description='Commands Of Logging setup', emoji=loggingemo),
            discord.SelectOption(label='AntiNuke', description='Commands of AntiNuke', emoji=antinukeemo)
        ]
        super().__init__(placeholder='Select!', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Moderation":
          embed = discord.Embed(title=f"{modemo} {self.values[0]} Commands", description="`ban`, `unban`, `kick`, `warn`, `mute`, `unmute`, `auditlog`, `roleall`, `addrole`, `removerole`, `lockall`, `unlockall`, `lock`, `unlock`, `hide`, `unhide`, `nuke`, `unbanall`, `purge`, `vcmute`, `vcunmute`, `vcdeafen`, `vcundeafen, `pin`, `unpin`, `delmsg`", color=color)
          await interaction.response.send_message(embed=embed)
        elif self.values[0] == "Utility":
          embed = discord.Embed(title=f"{utiemo} {self.values[0]} Commands", description="`userinfo`, `serverinfo`, `status`, `membercount`, `av`, `banner`, `steal`, `roleinfo`, `afk`, `ping`", color=color)
          await interaction.response.send_message(embed=embed)
        elif self.values[0] == "AutoRole":
          embed = discord.Embed(title=f"{autorlemo} {self.values[0]} Commands", description="`autorole humans add`, `autrole bots add`, `autorole humans remove`, `autorole bots remove`, `autorole config`", color=color)
          await interaction.response.send_message(embed=embed)
        elif self.values[0] == "Vanity Roles":
          embed = discord.Embed(title=f"{vanrlemo} {self.values[0]} Commands", description="`vrsetup`, `vrconfig`, `vrremove`", color=color)
          await interaction.response.send_message(embed=embed)
        elif self.values[0] == "logging":
          embed = discord.Embed(title=f"{loggingemo} {self.values[0]} Commands", description="`logset`, `logremove`, `logconfig`", color=color)
          await interaction.response.send_message(embed=embed)
        elif self.values[0] == "AntiNuke":
          emu = discord.Embed(title=f"{antinukeemo} {self.values[0]} Commands", description="`Under Development`")
          await interaction.response.send_message(embed=emu)

          

class dropdown(discord.ui.View):
  def __init__(self, *, gaeness=100):
     super().__init__(timeout=gaeness)
     self.add_item(Dropdown())
     self.response = None

  async def on_timeout(self):
    for child in self.children:
      child.disabled = True
    await self.response.edit(view=self)







@client.command(aliases=["h"])
async def help(ctx):
  view = dropdown()
  bal = discord.Embed(title=f"Help Panel", description=f"<:ReplyHLR:1038822348222103612> Prefix -`.`, `?`, `*`, `>`, `-`\n\n<:ReplyHLR:1038822348222103612> **Catagories**\n<:reply:1038822076372488302> <:SD_black_icons_vip:1038458070692528159> : Moderation\n<:reply:1038822076372488302> <:icons_loading:1038658107166957709> : Utility\n<:reply:1038822076372488302> <:icons_ping:1038657792988422215> : Vanity Roles\n<:reply:1038822076372488302> <:dark_a:1038656702184173568> : Autorole\n<:reply:1038822076372488302> <:icons_list:1038657884470399038> : Logging\n{reply} <:icons_ban:1038658008743432242> : AntiNuke", color=color)
  bal.set_thumbnail(url=ctx.guild.icon.url)
  bal.set_footer(text=f"/{svvanity} | developer - corpse", icon_url=ctx.author.avatar.url)


  r=await ctx.reply(embed=bal, view=view, mention_author=False)
  view.response = r
  
  




  


#Welc######



@client.listen("on_member_join")
async def huehuejoin(member):
  guild = member.guild
  chat = guild.get_channel(txtid)
  haj = len(guild.members)

  embed = discord.Embed(color=0x2f3136, description=f"""
**Hey {member.mention}, Welc to Corpse**""")  
  embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.avatar.url)
  embed.set_thumbnail(url=guild.icon.url)
  #embed.set_image(url="https://media.discordapp.net/attachments/998850519302938624/1013438484163334214/GIF-220828_172244.gif")
  embed.set_footer(text=f"Now we have {haj} homies.", icon_url=guild.icon.url)
  await chat.send(content=f"{member.mention}", embed=embed)


@client.listen("on_member_join")
async def huehuejoin2(member):
  guild = member.guild
  chat = guild.get_channel(welcid)
  await chat.send(f"{member.mention}, Welc to corpse")

@client.event
async def on_message(message):

  await client.process_commands(message)

  
  
  channel = message.channel
  member = message.author
  guild = message.guild 
  btw = guild.get_channel(txtid)


  if "MessageType.premium_guild" in str(message.type):
    achay = "**{}, just boosted the server!**".format(member.mention)
    await btw.send(achay)
    wogyto = "Thanks for boosting the server, {}.".format(member.mention)
    try:
      await message.reply(wogyto)
    except:
      await channel.send(wogyto)



@client.command()
@commands.has_permissions(administrator=True)
async def hautoroleadd(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role:
    await ctx.reply(f"{cross} | You Must Have Role Above Me To Use This command.**")
    return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if str(role.id) in omk['humanautoroles']:
      await ctx.reply(f"{cross} | That Role Is Already Set In Human Autoroles.**")
      return
    else:
      ff[str(ctx.guild.id)]['humanautoroles'].append(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(f"{tick} | Added **{role.name}** To My Autoroles Algorithm.")

@client.command()
async def ping(ctx):
    embed = discord.Embed(color=0x2f3136, 
        title="Ping!",
        description=
        f"**`{int(client.latency * 1000)}ms`**")
    embed.set_thumbnail(
        url=
        ctx.guild.icon.url
    )
    await ctx.reply(embed=embed)

###server info ki maa ka bosda####

@client.command(aliases=["si"])
async def serverinfo(ctx):
  guilduwu = ctx.guild
  memberc = len(guilduwu.members)
  #bomts = member.bot
  botc = len(guilduwu.members)
  verf = str(ctx.guild.verification_level)
  #so = client.get_guild(int(guilduwu))
 # idk = await so.vanity_invite()
  #vanityinv = guilduwu.vanity.url
  emo = len(ctx.guild.emojis)
  era = ctx.guild.created_at.strftime('%B %d, %Y %I:%M %p')
  boostc = ctx.guild.premium_subscription_count
  boostlvl = ctx.guild.premium_tier
  fea = ', '.join(ctx.guild.features).replace('_', " ")
  toprol = ctx.guild.roles[-1]
  rolec = len(ctx.guild.roles)
  svown = ctx.guild.owner
  guildnmxd = ctx.guild.name
 # guildidxd = ctx.guild.id
  textch = len(ctx.guild.text_channels)
  voicech = len(ctx.guild.voice_channels)
  allch = textch + voicech
 # splash = ctx.guild.splash.url
  bnr = ctx.guild.banner.url
  icon = ctx.guild.icon.url

  ok = discord.Embed(description=f"**{guildnmxd}**\n{reply1} **Owner: {svown.name}** (`{svown.id}`) {svown.mention}\n{reply1} **Created:** {era}\n\n**Members**\n{reply1} **humans:** {memberc}\n{reply1} **bots:** {botc}\n\n**General**\n{reply1} **verification:** {verf}\n{reply1} **vanity:** /{svvanity}\n\n**Boosts**\n{reply1} **boosts:** {boostc}\n{reply1} **boost lvl:** {boostlvl}\n\n**Channels**\n{reply} **text:** {textch}\n{reply1} **voice:** {voicech}\n{reply1} **all:** {allch}\n\n**Miscellaneous**\n{reply1} **roles:** {rolec}\n{reply1} **top role:** <@&{toprol.id}>\n{reply1} **emoji:** {emo}\n\n**Design**\n[icon]({icon})\n[banner]({bnr})\n[splash]({bnr})\n\n**Features**\n```{fea}```", color=color)
  ok.set_footer(text=f"guild id: {ctx.guild.id}", icon_url=ctx.author.avatar.url)
  ok.set_thumbnail(url=ctx.guild.icon.url)
  ok.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon.url)
  ok.set_image(url=ctx.guild.banner.url)
  await ctx.send(embed=ok)
  
  
  
                          


@client.command(aliases=["ri"])
async def roleinfo(ctx, role: discord.Role = None):
  #h = httpx.get(f"https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={}")
 # k = h.content.decode("utf-8")
 # kk = k.replace('"', '')
  #connect_ = int(kk)
  lund = role.color
  bhery = discord.Embed(title=f"**{role.name}'s Information**", colour=lund)
  perms = ""
  if role.permissions.administrator:
            perms += "Administrator, "
  if role.permissions.create_instant_invite:
            perms += "Create Instant Invite, "
  if role.permissions.kick_members:
            perms += "Kick Members, "
  if role.permissions.ban_members:
            perms += "Ban Members, "
  if role.permissions.manage_channels:
            perms += "Manage Channels, "
  if role.permissions.manage_guild:
            perms += "Manage Guild, "
  if role.permissions.add_reactions:
            perms += "Add Reactions, "
  if role.permissions.view_audit_log:
            perms += "View Audit Log, "
  if role.permissions.read_messages:
            perms += "Read Messages, "
  if role.permissions.send_messages:
            perms += "Send Messages, "
  if role.permissions.send_tts_messages:
            perms += "Send TTS Messages, "
  if role.permissions.manage_messages:
            perms += "Manage Messages, "
  if role.permissions.embed_links:
            perms += "Embed Links, "
  if role.permissions.attach_files:
            perms += "Attach Files, "
  if role.permissions.read_message_history:
            perms += "Read Message History, "
  if role.permissions.mention_everyone:
            perms += "Mention Everyone, "
  if role.permissions.external_emojis:
            perms += "Use External Emojis, "
  if role.permissions.connect:
            perms += "Connect to Voice, "
  if role.permissions.speak:
            perms += "Speak, "
  if role.permissions.mute_members:
            perms += "Mute Members, "
  if role.permissions.deafen_members:
            perms += "Deafen Members, "
  if role.permissions.move_members:
            perms += "Move Members, "
  if role.permissions.use_voice_activation:
            perms += "Use Voice Activation, "
  if role.permissions.change_nickname:
            perms += "Change Nickname, "
  if role.permissions.manage_nicknames:
            perms += "Manage Nicknames, "
  if role.permissions.manage_roles:
            perms += "Manage Roles, "
  if role.permissions.manage_webhooks:
            perms += "Manage Webhooks, "
  if role.permissions.manage_emojis:
            perms += "Manage Emojis, "

  if perms is None:
            perms = "None"
  else:
            perms = perms.strip(", ")
          
  bhery.add_field(name='**General info:**', value=f"Name: {role.name}\nId: {role.id}\nPosition: {role.position}\nHex: {role.color}\nMentionable: {role.mentionable}\nCreated At: <t:idk:D>\nManaged by Integration: {(role.managed)}\n\nPeople in this role: {(len(role.members))}\n\n**Allowed Permissions:**\n```{perms}```")
  bhery.set_thumbnail(url=role.icon)
  bhery.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar.url)
  await ctx.reply(embed=bhery, mention_author=False)




  




@client.command(aliases=["annclk"])
@commands.has_permissions(administrator=True)
@commands.guild_only()
async def annclock(ctx, btw):
  guild = ctx.guild
  lund = discord.utils.get(guild.channels,name=anncnm)
  global annclk
  if btw == "True" or btw == "true":
    bhay = discord.Embed(title="Psa Lockdown Information", description=f"**Information:**\n• While annclock algorithm is active, you can't send messages in <#{lund.id}>.\n• Sending messages while having administrator permission leads to removing of admin role.\n• You can't nuke <#{lund.id}>.", color=color)
    bhay.set_thumbnail(url=ctx.guild.icon.url)
    bhay.set_footer(text=f"Action Issued by {ctx.message.author.name}#{ctx.message.author.discriminator}", icon_url=ctx.author.avatar.url)
    await lund.send (f"{tick} | Action Issued, Psa lockdown Algorithm Enabled.", embed=bhay)
    annclk = True
  elif btw == "False" or btw == "false":
      await lund.send(f"{tick} | Successfully disabled Psa Lockdown Algorithm")
      annclk = False


####under dev###

@client.event
async def on_message(message):
  await client.process_commands(message)
  channel = message.channel
  member = message.author
  guild = message.guild 
  adnrol = discord.utils.get(guild.roles, id=admrole)
  byprol = discord.utils.get(guild.roles, id=anncbyp)
  if annclk == True:
   if channel == "psa":
     if member.guild_permissions.administrator: 
       if member.bot:
          return
       try:
         await member.send("Your roles have been removed because you sent a message in Psa.")
         await member.remove_role(adnrol, reason="sent message in annclk mode")
         await member.remove_role(byprol, reason="sent message in annclk mode")
       except:
        await member.send("Don't send messages in psa while annclk is active.")


@client.command(aliases=["credits"])
async def developer(ctx):
  em = discord.Embed(description=f"**__Developer's Information:__**\n\n**Developer:** [Corpse](https://discord.com/users/{ghufiplayzid})\nAll the algorithms used in the bot are solely made for the purpose of testing, and hold the copyright of dev", color=color)
  em.set_footer(text=f"GhufiPlayZ :)", icon_url=ctx.guild.owner.avatar.url)
  em.set_thumbnail(url=ctx.guild.owner.avatar.url)
  await ctx.send(embed=em)

#####

@client.command(aliases=["pinmsg", "msgpin"])
@commands.has_permissions(administrator=True)
@commands.guild_only()
@commands.cooldown(1, 30, commands.BucketType.user)
async def pin(ctx):
  modw = ctx.guild.get_role(modid)
  if modw in ctx.message.author.roles:
    msg = int(ctx.message.reference.message_id)
    h = httpx.put(f"https://discord.com/api/v9/channels/{ctx.channel.id}/pins/{msg}", headers={'Authorization': f'Bot {token}', 'X-Audit-Log-Reason': f"Action issued by {ctx.message.author}."})
    if h.status_code == 204:
      await ctx.reply(f"{tick} | Successfully pinned the message.", mention_author=False)
      return
    await ctx.reply(f"{cross} | Failed to pin the message.", mention_author=False)
    return
  await ctx.reply(f"{cross} | You don't have the permission to use this command.", mention_author=False, delete_after=14)

@client.command(aliases=["unpinmsg", "msgunpin"])
@commands.has_permissions(administrator=True)
@commands.guild_only()
@commands.cooldown(1, 30, commands.BucketType.user)
async def unpin(ctx):
  modw = ctx.guild.get_role(modid)
  if modw in ctx.message.author.roles:
    msg = int(ctx.message.reference.message_id)
    h = httpx.delete(f"https://discord.com/api/v9/channels/{ctx.channel.id}/pins/{msg}", headers={'Authorization': f'Bot {token}', 'X-Audit-Log-Reason': f"Action issued by {ctx.message.author}."})
    if h.status_code == 204:
      await ctx.reply(f"{tick} | Successfully unpinned the message.", mention_author=False)
      return
    await ctx.reply(f"{cross} | Failed to unpin the message.", mention_author=False)
    return
  await ctx.reply(f"{cross} | You don't have the permission to use this command.", mention_author=False, delete_after=14)

@client.command(aliases=["delmsg", "msgdel", "del"])
@commands.has_permissions(administrator=True)
@commands.guild_only()
@commands.cooldown(1, 5, commands.BucketType.user)
async def deletemessage(ctx):
  modw = ctx.guild.get_role(modid)
  logc = ctx.guild.get_channel(modlogs)
  c = ctx.channel.id
  if modw in ctx.message.author.roles:
    if c == txtid or c == picid or c == cmdid:
      msg = int(ctx.message.reference.message_id)
      
        # 
      h = httpx.delete(f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages/{msg}", headers={'Authorization': f'Bot {token}', 'X-Audit-Log-Reason': f"Action issued by {ctx.message.author}."})
      if h.status_code == 204:
        
        await ctx.send(f"{tick} | {ctx.message.author} Successfully deleted the message.", mention_author=False, delete_after=3)
        await ctx.message.delete()
        await logc.send(f"{ctx.message.author} deleted a message.")
        return
      await ctx.reply(f"{cross} | Failed to delete the message.", mention_author=False, delete_after=3)
      return
    await ctx.reply(f"{cross} | This channel is restricted from message deletions.", mention_author=False, delete_after=14)
    return
  await ctx.reply(f"{cross} | You don't have the permission to use this command.", mention_author=False, delete_after=14)


@client.command(aliases=["screenshot"])
@commands.guild_only()
async def ss(ctx, *, arabhay):
     embed = discord.Embed(title=f"{guildnm}", color=color)
     embed.set_footer(text="Screenshot")
     embed.set_image(url=f"https://image.thum.io/get/{arabhay}")
     await ctx.reply(embed=embed, mention_author=False)





      
#####Channel-Nuke####


@client.command()
@commands.has_permissions(administrator=True)
@commands.guild_only()
async def nuke(ctx, channel: discord.TextChannel = None):
    if annclk == True:
     await ctx.reply(f"{cross} | Action Rejected, Psa Lockdown Mode is enabled.")
     return None
    guild = ctx.guild
    semx = discord.utils.get(guild.roles, id=admid)
    lund = discord.utils.get(guild.channels,name=anncnm)
    nuke_channel = ctx.channel
    if nuke_channel.name != anncnm:
       await ctx.reply(f"{cross} | Action Rejected, you can only clone <#{lund.id}>")
    else: 
       if semx in ctx.message.author.roles:

          await ctx.reply(f"initiating Nuking.....")         

          new_channel = await nuke_channel.clone(reason=f"Channel nuke issued by {ctx.message.author.name}#{ctx.message.author.discriminator}")
          await nuke_channel.delete()
          embed = discord.Embed(color=color)
          embed.set_footer(text=f"Channel Nuked by {ctx.message.author.name}#{ctx.message.author.discriminator} | corpse")
          embed.set_image(url="https://images-ext-1.discordapp.net/external/B1An4_20rZHhufb1TGEwsthAM5Y0nmlJdmF4YOTCqwE/%3Fsize%3D1024/https/cdn.discordapp.com/banners/940271171415461898/a_3dc8d9d270a8bd831862cbce624f85e8.gif?width=432&height=240")
          await new_channel.send(embed=embed)




@client.command(aliases=['rolecreate'])
@commands.has_permissions(
    manage_roles=True)
async def create_role(ctx, *, name):
    guild = ctx.guild
    await guild.create_role(name=name)
    await ctx.send(f'{tick} | SuccessFully Created Role `{name}`')

@client.command(aliases=['roledel'])
@commands.has_permissions(
    manage_roles=True)
async def delete_role(ctx, *, name):
    omk = discord.utils.get(ctx.guild.roles, id=name.id)
    guild = ctx.guild
    await guild.delete_role(omk)
    await ctx.send(f'{tick} | SuccessFully Deleted Role `{name}`')

@client.command()
async def serverbanner(ctx):
    embed = discord.Embed(title=guildnm, color=color)
    embed.set_image(url=ctx.guild.banner.url)
    embed.set_footer(text=f"Request: {ctx.author} | {guildname}")
    await ctx.reply(embed=embed)

@client.command(aliases=['icon', 'svicon'])
async def servericon(ctx):
    embed = discord.Embed(title=guildnm, color=color)
    embed.set_image(url=ctx.guild.icon.url)
    embed.set_footer(text=f"Request: {ctx.author} | {guildnm}")
    await ctx.reply(embed=embed)

def reload_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)
@client.command()
async def restart(ctx):
    if ctx.author.id == ghufiplayzaltid or ghufiplayzid:
      await ctx.reply(f"restarting........")
      reload_bot()
    else:
      return


@client.command(aliases=["massunban"])
@commands.has_permissions(administrator=True)
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.send('Successfully Unbanning {} Members'.format(len(banlist)))
    for users in banlist:
        await ctx.guild.unban(user=users.user, reason=f"Mass Unban By {ctx.author}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def vcdeafen(ctx, user: discord.Member, * , reason=None):
        await ctx.send(f"{tick} | {user.display_name} has been deafened, for: {reason}")
        await user.edit(deafen = True)

@client.command(aliases=["vmute"])
@commands.has_permissions(manage_messages=True)
async def vcmute(ctx, member: discord.Member, * , reason=None):
        await ctx.send(f"{tick} | {member.display_name} has been muted, for: {reason}")
        await member.edit(mute = True)

@client.command()
@commands.has_permissions(manage_messages=True)
async def vcunmute(ctx, member: discord.Member):
        await ctx.send(f"{tick} | {member.display_name} has been unmuted.")
        await member.edit(mute = False)

@client.command()
@commands.has_permissions(manage_messages=True)
async def vcundeafen(ctx, member: discord.Member):
        await ctx.send(f"{tick} | {member.display_name} has been undeafened.")
        await member.edit(deafen = False)


@client.command(aliases=["log", "logs", "audit", "audit-logs", "audit-log", "auditlogs"])
@commands.has_permissions(view_audit_log=True)
@commands.cooldown(1, 12, commands.BucketType.user)
@commands.guild_only()
async def auditlog(ctx, lmt:int):
  if lmt >= 31:
     await ctx.reply(f"{cross} | Action rejected, you are not allowed to fetch more than `30` entries.", mention_author=False)
     return
  idk = []
  str = ""
  async for entry in ctx.guild.audit_logs(limit=lmt):
    idk.append(f'''User: `{entry.user}`
Action: `{entry.action}`
Target: `{entry.target}`
Reason: `{entry.reason}`\n\n''')
  for n in idk:
       str += n
  str = str.replace("AuditLogAction.", "")
  embed = discord.Embed(title=f"corpse ; audit logs", description=f">>> {str}", color=0x2f3136)
  embed.set_footer(text=f"Audit Log Actions List")
  await ctx.reply(embed=embed, mention_author=False)






###P4P-MODE###JO KISI KAMM KA NHI###
@client.command(aliases=["p4p"])
@commands.guild_only()
async def p4pmode(ctx, arg):
  global pforp 
  if ctx.message.author.id == 799927959569956904 or ctx.message.author.id == ghufiplayzid:
    if arg == "true" or arg == "True":
      await ctx.reply("Confirmation verified, Locking Server......")
      channel = discord.utils.get(ctx.guild.channels, name=txtid)
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channell = discord.utils.get(ctx.guild.channels, name=picid)
      overwrite = channell.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channell.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channelll = discord.utils.get(ctx.guild.channels, name=cmdid) 
      overwrite = channelll.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channelll.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      embed = discord.Embed(title="Information", description="**__General Info:__**\nAny command execution will be rejected, any changes will be instantly reverted, joining users will be kicked, any user joining vc will be banned, any admin sending a message will be banned.\n\n**__Changes:__**\n• Disabled command executions\n• General channels has been locked.\n• Force Locked Wall role hierarchy.", color=color)
      embed.set_footer(text=f"/{svvanity}", icon_url=ctx.guild.icon.url)
      embed.set_author(name=f"{guildnm}")
      await ctx.reply(content=f"{tick} | Successfully Enabled P4P mode.", embed=embed)
      pforp = True
    elif arg == "false" or arg == "False": 
      channel = discord.utils.get(ctx.guild.channels, name=txtid)
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channell = discord.utils.get(ctx.guild.channels, name=picid)
      overwrite = channell.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channell.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      channelll = discord.utils.get(ctx.guild.channels, name=cmdid) 
      overwrite = channelll.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channelll.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
      await ctx.reply(f"{tick} | P4P mode has been disabled")
      pforp = False
  else:
    if arg == "true" or arg == "True":
        await ctx.send("Unauthorised!")


@client.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel: discord.TextChannel = None):
  if channel is None:
    channel = ctx.message.channel
    try:
      await ctx.channel.set_permissions(ctx.guild.default_role,
                                        view_channel=False)
      await ctx.send(f"{tick} | <#{channel.id}> is now invisible from everyone")
    except:
      await ctx.send(f"{cross} | Action rejected, unable to hide")


@client.command()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel: discord.TextChannel = None):
  if channel is None:
    channel = ctx.message.channel
  await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=True)
  await ctx.send(f"{tick} | <#{channel.id}> is now visible from everyone")


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
  if channel == None:
    channel = ctx.message.channel
  await ctx.channel.set_permissions(
    ctx.guild.default_role,
    overwrite=discord.PermissionOverwrite(send_messages=False))
  await ctx.send(f"{tick} | Successfully Locked <#{channel.id}>")

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
  if channel == None:
    channel = ctx.message.channel
  await ctx.channel.set_permissions(
    ctx.guild.default_role,
    overwrite=discord.PermissionOverwrite(send_messages=True))
  await ctx.send(f"{tick} | Successfully Unlocked <#{channel.id}>")


###under dev##

import humanfriendly

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member = None, time = None):
  if member == None:
    await ctx.send(f"{cross} | Action rejected, mention a user")
  elif time == None:
    await ctx.send(f"{cross} | Action rejected, give a proper time")
  else:
    time = humanfriendly.parse_timespan(time)
  try:
    await member.edit(timeout=discord.utils.utcnow() +
                      datetime.timedelta(seconds=time),
                      reason=f"Timeout Given By {ctx.author}")
    await ctx.send(f"{tick} | {member.mention} is muted for **{time}s**")
  except:
    await ctx.send(f"{cross} | Action rejected, missing permissions")

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, mem: discord.Member = None):
  if mem == None:
    await ctx.send()
  else:
    await mem.edit(timeout=None)
    await ctx.send(f"{tick} | Successfully removed timeout from {mem.mention}")

###

@client.command(aliases=["ar", "ra"])
@commands.has_guild_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
  guild = ctx.guild
  if guild.me.top_role >= ctx.author.top_role:
    await ctx.send(f"{cross} | Succesfully Added {role.name} to {member.mention}")
    return
  if member.top_role >= ctx.author.top_role:
      await ctx.send()
  else:
    await member.add_roles(role)
    await ctx.send(f"{tick} | Succesfully Added {role.name} to {member.mention}")


####role####
@client.command(aliases=["red", "black", "blue", "green", "white", "yellow", "selfroles", "self"])
@commands.cooldown(1, 12000, commands.BucketType.user)
@commands.guild_only()
async def selfrole(ctx):
  member = ctx.message.author
  r = member.roles
  g = ctx.guild
  msg = ctx.message.content.lower()
  if "self" in msg:
    em = discord.Embed(color=0x2f3136, title="Corpse", description=">>> `red`, `black`, `blue`, `green`, `white`, `yellow`")
    em.set_footer(text="/{} | selfroles".format(svvanity), icon_url=ctx.guild.icon.url)
    await ctx.reply(embed=em, mention_author=False)
  red = discord.utils.get(g.roles, id=1033959349938302977)
  black = discord.utils.get(g.roles, id=1033959352723316766)
  blue = discord.utils.get(g.roles, id=1033959355801944105)
  green = discord.utils.get(g.roles, id=1033959354661089351)
  white = discord.utils.get(g.roles, id=1033959353541206027)
  yellow = discord.utils.get(g.roles, id=1033959351871877170)
  roles = [red, black, blue, green,white, yellow]
  for rxd in roles:
    if rxd in r:
      try:
        await member.remove_roles(rxd)
      except:
        continue
  if "red" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(tick, red.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(red, reason="self roles")
  elif "black" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(tick, black.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(black, reason="self roles")
  elif "blue" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(tick, blue.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(blue, reason="self roles")
  elif "green" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(tick, green.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(green, reason="self roles")
  elif "white" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(tick, white.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(white, reason="self roles")
  elif "yellow" in msg:
    await ctx.reply("{} | Successfully assigned you {}.".format(tick, yellow.mention), allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
    await member.add_roles(yellow, reason="self roles")


@client.command()
@commands.has_permissions(administrator=True)
async def team(ctx, member: discord.Member):
    r = discord.utils.get(ctx.guild.roles, id=1033959368196112425)
    await ctx.send(f"{tick} | Successfully Given **Team** To {member.mention}")
    await member.add_roles(r, reason="Command Used By {}".format(ctx.author))

@client.command()
@commands.has_permissions(administrator=True)
async def rmteam(ctx, member: discord.Member):
    r = discord.utils.get(ctx.guild.roles, id=1033959368196112425)
    await ctx.send(f"{tick} | Successfully Removed **Team** from {member.mention}")
    await member.remove_roles(r, reason="Command Used By {}".format(ctx.author))

@client.command(aliases=["vantyrolessetup"])
@commands.has_permissions(administrator=True)
async def vrsetup(ctx, vanity, role: discord.Role, channel: discord.TextChannel):
  with open("vanityroles.json", "r") as f:
    idk = json.load(f)
  if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members:
    await ctx.send(f'{cross} | You cant use roles with administrator/ban/kick members permission.')
  else:
    pop = {"vanity": vanity, "role": role.id, "channel": channel.id}
    idk[str(ctx.guild.id)] = pop
    embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"Vanity: {vanity}\nRole: {role.mention}\nChannel: {channel.mention}")
    
    await ctx.reply(embed=embed, mention_author=False)
  with open('vanityroles.json', 'w') as f:
    json.dump(idk, f, indent=4)

@client.command(aliases=["vantyrolesshow"])
@commands.has_permissions(administrator=True)
async def vrshow(ctx):
  with open("vanityroles.json", "r") as f:
    jnl = json.load(f)
  if str(ctx.guild.id) not in jnl:
    await ctx.reply(f"Setup vanity roles using `;vrsetup`", mention_author=False)
  elif str(ctx.guild.id) in jnl:
    vanity = jnl[str(ctx.guild.id)]["vanity"]
    role = jnl[str(ctx.guild.id)]["role"]
    channel = jnl[str(ctx.guild.id)]["channel"]
    gchannel = client.get_channel(channel)
    grole = ctx.guild.get_role(role)
    embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"**Vanity:** {vanity}\n**Role:** {grole.mention}\n**Channel:** {gchannel.mention}")
    
    await ctx.reply(embed=embed, mention_author=False)

@client.command(aliases=["vantyrolesremove"])
@commands.has_permissions(administrator=True)
async def vrremove(ctx):
  with open("vanityroles.json", "r") as f:
    jnl = json.load(f)
    if str(ctx.guild.id) not in jnl:
      await ctx.reply(f"Setup vanity roles using `;vrsetup`", mention_author=False)
    else:
      jnl.pop(str(ctx.guild.id))
      await ctx.reply(f"{cross} | Removed the vanity roles system from this server.", mention_author=False)
  with open('vanityroles.json', 'w') as f:
    json.dump(jnl, f, indent=4) 

@client.event
async def on_presence_update(before, after):
  with open("vanityroles.json", "r") as f:
    jnl = json.load(f)
  if str(before.guild.id) not in jnl:
    return
  elif str(before.guild.id) in jnl:
    vanity = jnl[str(before.guild.id)]["vanity"]
    role = jnl[str(before.guild.id)]["role"]
    channel = jnl[str(before.guild.id)]["channel"]
    if str(before.raw_status) == "offline":
      return
    else:
      aft = after.activities[0].name
      bef = before.activities[0].name
      if vanity in aft:
        try:
          if vanity not in bef:
            gchannel = client.get_channel(channel)
            grole = after.guild.get_role(role)
            await after.add_roles(grole, reason="- added vanity in status")
            await gchannel.send(f"> {after.mention}, Thanks for repping {vanity} <3")
          elif vanity in bef:
            return
        except:
          pass
      elif vanity not in aft:
        if vanity in bef:
          try:
            gchannel = client.get_channel(channel)
            grole = after.guild.get_role(role)
            await after.remove_roles(grole, reason="- removed vanity from status")
            
          except:
            pass

  #####Role##########

@client.command()
@commands.has_permissions(administrator=True)
async def role(ctx, hue, role:discord.Role):
  if hue == "humans" or hue == "humans":
        await ctx.send(f"{tick} | Adding {role.name} to all humans")

        humans = [mem for mem in ctx.guild.members if not mem.bot]
        for h in humans:
          
            await h.add_roles(role)
          
        await ctx.send(f"{tick} | Successfully given {role.name} to all members")
    
  elif hue == "Bots" or hue == "bots":
     
        await ctx.send(f"{tick} | Adding {role.name} to all bots")


        humans = [mem for mem in ctx.guild.members if mem.bot]
        for ghey in humans:
          
            await ghey.add_roles(role)
          
        await ctx.send(f"{tick} | Successfully given {role.name} to all members")




@client.command()
@commands.has_permissions(administrator=True)
async def rrole(ctx, hue2, role:discord.Role):
  if hue2 == "Humans" or hue2 == "humans":
        await ctx.send(f"<:tecno_tick:1016361996389711912> | Removing {role.name} from all humans!")

        humans = [mem for mem in ctx.guild.members if not mem.bot]
        for h in humans:
            await h.remove_roles(role)
        await ctx.send(f"{tick} | Successfully removed {role.name} from all members!")

  elif hue2 == "Bots" or hue2 == "bots":
        humans = [mem for mem in ctx.guild.members if  mem.bot]
        for h in humans:
            await h.remove_roles(role)
        await ctx.send(f"{tick} | Successfully removed {role.name} from all members!")


@commands.has_permissions(administrator=True)
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def roleall(ctx, *, role: discord.Role):
        num = 0
        failed = 0
        await ctx.send(f"{tick} | Adding roles to all humans & bots")
        for user in list(ctx.guild.members):
          try:
                await user.add_roles(role)
                num += 1
          except Exception:
                failed += 1
        await ctx.reply(f'{tick} | Added roles to all humans & bots')

@client.command()
async def vanity(ctx):
  await ctx.send(f"> <a:StarBlackStar:1038477202850861116> https://discord.gg/{svvanity}")

#@client.command()
#async def rules(ctx):
 # em = discord.Embed(color=0x2f3136, description="<a:StarBlackStar:1038477202850861116> https://discord.com/term\n<a:StarBlackStar:1038477202850861116> https://discord.com/guidelines")
 # await ctx.send(embed=em)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == self.bot:
            await ctx.send('You cannot ban the bot!')
        if ctx.author.top_role.position > member.top_role.position or ctx.author == ctx.guild.owner:
            await member.ban(reason=reason)
            emu = discord.Embed(description=f"{tick} **{member.display_name}** has been successfully banned for reason:`{reason}`", color=0x2ecc71)
            await ctx.send(embed=emu)
            await member.send(f"‼️ | You have been banned from **{ctx.message.guild.name}** for reason: {reason}")
        if not ctx.author.top_role.position > member.top_role.position and ctx.author != ctx.guild.owner:
            await ctx.send(f"{cross} | You cannot ban someone with a higher role than you.")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(self, ctx, id: int):
        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"{tick} | **{user.name}** has been successfully unbanned")


guildname = "corpse"
  
######status-utility######

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.guild_only()
async def status(ctx, user:discord.Member=None):
  #if pforp == True:
   #  await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
   #  return None
  if user == None:
    user = ctx.message.author
  off = "offline"
  mob = f"{user.mobile_status}"
  desk = f"{user.desktop_status}"
  web = f"{user.web_status}"
  if mob == off and desk == off and web == off: 
    embed = discord.Embed(title=f"{guildname}", description="Offline / Invisible / Undetected", color=color)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar.url)
    await ctx.reply(embed=embed, mention_author=False)
  elif mob != off and desk != off and web != off: 
    embed = discord.Embed(title=f"{guildname}", description=f"Mobile - {mob}\nBrowser - {web}\nDesktop - {desk}", color=color)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=f"{user.avatar.url}")
    await ctx.reply(embed=embed, mention_author=False)
  elif desk == off and web == off: 
    embed = discord.Embed(title=f"{guildname}", description=f"Mobile - {mob}", color=color)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar.url)
    await ctx.reply(embed=embed, mention_author=False) 
  elif mob == off and desk == off:
    embed = discord.Embed(title=f"{guildname}", description=f"Browser - {web}", color=color)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar.url) 
    await ctx.reply(embed=embed, mention_author=False)
  elif mob == off and web == off: 
    embed = discord.Embed(title=f"{guildname}", description=f"Desktop - {desk}", color=color)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar.url) 
    await ctx.reply(embed=embed, mention_author=False)
  elif desk == off:
    embed = discord.Embed(title=f"{guildname}", description=f"Mobile - {mob}\nBrowser - {web}", color=color)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar.url) 
    await ctx.reply(embed=embed, mention_author=False)
  elif web == off: 
    embed = discord.Embed(title=f"{guildname}", description=f"Mobile - {mob}\nDesktop - {desk}", color=color)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar.url) 
    await ctx.reply(embed=embed, mention_author=False)
  elif mob == off:    
    embed = discord.Embed(title=f"{guildname}", description=f"Browser - {web}\nDesktop - {desk}", color=color)
    embed.set_footer(text=f"{user.name}#{user.discriminator}", icon_url=user.avatar.url) 
    await ctx.reply(embed=embed, mention_author=False)
  else:
    await ctx.reply(f"{cross} | Unable to fetch user.", mention_author=False)

#####anti-vanity-steal#######

vanitycode = "nuker"
sniperid = 973546013354786887
@client.event
async def on_guild_update(before, after):
  reason = "Balcony Secure Algorithm | Server Update"
  guild = after
  corpse = {'code': vanitycode}
  async with aiohttp.ClientSession(headers={'Authorization': f'Bot {token}', 'X-Audit-Log-Reason': 'Changing vanity url is restricted.'}, connector=None) as session:
    async with session.patch(f"https://canary.discord.com/api/v9/guilds/{guild.id}/vanity-url", json=corpse) as r: 
      print(r.status)
    async for logs in guild.audit_logs(limit=10, after=datetime.datetime.now() - datetime.timedelta(seconds = 20)):
      if logs.action == discord.AuditLogAction.guild_update:
        if logs.user.bot or logs.user.id or sniperid or ghufiplayzid:
          continue
        else:
            async with session.put(f"https://canary.discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json={'delete_message_days': 0, 'reason': 'unauthorized changes'}) as chr:
            	print(chr.status)
            await guild.edit(name=f"corpse", verification_level=before.verification_level, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, preferred_locale=before.preferred_locale, rules_channel=before.rules_channel, public_updates_channel=before.public_updates_channel, region=before.region, reason="Balcony | Anti guild update Algorithm")
      else:
        continue

#roleidtogive = 1033959370343583764
#vanity = "/nuker" 
#logging_channel_id = 1033959400307695657


#@client.event
#async def on_member_update(before, after):
  #if str(before.raw_status) == "offline":
  #  return
 # else:
  #  try:
  #   bst = after.activities[0].name
  #   ast = before.activities[0].name
  #   if vanity in bst:
  #     if not vanity in ast:
   #      channel = client.get_channel(logging_channel_id)
   #      role = after.guild.get_role(roleidtogive)
   #      await after.add_roles(role, reason="Added Vanity In Status")
    #     await channel.send(f"> {after.mention}, thanks for repping {vanity} <:cc_black_dollar:997157749320319007> ")
   #  elif vanity in ast:
    #   if not vanity in bst:
    #     channel = client.get_channel(logging_channel_id)
    #     role = after.guild.get_role(roleidtogive)
    #     if role in after.roles:
     #      await after.remove_roles(role, reason="Removed Vanity From Status")
   # except Exception as e:
    #  print(e)


#######Logging info##########

reply = "<:reply:1038822076372488302>"
list = "<:icons_list:1038657884470399038>"
bot_name = "corpse"

        
#### Logging #####
@client.command(aliases=["log-set", "setlog", "setlogs"])
@commands.has_permissions(administrator=True)
async def logset(ctx, channel: discord.TextChannel):
  with open('logsch.json', 'r') as f:
    logs = json.load(f)
    if str(ctx.guild.id) not in logs:
      logs[str(ctx.guild.id)] = str(channel.id)
      await ctx.send(f"**{tick} | Successfully Updated The Logs Channel To {channel.mention}**")
      await channel.send(embed=discord.Embed(color=color, description=f"**{list} This Channel Has Been Added As Logs Channel And All Logs Will Be Shown Here**"))
    elif str(ctx.guild.id) in logs:
      logs[str(ctx.guild.id)] = str(channel.id)
      await ctx.send(f'**<:success:992024105975037992> | Successfully Updated the logs channel to {channel.mention}**', mention_author=False)
      await channel.send(embed=discord.Embed(color=color, description=f"**{list} This Channel Has Been Added As Logs Channel And All Logs Will Be Shown Here!**"))
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)

@client.command(aliases=["log-show", "showlogs", "showlog"])
@commands.has_permissions(administrator=True)
async def logshow(ctx):
  with open ('logsch.json', 'r') as i:
    logs = json.load(i)
    try:
      await ctx.send(f'**{tick} | The Logs Channel For This Server is <#{logs[str(ctx.guild.id)]}>**', mention_author=False)
    except KeyError:
      await ctx.send(f"**{cross} | No Logs Channel Has Been Found In The Server!**", mention_author=False)

@client.command(aliases=["log-remove", "logsremove", " removelog", "removelogs"],)
@commands.has_permissions(administrator=True)
async def logremove(ctx):
  with open('logsch.json', 'r') as f:
    logs = json.load(f)
    if str(ctx.guild.id) not in logs:
      await ctx.send(f"**{cross} | There is No Logs Channel in The Server!**", mention_author=False)
    else:
      logs.pop(str(ctx.guild.id))
      await ctx.send(f"**{tick} | Successfully Removed Logs Channel From The Server!**", mention_author=False)
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)

#lundness#
async def joinlog_event(member):
  with open ('logsch.json', 'r') as i:
    logs = json.load(i)
    if str(member.guild.id) in logs:
      em=discord.Embed(color=discord.Colour(0x2f3136), description=f"{reply} {member} | {member.id}\n{reply} created at: <t:{int(member.created_at.timestamp())}:D>\n{reply} links: [avatar]({member.avatar_url})")
      em.set_thumbnail(url=member.avatar_url)
      em.set_footer(text=f"{bot_name}", icon_url=client.user.avatar.url)
      em.set_author(name="Member joined!", icon_url=client.user.avatar.url)
      logchid = logs[str(member.guild.id)]
      logsch = client.get_channel(int(logchid))
      await logsch.send(embed=em)
    elif str(member.guild.id) not in logs:
      return
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)

async def leavelog_event(member):
  with open ('logsch.json', 'r') as i:
    logs = json.load(i)
    if str(member.guild.id) in logs:
      em=discord.Embed(color=discord.Colour(0x2f3136), description=f"{reply} {member} | {member.id}\n{reply} created at: <t:{int(member.created_at.timestamp())}:D>\n{reply} links: [avatar]({member.avatar_url})")
      em.set_thumbnail(url=member.avatar_url)
      em.set_footer(text=f"{bot_name}", icon_url=client.user.avatar.url)
      em.set_author(name="Member left!", icon_url=client.user.avatar.url)
      logchid = logs[str(member.guild.id)]
      logsch = client.get_channel(int(logchid))
      await logsch.send(embed=em)
    elif str(member.guild.id) not in logs:
      return
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)

async def chcreatelog_event(channel):
  with open ('logsch.json', 'r') as i:
    logs = json.load(i)
    if str(channel.guild.id) in logs:
      em=discord.Embed(color=discord.Colour(0x2f3136), description=f"{reply} #{channel.name} | {channel.id}\n{reply} type: {channel.type}\n{reply} position: {channel.position}")
      em.set_thumbnail(url=client.user.avatar_url)
      em.set_footer(text=f"{bot_name}", icon_url=client.user.avatar.url)
      em.set_author(name="Channel created!", icon_url=client.user.avatar.url)
      logchid = logs[str(channel.guild.id)]
      logsch = client.get_channel(int(logchid))
      await logsch.send(embed=em)
    elif str(channel.guild.id) not in logs:
      return
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)


async def chdellog_event(channel):
  with open ('logsch.json', 'r') as i:
    logs = json.load(i)
    if str(channel.guild.id) in logs:
      em=discord.Embed(color=discord.Colour(0x2f3136), description=f"{reply} #{channel.name} | {channel.id}\n{reply} type: {channel.type}\n{reply} position: {channel.position}")
      em.set_thumbnail(url=client.user.avatar_url)
      em.set_footer(text=f"{guildnm}", icon_url=client.user.avatar.url)
      em.set_author(name="Channel deleted!", icon_url=client.user.avatar.url)
      logchid = logs[str(channel.guild.id)]
      logsch = client.get_channel(int(logchid))
      await logsch.send(embed=em)
    elif str(channel.guild.id) not in logs:
      return
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)

async def rolecrlog_event(role):
  with open ('logsch.json', 'r') as i:
    logs = json.load(i)
    if str(role.guild.id) in logs:
      em=discord.Embed(color=discord.Colour(0x2f3136), description=f"{reply} {role.name} | {role.id}\n{reply} color: {role.color}\n{reply} position: {role.position}")
      em.set_thumbnail(url=client.user.avatar.url)
      em.set_footer(text=f"{guildnm}", icon_url=client.user.avatar.url)
      em.set_author(name="Role created!", icon_url=client.user.avatar.url)
      logchid = logs[str(role.guild.id)]
      logsch = client.get_channel(int(logchid))
      await logsch.send(embed=em)
    elif str(role.guild.id) not in logs:
      return
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)
  
async def roledellog_event(role):
  with open ('logsch.json', 'r') as i:
    logs = json.load(i)
    if str(role.guild.id) in logs:
      em=discord.Embed(color=discord.Colour(0x2f3136), description=f"{reply} {role.name} | {role.id}\n{reply} color: {role.color}\n{reply} position: {role.position}")
      em.set_thumbnail(url=client.user.avatar.url)
      em.set_footer(text=f"{guildnm}", icon_url=client.user.avatar.url)
      em.set_author(name="Role deleted!", icon_url=client.user.avatar.url)
      logchid = logs[str(role.guild.id)]
      logsch = client.get_channel(int(logchid))
      await logsch.send(embed=em)
    elif str(role.guild.id) not in logs:
      return
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)

async def msgdellog_event(message):
  with open ('logsch.json', 'r') as i:
    logs = json.load(i)
    if str(message.guild.id) in logs and message.author.id != client.user.id:
      em=discord.Embed(color=color, description=f"{reply} sent by: {message.author} in {message.channel.mention}\n{reply} content: {message.content}")
      em.set_thumbnail(url=message.author.avatar.url)
      em.set_footer(text=f"{guildnm}", icon_url=client.user.avatar.url)
      em.set_author(name="Message deleted!", icon_url=client.user.avatar.url)
      logchid = logs[str(message.guild.id)]
      logsch = client.get_channel(int(logchid))
      await logsch.send(embed=em)
    elif str(message.guild.id) not in logs:
      return
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)

async def msgeditlog_event(after, before):
  with open ('logsch.json', 'r') as i:
    message = after
    logs = json.load(i)
    if str(message.guild.id) in logs:
      if message.author.bot:
        return
      else:
        em=discord.Embed(color=discord.Colour(0x2f3136), description=f"{reply} sent by: {message.author} in {message.channel.mention}\n{reply} before: {after.content}\n{reply} after: {before.content}")
        em.set_thumbnail(url=message.author.avatar_url)
        em.set_footer(text=f"{guildnm}", icon_url=client.user.avatar.url)
        em.set_author(name="Message edited!", icon_url=client.user.avatar.url)
        logchid = logs[str(message.guild.id)]
        logsch = client.get_channel(int(logchid))
        await logsch.send(embed=em)
    elif str(message.guild.id) not in logs:
      return
  with open('logsch.json', 'w') as f:
    json.dump(logs, f, indent=4)
    



client.add_listener(joinlog_event, 'on_member_join')
client.add_listener(leavelog_event, 'on_member_remove')
client.add_listener(chcreatelog_event, 'on_guild_channel_create')
client.add_listener(chdellog_event, 'on_guild_channel_delete')
client.add_listener(rolecrlog_event, 'on_guild_role_create')
client.add_listener(roledellog_event, 'on_guild_role_delete')
client.add_listener(msgdellog_event, 'on_message_delete')
client.add_listener(msgeditlog_event, 'on_message_edit')


keep_alive()

token = ""


client.run(token, reconnect=True)