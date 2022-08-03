import pyautogui #used to track mouse movements
import time #used to call time commands and delay stuff
import string #this will be used for just choosing letters
import random #this will be used for randomly selecting letters
import sys

numOfDownPresses = [1, 2, 3, 4, 5, 6]
processCounter = 1

print("Program starting up.")
time.sleep(3)
print("Your cursor position is being saved, place it where you want the automation to start.")

heldPosition = pyautogui.position() #holds in a variable where you wanted it
print(heldPosition)

promptChoice = input("Look at the current position, is that where you want it to start? (Y/N): ")

if promptChoice.lower() == "y": #continue as normal if yes
    pyautogui.click(heldPosition)
else:
    sys.exit() #stop program overall if no

time.sleep(5) #wait for edge to open up

for i in range(0, 30): #press backspace, then any key on the alphabet, then another random key on the alphabet, then press down a few times, then press enter
    print("Loop has executed", processCounter, "times.")

    pyautogui.hotkey('ctrl', 'e')  #ctrl e opens the search bar

    pyautogui.press('backspace')

    time.sleep(1) #wait a second
    
    randomLetter = random.choice(string.ascii_letters) #choose a random letter
    pyautogui.press(randomLetter) #type the random letter
    
    time.sleep(random.random()*2) #wait a little but in random times to avoid being spotted
    
    randomLetter = random.choice(string.ascii_letters) #choose random letter again
    pyautogui.press(randomLetter)
    
    for i in range(0, random.choice(numOfDownPresses)): #avoiding bot detection for like how many search results down we go
        pyautogui.press('down')
        time.sleep(random.random())
        
    pyautogui.press('enter')
    
    time.sleep(random.random()*10) #waiting between each search
    
    processCounter += 1

print("Program is done.")