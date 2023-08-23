import keyboard
import xerox
flag=0
while True:
      if keyboard.is_pressed("ctrl+c") and flag==0:
       text= xerox.paste()
       flag=1
      if(flag==1) and keyboard.is_pressed("a"):
       flag=0
       with open('/home/mohanad/Documents/docs/text', "alt+shift+s") as f:
        f.write(text + "\n") 
    


