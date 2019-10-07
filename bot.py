import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("로그인중")
    print("준비됨")
    game = discord.Game("명령어 준비됨")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="{} 명의 유저와 {} 개의 서버에서 함께하는중 ". format(len(client.guilds), len(client.users))))
    




@client.event
async def on_message(message):
    if message.content.startswith("!서준아"):
        await message.channel.send("왓")
    if message.content.startswith("!심심해"):
        await message.channel.send("배그하던가 아무게임하던가.노래들으러가던가.공부하러가")
    if message.content.startswith("!몇살이니?"):
        await message.channel.send("관셈을보3")
    if message.content.startswith("!욕잘함?"):
        await message.channel.send("어 나 욕 잘해")
    if message.content.startswith("!도움"):
        await message.channel.send("명령어들 입니다")
        await message.channel.send("#!서준아")
        await message.channel.send("#!심심해")
        await message.channel.send("#!몇살이니?")
        await message.channel.send("#!욕잘함?")
        await message.channel.send("#!ㅎㅇ")
        await message.channel.send("#!ㅂㅂ")
        await message.channel.send("#!어디살아?")
    if message.content.startswith("!ㅎㅇ"):
        await message.channel.send("안녕 나는 서준이노예야")
    if message.content.startswith("!어디살아"):
        await message.channel.send("이세상 어딘가")
    if message.content.startswith("!ㅂㅂ"):
        await message.channel.send("잘가 다음에보장!!")




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
