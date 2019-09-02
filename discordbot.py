import discord
import asyncio
import openpyxl
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    await client.change_presence(game=discord.Game(name="명령어 수정중", type=1))    



  
        
@client.event
async def on_member_join(member):
    fmt = '{0.mention} 님이 놀이터 테섭에 접속하셨습니다'
    channel = member.server.get_channel("594144519688028172")
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("594144519688028172")
    fmt = '{0.mention} 님이 놀이터 테섭에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))



@client.event
async def on_member_join(member):
    fmt = '#USER ID {0.mention} login, black mesa new Mexico'
    channel = member.server.get_channel("567326501259837441")
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("567326887135936522")
    fmt = '#USER ID {0.mention} logout, black mesa new Mexico'
    await client.send_message(channel, fmt.format(member, member.server))










eccess_token = os.environ["BOT_TOKEN"]
client.run(eccess_token)

