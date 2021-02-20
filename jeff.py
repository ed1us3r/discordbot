import io

import discord
import random
import asyncio

from datetime import datetime
from PIL import Image
from discord import VoiceClient, VoiceChannel, FFmpegPCMAudio

random_quotes_list = [
        'Des isch ka Roggatsience       ~ T.Schaller',
        'Ich spuck dir in die Augen und blende dich!         ~ Die Ritter der Kokosnuss',
        'Querfeldein bin ich nicht zu gebrauchen. Wir Zwerge sind eher geborene Sprinter. Mordsgefährlich über kurze Entfernungen!          ~ Gimli Zwerg',
        'Gott würfelt nicht.         ~ Albert Einstein',
        'Das ist Nazi-jargong       ~ S.Schiller',
        'Woher soll ich das wissen ?        ~C.Schaller',
        'Wir sehen uns morgen in der Vorlesung!         ~F.Egerer',
        'Bims misch du Tischer.         ~A.Grammel',
        'Guns rarely kill people. Its usually the bullet leaving the gun that does the damage       ~Captain Obvious',
        'Beep Beep Bop      ~Jeff the Bot',
        'My Name is Jeff         ~Jeff',
        'Ähm        ~F.Adamsky',
        'Ich kümmere mich um Probleme in den Unterkünften.          ~S.Österle',
        'Ich bin kein Alkholiker        ~D.Harm -trinkend-',
        'Ich f1cke den mit meinem Rohr       ~N.Bauer',
        'Ich bin der Uwe und ich bin auch dabei         ~Uwe von der Parkbank',
        'Wer is denn eigentlich der Moritz?         ~Unbekannt',
        'Wo kommt denn da die Eins her?         ~Unbekannter Niederbayer',      
        'It is latency, stupid          ~Stuart Cheshire',
        'Hiar sehen wiar einen Spacko       ~W.Giltschier',
        'Alles Bots hier ~Grusi der Bot',
        'Es wird schwerer, die Reihen lichten sich          ~M.Kullmann'
        ]

choice_list = [True, False]
#For Random effect when bot does random quotes




class MyClient(discord.Client):

    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt Meister")
    async def send_public_message(message, msg):
        await message.channel.send(msg)
    async def send_direct_message(message, msg):
        
        await message.author.send(msg) 
    #IDEE WEGEN ZEIT zur Prüfung !!!!!!
    #Wenn Nachricht kommt, egal von wem
    async def on_message(self, message):
        #Wennn Bot adressiert wird
        if check_message_for_jeff(message)and message.author.name != 'J3ff':          
           await message.channel.send(bot_jeff_def(message))

           return
        if message.content.startswith('!'):
            print("Message starts with >>     !       <<")

            print("Starting Bot Dialogue >>           <<")
            await bot_comm_def(message)
            return
        # Returns a datetime object containing the local date and time
        datetimeobj = datetime.now()

        if message.channel.type != discord.ChannelType.private: #Only for non Private DM Conversations
            print(datetimeobj.strftime("%d-%b-%Y (%H:%M:%S.%f)") + ' >>  ' + 'Nachricht von '+ message.author.name + ' im Channel ' + message.channel.name + ' erhalten.  << ' )
            if message.channel.name == 'testchat'  and message.author.name != 'J3ff':
                print(datetimeobj.strftime("%d-%b-%Y (%H:%M:%S.%f)") + ' >>  ' + 'Nachricht im ' + message.channel.name + ' ... Erstelle eine Nachricht  << ' )
                if random.choice(choice_list):
                    response = create_message(message)
                
                elif random.choice(choice_list):
                    response = create_random_quotes()
                else:
                    response = None
                

                if response is not None:
                    await message.channel.send(response)
                    return
            return
        elif message.channel.type == discord.ChannelType.private and message.author.name != "J3ff":
            
            print(datetimeobj.strftime("%d-%b-%Y (%H:%M:%S.%f)") + ' >>  ' + 'Nachricht von '+ message.author.name + ' im privaten Channel  erhalten.  << ' )

def check_message_for_jeff(message):
    jeff_aliases = ["jeff", "Jeff", "JEFF", "J3ff", "J3FF", "j3ff","JEff","jEff", "Bot", "bot", "BOT", "JefF", "jeFf", "jEff", "jEFf", "jef"]
    msg = message.content
    msg_list = msg.split()
    x = 0
    for x in range(len(msg_list)):
        if msg_list[x] in jeff_aliases:
            return True
        
    return False 

def bot_jeff_def(message):
    #Whenever Jeff is mentioned JEff starts a dialogue
    answer = "Hi "+ message.author.name + ", you just mentioned me, can i help you? \n Just try out !help to get further Informations"
    return answer
    
def eastereggs_def():
    return "I was made by a crazy guy named Spasterix"

def create_message(message):
    # Returns a datetime object containing the local date and time
    datetimeobj = datetime.now()

    print(datetimeobj.strftime("%d-%b-%Y (%H:%M:%S.%f)") + ' >>  ' + 'Erstelle eine Nachricht für: '+ message.author.name + '   << ')
    if random.choice(choice_list):
        #Sends Personalized messages 
        if message.author == client.user:
            return
        elif message.author.name == 'EdiUser' and random.choice(choice_list):
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


def create_random_quotes():
    #Creates Random Quote from list above
    random_quote = random.choice(random_quotes_list)
    return random_quote

async def play_auenland(message):
    #Creates and plays the Auenland Scream and establishes the needed Voice Connection
    channel = message.author.voice.channel
    print("Channel to Connect to :"+channel.name)
    vc = await channel.connect()

    vc.play(FFmpegPCMAudio('Auenland.mp3'))

    while vc.is_playing():
        await asyncio.sleep(1)
    else:
        await vc.disconnect()


async def bot_comm_def(message):
    #Starts Bot dialogue from public server
    message = message
    msg = message.content
    print("Message to Bot contains:  >> "+ msg+ "     <<")

    if msg.startswith('!'):
        #Help Dialogue
        if msg == "!help"or msg == "!h" or  msg == "!HELP" or msg == "!Help" or "help" in msg or "HELP" in msg or "Help" in msg:
            startmessage = "Hi "+ message.author.name + ", i am an nonhuman Intelligance and i will try my best to help you !"
            await MyClient.send_direct_message(message, startmessage)
            information_message = "Maybe try out \n :ballot_box_with_check:\" !Exams \" \n :ballot_box_with_check:\" !Stundenplan \" \n for some additional Infos ! " + "\n" + "And don't forget to use \n :ballot_box_with_check:\" !fun \"  \n"
            await MyClient.send_direct_message(message,information_message)
            print(" >> " + " Erstelle eine Direkachricht für "+ message.author.name + '   << ')
            return 
        elif  msg == "!lol": 
            #EASTEREGG
            return 
        elif msg == "!fun" or msg =="!FUn" or msg ==  "!FUN" or msg == "!fUn" or msg == "!f" or msg == "!fuN":
            x = 12
            troll_message = "\n"
            for i in range(x+2):
                troll_message += ":white_medium_square:"
            troll_message += "\n"
            for i in range(x):
                troll_message += ":large_blue_diamond: "
            troll_message += "\n"
            for i in range(x):
                troll_message += ":red_circle: "
            troll_message += "\n"
            troll_message += "Ra Ra Rasputin ... Jeff is a russian Machine !!!  " 
            await MyClient.send_direct_message(message,troll_message )
            return
        elif msg == "!Gollum" or msg =="!gollum":
            #source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("Auenland.mp3"))
            #client.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            await play_auenland(message)
            #await client.send('Now playing: {}'.format("./Auenland.ogg"))

        elif msg == "!StundenPlan" or msg == "!Stunenplan" or msg == "Studenplan":
            today = datetime.now()
            wek = today.strftime("%W")
            wk = int(wek)+1
            week = str(wk)
            print(week)
            path = "/home/ediuser/py.practise/discordbot/Stundenpläne/KW_39.JPG"
            with open(path, 'rb') as f:
                picture = discord.File(f)
                await MyClient.send_direct_message(message,picture)
            return

         
#     Run bot
if __name__ == '__main__':
    client = MyClient()
    client.run("NzU2MTk5OTc3NDM2NTc3ODUz.X2OYHA.C3hiYKIiqx0tqiss8iNMfzpc_AE")


