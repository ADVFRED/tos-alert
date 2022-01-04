from mcstatus import MinecraftServer
import asyncio
import discord
import configparser
import json

client = discord.Client()

config = configparser.ConfigParser()
config.read("config.cfg")

token=config["DISCORD"]["TOKEN"]
ip=config["MINECRAFT"]["serverIP"]
poil=json.loads(config["MINECRAFT"]["playersOfInterest"])
rate=int(config["SETUP"]["rate"])
channelID=int(config["DISCORD"]["channelID"])
server=MinecraftServer.lookup(ip)


class UnchangedDefaults (BaseException):
    pass

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    botChannel=client.get_channel(channelID)
    await botChannel.send("starting")
    print("starting")
    sentLog=[]
    query = server.query()
    playerList=query.players.names
    print(playerList)
    
    while True:
        query = server.query()
        playerList=query.players.names
        print(playerList)
        for onlinePlayer in playerList:
            print('op: '+onlinePlayer)
            if onlinePlayer in poil:
                print(onlinePlayer+"is in poil: "+str(poil))
                if onlinePlayer not in sentLog:
                    print(onlinePlayer+"not in connection log: "+str(sentLog))
                    sentLog.append(onlinePlayer)
                    await botChannel.send(onlinePlayer+" logged on")
        for target in sentLog:
            if target not in playerList:
                await botChannel.send(target+" logged off")
                sentLog.remove(target)
        await asyncio.sleep(rate)

if __name__ == "__main__":
    if token=="None" or ip=="None" or poil==[]:
        print("Config Defaults Unchanged")
        raise UnchangedDefaults()
    client.run(token)
