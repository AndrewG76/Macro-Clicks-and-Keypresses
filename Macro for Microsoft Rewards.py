import pyautogui #used to track mouse movements
import time #used to call time commands and delay stuff
import string #this will be used for just choosing letters
import random #this will be used for randomly selecting letters
import sys

numOfDownPresses = [1, 2, 3, 4, 5, 6]

print("Program starting up.")
time.sleep(2)
print("Your cursor position is being saved, place it where you want the automation to start.")

heldPosition = pyautogui.position() #holds in a variable where you wanted it
print(heldPosition)

promptChoice = input("look at the current position, is that where you want it to start? (Y/N): ")

if promptChoice.lower() == "y": #continue as normal if yes
    pyautogui.click(heldPosition)
else:
    sys.exit() #stop program overall if no

time.sleep(5) #wait for edge to open up

for i in range(0, 30): #press backspace, then any key on the alphabet, then another random key on the alphabet, then press down a few times, then press enter
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
    
    time.sleep(random.random()*5) #waiting between each search

print("Program is done.")
        
    
    
    
    
    
    

#maybe i can use like random function to choose between letters a-z for a bing search
#have it automate pressing the start button and typing in microsoft edge
#then it can macro press like ctrl e and then start typing stuff to search and then ctrl e again and keeps looping

