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
    while True:
        query = server.query()
        pl=query.players.names
        for op in pl:
            if op in poil:
                if op not in sentLog:
                    sentLog.append(op)
                    await botChannel.send(op+" is online")
        for poi in sentLog:
            if poi not in pl:
                await botChannel.send(op+" is offline")
                sentLog.remove(poi)
        await asyncio.sleep(rate)

if __name__ == "__main__":
    if token=="None" or ip=="None" or poil==[]:
        print("Config Defaults Unchanged")
        raise UnchangedDefaults()
    client.run(token)
