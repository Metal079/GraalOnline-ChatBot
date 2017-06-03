import time
import pyautogui
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract' # Path to tesseract needs to be here for tesseract to work for whatever reason
players = {} # Used to store players names and where in the response is

def main(): # Lets all the magic happen
	while True:
		find_notification() # Finds and opens message notifications
		name_coords, reply_coords, text_coords = set_message_coords() # sets coords for various things
		option = read_message(text_coords) # Reads player's message and returns what they sent
		placement = player_id(name_coords, option) # Determines if the person who message was a previous user
		answer = response(placement) # Determines what response the bot should give
		reply(reply_coords, answer) # Actually replies


def find_notification(): #looks for a waiting PM and clicks it
	while True:
		image = pyautogui.locateCenterOnScreen('chat_icon.png', grayscale = False, confidence = .9)
		print(image)
		if image is not None:
			print('Found a waiting message')
			pyautogui.click(image)
			time.sleep(.1)
			break


def set_message_coords(): # Creates coords for message box and screenshots name
	try:
		imagex, imagey = pyautogui.locateCenterOnScreen('upper_right_message_corner.png', grayscale = True, confidence = .8)

	except:
		print('ERROR I SHOULD BE FINDING "upper_right_message_corner.PNG" EXITING PROGRAM')	
		exit()
	name_coords = (imagex - 390), imagey, 378, 50 # The coords of where the players name would be
	print('Found an open message, will now create coords')

	reply_coords = (imagex - 251), (imagey + 255 ) # Coords of the reply button
	text_coords = (imagex - 461), (imagey + 45), 430, 45 # Coords of where a players possible response is
	return name_coords, reply_coords, text_coords # Returns all coord values to be used by other functions


def player_id(name_coords, option): # Indentifies person who messaged and depending on if this person has messaged before changes response
	image = pyautogui.screenshot('name_test.png', region = name_coords) # Names are screenshots 
	name_image = str(pytesseract.image_to_string(Image.open('name_test.png'), lang = 'eng'))
	print('Players name is {}'.format(name_image))

	if name_image in players:
		print("User is previous user.")
		if option == '0':
			players[name_image] = None
		elif option == None:
			players[name_image] = None
		elif players[name_image] == None:
			players[name_image] = option
			return players[name_image]
		else:
			players[name_image] += option
		print(players[name_image])
		return players[name_image]
	else:
		print("User was not previously found, adding to dictionary.")
		players[name_image] = None
		print(players)
		return None


def reply(reply_coords, response): #Replies to PM
	pyautogui.click(reply_coords)
	print('Replying with {}'.format(response))
	pyautogui.typewrite(response)
	pyautogui.press('enter')


def read_message(text_coords): # Reads PM for numbers and sets option the number
	if pyautogui.locateCenterOnScreen('1.png',region = text_coords,  confidence = .9, grayscale = True):
		option = '1'
		print('Player messaged 1')
	elif pyautogui.locateCenterOnScreen('2.png',region = text_coords,  confidence = .9, grayscale = True):
		option = '2'
		print('Player messaged 2')
	elif pyautogui.locateCenterOnScreen('3.png',region = text_coords,  confidence = .9, grayscale = True):
		option = '3'
		print('Player messaged 3')
	elif pyautogui.locateCenterOnScreen('4.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '4'
		print('Player messaged 4l')
	elif pyautogui.locateCenterOnScreen('5.png',region = text_coords,  confidence = .9, grayscale = True):
		option = '5'
		print('Player messaged 5')
	elif pyautogui.locateCenterOnScreen('6.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '6'
		print('Player messaged 6')
	elif pyautogui.locateCenterOnScreen('7.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '7'
		print('Player messaged 7')
	elif pyautogui.locateCenterOnScreen('8.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '8'
		print('Player messaged 8')
	elif pyautogui.locateCenterOnScreen('9.png',region = text_coords,  confidence = .9, grayscale = True):
		option = '9'
		print('Player messaged 9')
	elif pyautogui.locateCenterOnScreen('0.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '0'
		print('Player messaged 0')
	else:
		print('Did not find digit answer. Will give default response.')
		option = None
	print(option)
	return option


def response(placement): # All the possible responses the bot can give a player
	if placement == None:
		return "Hello! I am a bot made to answer your questions! PM the number for more options! 1: Bounties. 2: Bug Hunting. 3: Looting. 4: Farming. 5: Obtaining Items. 6: Treasure Maps. 7: About Me."

	elif placement == '1':
		return "The bounty quest allows you to hunt mobs for cash! Location: Castle, steward's room(to the right in the throne room) [PM 1 for specifics, PM 2 for TIPS, PM 3 for possible bounties]"
	elif placement == '11':
		return 'Section under construction please check back later. PM "Metal" to suggest things [PM 0 to reset bot]'
	elif placement == '12':
		return '1. The bounty box will "drop"(stop following you, and will not pick up anything) after every kill/capture you get, and will require you to call it, or run over it to pick it up again. [PM 0 to reset choices]'
	elif placement == '13':
		return '100 green blobs, 20 Lizardons, 75 Pyrats, 75 Rebel soldiers(regular green baddy), 60 dark blobs, 60 rats, 75 snakes, 75 bats, 75 bandits, 80 spiders, 50 archers, or 50 crabs. [PM 0 to reset bot]'

	elif placement == '2':
		return '[PM 1 for Mantis info, 2 for Grasshopper, 3 for ladybug, 4 for Bumblebee, 5 for Dragonfly, or 6 for selling bugs]'
	elif placement == '21':
		return 'Flies from bush to bush and is worth 52 Gralats. Catching them is pretty easy, just turn towards the bush it is on and swing. Delta and Mod are my favorite places to find these bugs. But they are all over the map. [PM 0 to reset bot]'
	elif placement == '22':
		return 'These are worth 20 Gralats. One way to catch them is to let them hop, and as they land move and then swing. They are everywhere, but the ones on Castle\'s ramparts are often not caught, so its a good spot. [PM 0 to reset bot]'
	elif placement == '23':
		return 'These bugs fly around after being swung at(or just at random every now at then) and then will land again in a different spot, they are worth 52 Gralats. Now, the best technique is just being patient and locking on. [PM 0 to reset bot]'
	elif placement == '24':
		return 'Comes from bushes and grass. This bug is worth 16 Gralats. This bug will chase you after spawning and string. The strategy is to get above it, and swing downwards when it is in range. The best spots are in the castle courtyard. [PM 0 to reset bot]'
	elif placement == '25':
		return 'Flys around and stops periodically, they are worth 8 Gralats. Just follow it around, swing when it stops and continue following it. The best place(and only place) to find them is Swamp Town. [PM 0 to reset bot]'
	elif placement == '26':
		return 'Bugs can be sold to a witch in Swamp Town, she is in the tree above the pond at the start. Everyday she will have a bug she will pay 1.5x the usual price for. Always sell the bugs you get for that price. [PM 0 to reset bot]'

	elif placement == '3':
		return '[PM 1 for tips, PM 2 for loot selling locations, PM 0 to reset bot]'
	elif placement == '31':
		return "There are 5 loot chests in the Bandit Caves that reset daily. Go get them! [PM 0 to reset bot]"
	elif placement == '32':
		return 'PM 1 for selling clothes, 2 for pyrat stuff, 3 for mugs, 4 for weapons, 5 for fishing gear, 6 for sea shells, 7 for odd gem, 8 jewelry, 9 for anything else, and 0 to reset bot]'
	elif placement == '321':
		return "Taylor Richaards' House is right under Graal City.[PM 0 to reset choices]"
	elif placement == '322':
		return "He is standing on a small boat in York Town. Get in the water east of the horse track and swim east a little.[PM 0 to reset choices]"
	elif placement == '323':
		return "Rafael owns the Black Orchid, the pub in northwestern MoD Town.[PM 0 to reset choices]"
	elif placement == '324':
		return "The Snow Town Blacksmith, not the Onnet Town one. His place is in the northwest corner of Snow Town.[PM 0 to reset choices]"
	elif placement == '325':
		return "He is out fishing next to the house in the southwest corner of Swamp Town.[PM 0 to reset choices]"
	elif placement == '326':
		return "It is on the southeast beach of Oasis Island. This island is only accessible to VIP subscribers. If you don't think it is worth buying the VIP subscription, then just sell your seashells to Elster. [PM 0 to reset choices]"
	elif placement == '327':
		return "This guy is in the secret furniture in the rail cave between Snow Town and York Town.[PM 0 to reset choices]"
	elif placement == '328':
		return "Go to the west side of Destiny. This area is infested with Lizardons, so be careful.  The church is partially caved in, so you have to enter through the hole to the right. [PM 1 to continue]"
	elif placement == '3281':
		return 'Inside the church, you have to kill the Lizardon. Then place a bomb up at the front to blow up the ruble blocking the stairs. Father Randell will thank you for rescuing him and will give you a coin. [PM 1 to continue]'
	elif placement == '32811':
		return "Enter the cave that is right below Destiny Tower. Inside, go to the right and back. Use the Trick Coin on the metal door and you will be allowed into the Owl's Nest, a blackmarket. [PM 0 to reset choices]"
	elif placement == '329':
		return "Elster's Cave is just to the left of Sardon's Tower. If you talk to him, Elster will give you a lump sum of gralats for all your loot items. Note, you won't get as many Gralats as selling to the other NPCs.[PM 0 to reset choices]"

	elif placement == '4':
		return 'To start, over-world farming is a really good way to earn gralats. It is just boring as hell, so most people stay away from it.[PM 1 to continue, PM 0 to reset bot]'
	elif placement == '41':
		return ' VIP island has a good farm in a building in the north west corner, any of the hour areas(Fan, Zone, Snow Lodge, Grotto) are good areas. Then you have that one little house in upper York, I like that one. [PM 1 to continue, PM 0 to reset bot]'
	elif placement == '411':
		return 'House farming is a good way to have "back up" money, though most just use it for decoration. I would recommend getting a 2-p mount for this, as it has more blasts per bomb then your average horse.[PM 0 to reset bot]'

	elif placement == '5':
		return '[PM 1 for info getting the bug net, PM 2 for flippers]'
	elif placement == '51':
		return 'Open the map and head up to MoD town. When you make it, head down. You will see a tree on your right, go to inside. Talk to Adam(the NPC) inside and receive the bug net. [PM 0 to reset bot]'
	elif placement == '52':
		return "Before starting this quest, you must have already given the Fishing Line to Toll Guy. First, go to Toll Guy at the south end of the bridge under Graal City. [PM 1 to continue, 0 to reset bot]"
	elif placement == '521':
		return "He is thankful for the fishing line and wants to repay you by selling you the next fish he catches for 500 gralats. Pay him and stand there awhile. It just so happens that the next fish he catches is a very rare fish.[PM 1 to continue, 0 to reset bot]"
	elif placement == '5211':
		return "Go to York Town, then get into the sea. On your draisine, take the rail going north towards Snow Town. The draisine isn't really required for this since we are not going all the way to Snow Town. [PM 1 to continue, 0 to reset bot]"
	elif placement == '52111':
		return "In the first part of this rail cave, there is still a lot of water from the sea. Swim up the northwest corner of the cave and you will see a waterfall. Swim through the waterfall and you will enter a room.  [PM 1 to continue, 0 to reset bot]"
	elif placement == '521111':
		return "You will first notice the strange shadow swimming in circles around you. The chest on the ledge is locked. Equip the very rare fish received from the fisherman and hold it up in the center of the room. [PM 1 to continue, 0 to reset bot]"
	elif placement == '5211111':
		return "The shadow will reveal itself to be a Zorbi. Give him your fish and he will eat it right away. The Zorbi will you a Rusty Key. So go up and unlock the chest and you will find the Flippers. [PM 0 to reset bot]"


	elif placement == '6':
		return 'Treasure Maps can be obtained as rare loot, killing Bandits/Pyrats. Once found, you need to get it deciphered by the guy in the house which is second to the right as you first enter Destiny. [PM 1 to continue, 2 for loot, 0 to reset bot]'
	elif placement == '61':
		return "Once you're at the location shown on map, you need to dig the chest up with a shovel. It is possible to win treasure maps playing Crab Chance, too. [PM 1 to continue, 0 to reset bot]"
	elif placement == '611':
		return "It costs 25 gralats to get the guy to read another map after your first one is done for free. After this, the price will continue to stack (25, 50, 100 etc). This resets every 24hr when scoreboards resets. [PM 0 to reset bot]"
	elif placement == '62':
		return "You'll get one of the following: a miner's hat, traveler's hat, mushroom hat, a gold Gralat, a rare loot item, a pet rock, a mushroom pet, some treasure chest furniture, a treasure chest hat, a morph, a rock juggle, a gem skull juggle. [PM 0 to reset bot]"

	elif placement == '7':
		return 'I was created by "Metal", written in Python and my source code can be found by searching Github for GraalOnline-ChatBot. PM my creator to suggest things or if you just want to learn more about how I work. [PM 0 to reset bot]'

	else:
		return "Error! Valid invalid input. PM 0 to reset bot."

main()