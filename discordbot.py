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
async def on_message(message):
    if message.content.startswith('!소개'):
        await client.send_message(message.channel, '전..미친봇 입니다...!')
        await client.send_message(message.channel, '하프라이프에 대한 도움말을 받습니다')
        await client.send_message(message.channel, '자세한것은 저도 모르니 YT_sken91198#4246에 DM넣어주세요')
    if message.content.startswith('!프리맨에 대해서'):
        await client.send_message(message.channel, '자 프리맨은 우주게이입니다 젠까지 가서 난리를 친거 봤죠?')
        await client.send_message(message.channel, '끼요ㅗㅗㅗㅗㅗㅗㅗ옷(하프라이프2 고든프리맨 인성질중 제 2 악장)')
    if message.content.startswith('!명령어'):
        await client.send_message(message.channel, '()!소개 #이 명령어를 쓰면 고든프리맨이 자신에대해 설명합니다')
        await client.send_message(message.channel, '()!프리맨에 대해서 #이 명령어를 쓰면 고든 프리맨이 누구인지 설명합니다')
        await client.send_message(message.channel, '()!모두 #이 명령어를 쓰면 전체를 호출합니다')
    if message.content.startswith('!모두'):
    	roll = '@everyone {0.author.mention}님이 여러분을 부릅니다!'.format(message)
    	await client.send_message(message.channel, roll)
    if message.content.startswith('ㅎㅇ'):
        await client.send_message(message.channel, ':regional_indicator_h: :regional_indicator_i:')
    if message.content.startswith('벨브와'):
        await client.send_message(message.channel, '스팀(3좀 내라)')
    if message.content.startswith('@everyone 동영상 인데요'):
        await client.send_message(message.channel, '뭔영상임?')
    if message.content.startswith('??'):
        await client.send_message(message.channel, '왜........뭐')
    if message.content.startswith('도대채 무슨일이 벌어지는거야'):
        await client.send_message(message.channel, '두눈으로 직접 봐')
    if message.content.startswith('킹갓'):
        await client.send_message(message.channel, '빠루')

 
                   


      
                
            


        


@client.event
async def on_member_join(member):
    fmt = '#USER ID {0.mention} login, black mesa new Mexico'
    channel = member.server.get_channel("574861796624695300")
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("574861796624695300")
    fmt = '#USER ID {0.mention} logout, black mesa new Mexico'
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

