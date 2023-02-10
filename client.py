import socket
from tkinter import * 
from threading import Thread
import random 
from PIL import Image,ImageTk

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 5000

def setup():
 global SERVER
 global IP_ADDRESS
 global PORT

 SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 SERVER.connect((IP_ADDRESS,PORT))
 
 thread = Thread(target=recievedMsg)
 thread.start()

setup()

def askPlayerName():
  global playerName
  global nameEntry
  global nameWindow
  global canvas1

  nameWindow = Tk()
  nameWindow.title('Tambola Family Game')
  nameWindow.geometry('800x800')

  screen_width = nameWindow.winfo_screenwidth()
  screen_height = nameWindow.winfo_screenheight()

  bg = ImageTk.PhotoImage('./assets/background.jpg')

  canvas1 = Canvas(nameWindow, width=500, height=500)
  canvas1.pack(fill='both',expand = True)
  
  canvas1.create_image(0,0,image = bg, anchor='nw')
  canvas1.create_text(screen_width/4.5,screen_height/8, text='Enter Name',font=('Chalkboard SE',60),fill='black')

  nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE',30), bd=5,bg='white')
  nameEntry.place(x= screen_width/7,y= screen_height/5.5)

  button = Button(nameWindow, text='Save', font=('Chalkboard SE',30),width=11,height=2, bg='#80deea',bd=2, command=saveName)
  button.place(x = screen_width/6,y = screen_height/4)

  nameWindow.resizable(True,True)
  nameWindow.mainloop()

def saveName():
    global SERVER
    global nameEntry
    global nameWindow

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()
     
    SERVER.send(playerName.encode())