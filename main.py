import pyautogui as auto
import pytesseract
import cv2

players = {}  # Used to store players names and where in the response is
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'  # Path to tesseract needs to be here for tesseract to work for whatever reason

def main():
    print("starting...")
    #setup
    message_region = set_message_coords()
    auto.click(message_region)
    player_name_region = set_username_coords()
    auto.press("tab")
    auto.typewrite(":sit")
    auto.press("enter")
    auto.press("tab")
    auto.typewrite("I am FAQ BOT ASK ME QUESTIONS")
    auto.press("enter")
    auto.press("tab")
    auto.typewrite(":pm")
    auto.press("enter")

    while(1):
        message_coords = find_message(message_region)
        auto.click(message_coords)
        player_username, player_spot = read_username(player_name_region)
        player_text = read_message(player_name_region)
        response =  find_response(player_username, player_spot, player_text)
        answer_message(message_coords, response)
        find_reconnect()


def set_message_coords():
    message_coords = None
    while message_coords == None:
        try:
            message_coords = auto.locateOnScreen('test.png')
            print(message_coords)
        except:
            print("did not find coords")
            pass

    print("Found pm coords")
    message_region = list(message_coords)
    message_region[0] = message_region[0] - 10
    message_region[1] = message_region[1] - 10
    message_region[2] = message_region[2] + 10
    message_region[3] = message_region[3] + 10
    print(message_region)
    message_region = tuple(message_region)
    return message_region

def find_message(message_region):
    message = None
    while message == None:
        try:
            message = auto.locateCenterOnScreen('test.png', region=message_region)
        except:
            #print("did not find message")
            pass
    print("found message")
    print(message)
    return message

def answer_message(message_coords, response):
    reply_button_coords = None
    while reply_button_coords == None:
        try:
            reply_button_coords = auto.locateCenterOnScreen('reply.png', grayscale=True, confidence=.8)
        except:
            print("did not find reply image")
            pass
    auto.click(reply_button_coords)
    auto.typewrite(response)
    auto.press('enter')
    print("answered message")

def read_username(player_name_region):
    try:
        image = auto.screenshot('name_test.png', region=player_name_region)  # Names are screenshots
    except:  # Some names break the bot, therefor we need to check for them
        return "Invalid Name"
    name_image = str(pytesseract.image_to_string(image))
    print('Players name is {}'.format(name_image))

    if name_image in players.keys():
        player_spot = players[name_image]
        print("player %s is in position %s", name_image, players[name_image])

    else:
        print("player is new")
        players[name_image] = "None"
        player_spot = players[name_image]
    return name_image, player_spot

def set_username_coords():
    name_coords = None
    while name_coords == None:
        try:
            name_coords = auto.locateOnScreen('username.png')
            print(message_coords)
        except:
            print("did not find initial username image (make sure your username matches username.png")
            pass
    return name_coords

def find_response(player_username, player_spot, player_text):
    if player_spot == "None":
        players[player_username] = ""
        return "Hello! I am a bot made to answer your questions! PM the number for more options! 1: Bounties. 2: Bug Hunting. 3: Looting. 4: Farming. 5: Obtaining Items. 6: Treasure Maps. 7: About Me."
    else:
        players[player_username] += player_text
        player_spot = players[player_username]
        print(player_spot)
        try:
            if int(players[player_username]) % 10 == 0:
                players[player_username] = '0'
                player_spot =  players[player_username]
        except:
            players[player_username] = ""
            player_spot = players[player_username]
            return "Error! Please only reply with numbers or the bot will freak out"

        if player_spot == "Invalid Name":
            return "Hello! It seems I am unable to decipher your name! Sorry but I cannot help you unless you change your name."
        elif player_spot == '1':
            print("asnwered %s", player_spot)
            return "The bounty quest allows you to hunt mobs for cash! Location: Castle, steward's room(to the right in the throne room) [PM 1 for specifics, PM 2 for TIPS, PM 3 for possible bounties]"
        elif player_spot == '11':
            return 'Section under construction please check back later. PM "Metal" to suggest things [PM 0 to reset bot]'
        elif player_spot == '12':
            return '1. The bounty box will "drop"(stop following you, and will not pick up anything) after every kill/capture you get, and will require you to call it, or run over it to pick it up again. [PM 0 to reset choices]'
        elif player_spot == '13':
            return '100 green blobs, 20 Lizardons, 75 Pyrats, 75 Rebel soldiers(regular green baddy), 60 dark blobs, 60 rats, 75 snakes, 75 bats, 75 bandits, 80 spiders, 50 archers, or 50 crabs. [PM 0 to reset bot]'

        elif player_spot == '2':
            return '[PM 1 for Mantis info, 2 for Grasshopper, 3 for ladybug, 4 for Bumblebee, 5 for Dragonfly, or 6 for selling bugs]'
        elif player_spot == '21':
            return 'Flies from bush to bush and is worth 52 Gralats. Catching them is pretty easy, just turn towards the bush it is on and swing. Delta and Mod are my favorite places to find these bugs. But they are all over the map. [PM 0 to reset bot]'
        elif player_spot == '22':
            return 'These are worth 20 Gralats. One way to catch them is to let them hop, and as they land move and then swing. They are everywhere, but the ones on Castle\'s ramparts are often not caught, so its a good spot. [PM 0 to reset bot]'
        elif player_spot == '23':
            return 'These bugs fly around after being swung at(or just at random every now at then) and then will land again in a different spot, they are worth 52 Gralats. Now, the best technique is just being patient and locking on. [PM 0 to reset bot]'
        elif player_spot == '24':
            return 'Comes from bushes and grass. This bug is worth 16 Gralats. This bug will chase you after spawning and string. The strategy is to get above it, and swing downwards when it is in range. The best spots are in the castle courtyard. [PM 0 to reset bot]'
        elif player_spot == '25':
            return 'Flys around and stops periodically, they are worth 8 Gralats. Just follow it around, swing when it stops and continue following it. The best place(and only place) to find them is Swamp Town. [PM 0 to reset bot]'
        elif player_spot == '26':
            return 'Bugs can be sold to a witch in Swamp Town, she is in the tree above the pond at the start. Everyday she will have a bug she will pay 1.5x the usual price for. Always sell the bugs you get for that price. [PM 0 to reset bot]'

        elif player_spot == '3':
            return '[PM 1 for tips, PM 2 for loot selling locations, PM 0 to reset bot]'
        elif player_spot == '31':
            return "There are 5 loot chests in the Bandit Caves that reset daily. Go get them! [PM 0 to reset bot]"
        elif player_spot == '32':
            return 'PM 1 for selling clothes, 2 for pyrat stuff, 3 for mugs, 4 for weapons, 5 for fishing gear, 6 for sea shells, 7 for odd gem, 8 jewelry, 9 for anything else, and 0 to reset bot]'
        elif player_spot == '321':
            return "Taylor Richaards' House is right under Graal City.[PM 0 to reset choices]"
        elif player_spot == '322':
            return "He is standing on a small boat in York Town. Get in the water east of the horse track and swim east a little.[PM 0 to reset choices]"
        elif player_spot == '323':
            return "Rafael owns the Black Orchid, the pub in northwestern MoD Town.[PM 0 to reset choices]"
        elif player_spot == '324':
            return "The Snow Town Blacksmith, not the Onnet Town one. His place is in the northwest corner of Snow Town.[PM 0 to reset choices]"
        elif player_spot == '325':
            return "He is out fishing next to the house in the southwest corner of Swamp Town.[PM 0 to reset choices]"
        elif player_spot == '326':
            return "It is on the southeast beach of Oasis Island. This island is only accessible to VIP subscribers. If you don't think it is worth buying the VIP subscription, then just sell your seashells to Elster. [PM 0 to reset choices]"
        elif player_spot == '327':
            return "This guy is in the secret furniture in the rail cave between Snow Town and York Town.[PM 0 to reset choices]"
        elif player_spot == '328':
            return "Go to the west side of Destiny. This area is infested with Lizardons, so be careful.  The church is partially caved in, so you have to enter through the hole to the right. [PM 1 to continue]"
        elif player_spot == '3281':
            return 'Inside the church, you have to kill the Lizardon. Then place a bomb up at the front to blow up the ruble blocking the stairs. Father Randell will thank you for rescuing him and will give you a coin. [PM 1 to continue]'
        elif player_spot == '32811':
            return "Enter the cave that is right below Destiny Tower. Inside, go to the right and back. Use the Trick Coin on the metal door and you will be allowed into the Owl's Nest, a blackmarket. [PM 0 to reset choices]"
        elif player_spot == '329':
            return "Elster's Cave is just to the left of Sardon's Tower. If you talk to him, Elster will give you a lump sum of gralats for all your loot items. Note, you won't get as many Gralats as selling to the other NPCs.[PM 0 to reset choices]"

        elif player_spot == '4':
            return 'To start, over-world farming is a really good way to earn gralats. It is just boring as hell, so most people stay away from it.[PM 1 to continue, PM 0 to reset bot]'
        elif player_spot == '41':
            return ' VIP island has a good farm in a building in the north west corner, any of the hour areas(Fan, Zone, Snow Lodge, Grotto) are good areas. Then you have that one little house in upper York, I like that one. [PM 1 to continue, PM 0 to reset bot]'
        elif player_spot == '411':
            return 'House farming is a good way to have "back up" money, though most just use it for decoration. I would recommend getting a 2-p mount for this, as it has more blasts per bomb then your average horse.[PM 0 to reset bot]'

        elif player_spot == '5':
            return '[PM 1 for info getting the bug net, PM 2 for flippers]'
        elif player_spot == '51':
            return 'Open the map and head up to MoD town. When you make it, head down. You will see a tree on your right, go to inside. Talk to Adam(the NPC) inside and receive the bug net. [PM 0 to reset bot]'
        elif player_spot == '52':
            return "Before starting this quest, you must have already given the Fishing Line to Toll Guy. First, go to Toll Guy at the south end of the bridge under Graal City. [PM 1 to continue, 0 to reset bot]"
        elif player_spot == '521':
            return "He is thankful for the fishing line and wants to repay you by selling you the next fish he catches for 500 gralats. Pay him and stand there awhile. It just so happens that the next fish he catches is a very rare fish.[PM 1 to continue, 0 to reset bot]"
        elif player_spot == '5211':
            return "Go to York Town, then get into the sea. On your draisine, take the rail going north towards Snow Town. The draisine isn't really required for this since we are not going all the way to Snow Town. [PM 1 to continue, 0 to reset bot]"
        elif player_spot == '52111':
            return "In the first part of this rail cave, there is still a lot of water from the sea. Swim up the northwest corner of the cave and you will see a waterfall. Swim through the waterfall and you will enter a room.  [PM 1 to continue, 0 to reset bot]"
        elif player_spot == '521111':
            return "You will first notice the strange shadow swimming in circles around you. The chest on the ledge is locked. Equip the very rare fish received from the fisherman and hold it up in the center of the room. [PM 1 to continue, 0 to reset bot]"
        elif player_spot == '5211111':
            return "The shadow will reveal itself to be a Zorbi. Give him your fish and he will eat it right away. The Zorbi will you a Rusty Key. So go up and unlock the chest and you will find the Flippers. [PM 0 to reset bot]"


        elif player_spot == '6':
            return 'Treasure Maps can be obtained as rare loot, killing Bandits/Pyrats. Once found, you need to get it deciphered by the guy in the house which is second to the right as you first enter Destiny. [PM 1 to continue, 2 for loot, 0 to reset bot]'
        elif player_spot == '61':
            return "Once you're at the location shown on map, you need to dig the chest up with a shovel. It is possible to win treasure maps playing Crab Chance, too. [PM 1 to continue, 0 to reset bot]"
        elif player_spot == '611':
            return "It costs 25 gralats to get the guy to read another map after your first one is done for free. After this, the price will continue to stack (25, 50, 100 etc). This resets every 24hr when scoreboards resets. [PM 0 to reset bot]"
        elif player_spot == '62':
            return "You'll get one of the following: a miner's hat, traveler's hat, mushroom hat, a gold Gralat, a rare loot item, a pet rock, a mushroom pet, some treasure chest furniture, a treasure chest hat, a morph, a rock juggle, a gem skull juggle. [PM 0 to reset bot]"

        elif player_spot == '7':
            return 'I was created by "Metal", written in Python and my source code can be found by searching Github for GraalOnline-ChatBot. PM my creator to suggest things or if you just want to learn more about how I work. [PM 0 to reset bot]'
        elif player_spot == "0":
            players[player_username] = ""
            return "Hello! I am a bot made to answer your questions! PM the number for more options! 1: Bounties. 2: Bug Hunting. 3: Looting. 4: Farming. 5: Obtaining Items. 6: Treasure Maps. 7: About Me."
        else:
            return "Error! invalid input. PM 0 to reset bot."

def read_message(player_name_region):  # Reads PM for numbers and sets option the number
    text_coords = list(player_name_region)
    print(text_coords)
    text_coords[0] -= 50
    text_coords[1] += 35
    text_coords[2] = 50
    text_coords[3] = 25
    text_coords = tuple(text_coords)

    player_text_image = auto.screenshot('player_text_region.png', region=text_coords)
    player_text = str(pytesseract.image_to_string(player_text_image, config="--psm 13"))
    print('Players text is "{}"'.format(player_text))
    while player_text is "":
        player_text_image = auto.screenshot('player_text_region.png', region=text_coords)
        player_text = str(pytesseract.image_to_string(player_text_image, config="--psm 13"))
        print('Players text is "{}"'.format(player_text))
    player_text_digit = player_text[0]
    if player_text_digit == 'O':
        player_text_digit = '0'
    print('input interpreted as %s', player_text_digit)
    return player_text_digit

def find_reconnect():  # looks for a recconect button and clicks it
	try:
		image = auto.locateCenterOnScreen('reconect.png', grayscale=True, confidence=.8)
	except:
		image = None
	if image is not None:
		print('Found a reconnect message')
		auto.click(image)
		print("------------------------------------")

main()
