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
        await client.send_message(message.channel, '()!도움 #하프라이프2에 대한 도움말 명령어를 띄웁니다')
        await client.send_message(message.channel, '()!pip list #봇에 임포트 되있는 py파일 목록을 띄웁니다')
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
    if message.content.startswith('!도움'):
        await client.send_message(message.channel, '()!빠루 #빠루가 무엇인지 설명해 드립니다')
        await client.send_message(message.channel, '()!고든 프리맨 #고든 프리맨이 누구인지 설명해 드립니다(잘 알면서.....)')
        await client.send_message(message.channel, '나무위키 밎 위키백과에 없으므로 버기는 빠졌습니다')
        await client.send_message(message.channel, '나무위키 및 위키백과에 없으므로 에어보트는 빠졌습니다')
        await client.send_message(message.channel, '나무위키 및 위키백과에 없으므로 콤바인은 빠졌습니다')
        await client.send_message(message.channel, '()!반시민 #반시민이 뭔지 설명해 드립니다')
    if message.content.startswith('!빠루'):
        await client.send_message(message.channel, 'https://namu.wiki/w/%EC%87%A0%EC%A7%80%EB%A0%9B%EB%8C%80')
    if message.content.startswith('!고든 프리맨'):
        await client.send_message(message.channel, 'https://namu.wiki/w/%EA%B3%A0%EB%93%A0%20%ED%94%84%EB%A6%AC%EB%A7%A8')
    if message.content.startswith('!반시민'):
        await client.send_message(message.channel, '(위키백과)https://ko.wikipedia.org/wiki/%EB%B0%98%EC%8B%9C%EB%AF%BC')
    if message.content.startswith('!pip list'):
        await client.send_message(message.channel, '임포트된 py파일:')
        await client.send_message(message.channel, '1.asyncio 3.4.3')
        await client.send_message(message.channel, '2.discord.py 0.16.12')
        await client.send_message(message.channel, '3.openpyxl 2.6.2')
    if message.content.startswith('욕'):
        await client.send_message(message.channel, '@everyone  {0.author.mention}가 욕을 사용했읍니다 널리널리 알리세요^^')
        
    if message.content.startwuth('!회원가입'):
        addrole("회원")
        

        
    
        
    

        

                

        
  
        



    
    
        
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

