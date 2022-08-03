import pyautogui #used to track mouse movements
import time #used to call time commands and delay stuff
import string #this will be used for just choosing letters
import random #this will be used for randomly selecting letters
import sys

numOfDownPresses = [1, 2, 3, 4, 5, 6]

print("yo wassup")
#userInput = input("give me some kind of user input")
time.sleep(2)
print("after 2 seconds")

heldPosition = pyautogui.position()
print(heldPosition)

#pyautogui.click(685,1045) #this will click my file explorer on the vertical monitor setup

#pyautogui.click(612, 1049) #this will click microsoft edge on the vertical monitor setup


promptChoice = input("look at the current position, is that where you want it to start? (Y/N)")

if promptChoice == "Y" or promptChoice == "y":
    pyautogui.click(heldPosition)
else:
    sys.exit()

time.sleep(5) #wait for edge to open up

#then press backspace, then any key on the alphabet, then another random key on the alphabet, then press down twice, then press enter

for i in range(0, 30):
    pyautogui.hotkey('ctrl', 'e')  #ctrl e opens the search bar
    
    #equivalent method is do the hotkey by simulating pressing the buttons down
    #with pyautogui.hold('ctrl'): #press the ctrl key down
    #    pyautogui.press('e') 

    pyautogui.press('backspace')

    time.sleep(1) #wait a second
    
    randomLetter = random.choice(string.ascii_letters) #choose a random letter
    pyautogui.press(randomLetter) #type the random letter
    
    time.sleep(random.random()*3) #wait a little but in random times to avoid being spotted
    
    randomLetter = random.choice(string.ascii_letters) #again
    pyautogui.press(randomLetter)
    
    for i in range(0, random.choice(numOfDownPresses)): #avoiding bot detection for like how many search results down we go
        pyautogui.press('down')
        time.sleep(random.random())
        
    pyautogui.press('enter')
    
    time.sleep(random.random()*5)
        
    
    
    
    
    
    

#maybe i can use like random function to choose between letters a-z for a bing search
#have it automate pressing the start button and typing in microsoft edge
#then it can macro press like ctrl e and then start typing stuff to search and then ctrl e again and keeps looping

