import random
import pyautogui as pg
# pyautogui is a Python library that allows you to control the mouse and keyboard to automate tasks and perform GUI automation
import time

animal=("Hack","Error404","Down")

time.sleep(8)                  #after 8 second below message print

for i in range(100):
    a=random.choice(animal)
    pg.write(a)
    pg.press("enter")

'''
working:-   1:-First click on the run button 
            2:-open your friend's chat page in WhatsApp web 
            3:-then wait for 8 seconds 
'''    
