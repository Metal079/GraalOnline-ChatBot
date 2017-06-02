# GraalOnline-ChatBot

This is a bot that will search for unread PMs on the display, and depending on what numerical input it finds in the message, it will reply with the appropriate response.

Bot currently only supports GraalOnline Classic. However, support for Era, Olwest, Zone should be relatively easy to add in.

# How it works

The bot starts off by continuesly searching in a loop for chat_icon.png. Once it finds it, it will click it and then run set_message_coords() which will return the coordinates of the reply button, the players name, and the area where the message would be located. Afterwards, read_message(text_coords) will launch and search text_coords for a numerical response. If a number response is not found then None will be returned. From there player_id() will run and will check if the person who messaged the bot has previously messaged before, if it has it will load up the coresponding dictionary value and add option to it, if the person has not previously used the bot, a dictionary entry with the players name and the value None will be added. It will then run response(placement) and decide which response to send the player who messaged them. Finally, response() will actually reply.

# Requirements

Modules required: Pyautogui, pillow(Included when you install Pyautogui from pip), tesseract(for python 3) and pytesseract.

# To do

*Add much more dialoge options

*Add number 9 as a way to go back one level.

*Reorginize responses into a seperate file to prevent things from getting too confusing in the future.

*Find a way for the bot to handle strange IGNs (ex. mệtẩḽ).
