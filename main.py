import time
import pyautogui
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract' #Needs to be here for tesseract to work for whatever reason
players = {} # Used to store players names and where in the response is
previous_message = None # Used in player_id() to 

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
	#print(imagex, imagey)

	reply_coords = (imagex - 251), (imagey + 255 ) # Coords of the reply button
	text_coords = (imagex - 461), (imagey + 45), 430, 45 # Coords of where a players possible response is
	return name_coords, reply_coords, text_coords # Returns all coord values to be used by other functions


def player_id(name_coords, option): # Indentifies person who messaged and depending on if this person has messaged before changes response
	image = pyautogui.screenshot('name_test.png', region = name_coords) # Names are screenshots 
	name_image = str(pytesseract.image_to_string(Image.open('name_test.png')))
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
	elif pyautogui.locateCenterOnScreen('3.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '3'
		print('Player messaged 3')
	elif pyautogui.locateCenterOnScreen('4.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '4'
		print('Player messaged 4l')
	elif pyautogui.locateCenterOnScreen('5.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '5'
		print('Player messaged 5')
	elif pyautogui.locateCenterOnScreen('6.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '6'
		print('Player messaged 6')
	elif pyautogui.locateCenterOnScreen('7.png',region = text_coords,  confidence = .8, grayscale = True):
		option = '7'
		print('Player messaged 7')
	elif pyautogui.locateCenterOnScreen('8.png',region = text_coords,  confidence = .9, grayscale = True):
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
		#reply(reply_coords,'ERROR PLEASE ENTER A NUMBER RESPONSE!')
		#main()
	print(option)
	return option


def response(placement): # All the possible responses the bot can give a player
	if placement == None:
		return "Hello! I am a bot made to answer your questions! PM the number for more options! 1: Bounties. 2: Bug Hunting. 3: Looting. 4: Farming. 5: Finding Items."

	elif placement == '1':
		return "The bounty quest allows you to hunt mobs for cash! Location: Castle, steward's room(to the right in the throne room) [PM 1 for specifics, PM 2 for TIPS, PM 3 for possible bounties]"
	elif placement == '11':
		return 'Section under construction please check back later. PM "Metal" to suggest things [PM 0 to reset choices]'
	elif placement == '12':
		return '1. The bounty box will "drop"(stop following you, and will not pick up anything) after every kill/capture you get, and will require you to call it, or run over it to pick it up again. [PM 1 for more info, PM 0 to reset choices]'
	elif placement == '13':
		return '100 green blobs, 20 Lizardons, 75 Pyrats, 75 Rebel soldiers(regular green baddy), 60 dark blobs, 60 rats, 75 snakes, 75 bats, 75 bandits, 80 spiders, 50 archers, or 50 crabs. [PM 0 to reset choices]'

	elif placement == '2':
		return 'Section under construction please check back later. PM "Metal" to suggest things [PM 0 to reset choices]'

	elif placement == '3':
		return 'Section under construction please check back later. PM "Metal" to suggest things [PM 0 to reset choices]'


	elif placement == '4':
		return 'To start, over-world farming is a really good way to earn gralats. It is just boring as hell, so most people stay away from it.[PM 1 to continue, PM 0 to reset choices]'
	elif placement == '41':
		return ' VIP island has a good farm in a building in the north west corner, any of the hour areas(Fan, Zone, Snow Lodge, Grotto) are good areas. Then you have that one little house in upper York, I like that one. [PM 1 to continue, PM 0 to reset choices]'
	elif placement == '411':
		return 'House farming is a good way to have "back up" money, though most just use it for decoration. I would recommend getting a 2-p mount for this, as it has more blasts per bomb then your average horse.[PM 1 to continue, PM 0 to reset choices]'

	elif placement == '5':
		return '[PM 1 for info getting the bug net]'
	elif placement == '51':
		return 'Open the map and head up to MoD town. When you make it, head down. You will see a tree on your right, go to inside. Talk to Adam(the NPC) inside and receive the bug net. [PM 0 to reset choices]'

	else:
		return "Error! Valid invalid input. If you think this bot is buggy as crap PM 'Metal'"
main()