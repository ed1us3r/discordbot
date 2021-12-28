import discord
import io
import os
import logging
import discord
import random
import asyncio

from datetime import datetime
from discord import VoiceClient, VoiceChannel, FFmpegPCMAudio
from dotenv import load_dotenv

choice_list = [True, False]

class MyClient(discord.Client):
    def init(self):
        self.ready = False
        self.quotes = []
        self.choice_list = [True, False]
        with open("src/Quotes") as file:
            for line in file:
                self.quotes.append(line)

    # Login
    async def on_ready(self):
        self.ready = True
        logging.debug("Bot hat sich am Server eingeloggt !")
        print("Ich habe mich eingeloggt Meister")
        return 1

    # Send message in channel
    async def send_public_message(message, msg):
        try:
            logging.debug("Sende Message: " + msg + " an den Channel: " + message.channel.name + " ")
            await message.channel.send(msg)
        except err:
            print(err)
            logging.error("Senden der Message war nicht erfolgreich!")

    # Send message in DM's
    async def send_direct_message(message, msg):
        try:
            logging.debug("Sende Message: " + msg + " direkt an den User: " + message.author.name + " ")
            await message.author.send(msg)
        except err:
            print(err)
            logging.error("Senden der Direktnachricht nicht erfolgreich!")

    async def create_random_quotes(self):
        # Creates Random Quote from list above
        random_quote = random.choice(self.quotes)
        return random_quote

    # every message that reaches the bot
    async def on_message(self, message):
        # Returns a datetime object containing the local date and time
        datetimeobj = datetime.now()
        logging.info("Nachricht mitgelesen >> Inhalt:" + message.content + " Absender: " + message.author.name)
        # Message in DM
        if not message.author.bot and message.channel.type == discord.ChannelType.private:
            logging.debug("Nachricht war in den DM's von Jeff")
            logging.debug(
                "erhaltene Nachricht ist nicht von einem Bot da message.author.bot= " + str(message.author.bot))
            if check_message_for_jeff(message) and message.author.name != 'J3ff':
                print(
                    "Message contains >>     Jeff     << >> Preparing personalized Message for:" + message.author.name)
                await message.channel.send(bot_jeff_def(message))
                return 1
            if message.content.startswith('!'):
                print("Message starts with >>     !       <<")
                print("Starting Bot Dialogue >>           <<")
                await bot_comm_def(message)
                return 1

        # Only for non Private Message (!DM)
        if message.channel.type != discord.ChannelType.private:
            logging.debug(datetimeobj.strftime(
                "%d-%b-%Y (%H:%M:%S.%f)") + ' >>  ' + 'Nachricht von ' + message.author.name + ' im Channel ' + message.channel.name + ' erhalten.  << ')
            if message.content.startswith('!'):
                print("Message starts with >>     !       <<")
                print("Starting Bot Dialogue >>           <<")
                await bot_comm_def(message)
                return 1
            elif message.channel.name == "call-a-gollum":
                try:
                    logging.debug("Nachricht im Channel call-a-gollum @ Auenland, versuche Nachricht zu löschen.")
                    await message.delete()
                except:
                    logging.error("Es ist ein Fehler aufgetreten beim Versuch die Nachricht:" + message + "zu löschen.")
                    return 0
                else:
                    return 1
            elif message.channel.name == 'testchat':
                print(datetimeobj.strftime(
                    "%d-%b-%Y (%H:%M:%S.%f)") + ' >>  ' + 'Nachricht im ' + message.channel.name + ' \n >> Erstelle eine Nachricht  << ')
                if random.choice(self.choice_list):
                    response = create_message(message)
                elif random.choice(self.choice_list):
                    response = await self.create_random_quotes()
                else:
                    response = None
                if response is not None:
                    await message.channel.send(response)
                    return
            return


def check_message_for_jeff(message):
    jeff_aliases = ["jeff", "Jeff", "JEFF", "J3ff", "J3FF", "j3ff", "JEff", "jEff", "Bot", "bot", "BOT", "JefF", "jeFf",
                    "jEff", "jEFf", "jef"]
    msg = message.content
    msg_list = msg.split()
    x = 0
    for x in range(len(msg_list)):
        if msg_list[x] in jeff_aliases:
            return True

    return False


def bot_jeff_def(message):
    # Whenever Jeff is  in DM mentioned JEff starts a dialogue
    answer = "Hi " + message.author.name + ", you just mentioned me, can i help you? \n Just try out !help to get further Informations"
    return answer


def eastereggs_def():
    return "I was made by a crazy guy named Spasterix"


def create_message(message):
    # Returns a datetime object containing the local date and time
    datetimeobj = datetime.now()
    print(datetimeobj.strftime(
        "%d-%b-%Y (%H:%M:%S.%f)") + ' >>  ' + 'Erstelle eine Nachricht für: ' + message.author.name + '   << ')
    if random.choice(choice_list):
        # Sends Personalized messages
        if message.author.name == 'EdiUser' and random.choice(choice_list):
            return 'Der Meister hat gesprochen'
        elif message.author.name == 'hasselhoff':
            return 'Was ein Spasst dieser David'
        elif message.author.name == 'Der Laternisierer':
            return 'Der Tiger hat gesprochen'
        elif message.author.name == 'philsstift':
            return 'Nohomo ?'
        elif message.author.name == 'Dani_ela':
            return 'Taniela hat gesprochen'
        elif message.author.name == 'GT-Saiyaman':
            return 'Invest Invest Invest '
        return


async def play_auenland(message):
    # Creates and plays the Auenland Scream and establishes the needed Voice Connection
    channel = message.author.voice.channel
    print("Channel to Connect to :" + channel.name)
    vc = await channel.connect()

    vc.play(FFmpegPCMAudio('src/Auenland.mp3'))

    while vc.is_playing():
        await asyncio.sleep(1)
    else:
        await vc.disconnect()


async def bot_comm_def(message):
    # Starts Bot dialogue from public server
    message = message
    msg = message.content
    print("Message to Bot contains:  >> " + msg + "     <<")

    if msg.startswith('!'):
        # Help Dialogue
        if msg == "!help" or msg == "!h" or msg == "!HELP" or msg == "!Help" or "help" in msg or "HELP" in msg or "Help" in msg:
            startmessage = "Hi " + message.author.name + ", i am an nonhuman Intelligance and i will try my best to help you !"
            await MyClient.send_direct_message(message, startmessage)
            information_message = "Maybe try out \n :ballot_box_with_check:\" !Exams \" \n :ballot_box_with_check:\" !Stundenplan \" \n for some additional Infos ! " + "\n" + "And don't forget to use \n :ballot_box_with_check:\" !fun \"  \n"
            await MyClient.send_direct_message(message, information_message)
            print(" >> " + " Erstelle eine Direkachricht für " + message.author.name + '   << ')
            return
        elif msg == "!lol":
            # EASTEREGG
            return
        elif msg == "!fun" or msg == "!FUn" or msg == "!FUN" or msg == "!fUn" or msg == "!f" or msg == "!fuN":
            x = 12
            troll_message = "\n"
            for i in range(x + 2):
                troll_message += ":white_medium_square:"
            troll_message += "\n"
            for i in range(x):
                troll_message += ":large_blue_diamond: "
            troll_message += "\n"
            for i in range(x):
                troll_message += ":red_circle: "
            troll_message += "\n"
            troll_message += "Ra Ra Rasputin ... Jeff is a russian Machine !!!  "
            await MyClient.send_direct_message(message, troll_message)
            return
        elif msg == "!Gollum" or msg == "!gollum":
            # source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("Auenland.mp3"))
            # client.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            await play_auenland(message)
            # await client.send('Now playing: {}'.format("./Auenland.ogg"))
            if message.channel.name == "call-a-gollum":
                await message.delete()

        elif msg == "!StundenPlan" or msg == "!Stunenplan" or msg == "Studenplan":
            today = datetime.now()
            wek = today.strftime("%W")
            wk = int(wek) + 1
            week = str(wk)
            print(week)
            path = "/home/ediuser/py.practise/discordbot/Stundenpläne/KW_39.JPG"
            with open(path, 'rb') as f:
                picture = discord.File(f)
                await MyClient.send_direct_message(message, picture)
            return


def run():
    client = MyClient()
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client.init()
    client.run(token)
    return


#     Run bot
if __name__ == '__main__':
    run()
