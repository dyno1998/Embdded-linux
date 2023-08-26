import pyautogui
import time

#mouse functions 

#give the python file some time before executing 
time.sleep(3)

#mouse functions 
#prints the resolution of your screen
print(pyautogui.size()) 

#prints the current postion of the mouse 
print(pyautogui.position()) 

#moves the mouse over time 
# the third variables is the time 
pyautogui.moveTo(100,100,3)
#move the mouse relative to its current postion 
pyautogui.moveRel(100,100,3)


#click first two variables is he pos of y and x number of clicks duration and the button
pyautogui.click(500,500,3,3,button="left")
pyautogui.leftClick()
pyautogui.rightClick()
pyautogui.doubleClick()
pyautogui.tripleClick()

#scroll down - scroll up postive 
pyautogui.scroll(-500)

#mouse up and down
pyautogui.mouseUp(100,100,button='left')


#keyboard functions 
pyautogui.write("hello")
pyautogui.press("hello")
