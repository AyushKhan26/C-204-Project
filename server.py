import socket
from threading import Thread

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 5000

CLIENTS = []

def acceptConnections():
  global SERVER
  global CLIENTS

  while True:
    player_socket,addr = SERVER.accept()
    player_name = player_socket.recv(2048).decode().strip()
    print(player_name)
    if(len(CLIENTS.keys()) == 0):
        CLIENTS[player_name]= {'player_type' : 'player1'}
    else :
      CLIENTS[player_name] = {'player_type' : 'player2'}

    CLIENTS[player_name]['player_socket'] = player_socket
    CLIENTS[player_name]['addr'] = addr
    CLIENTS[player_name]['player_name']= player_name
    CLIENTS[player_name]['turn']= False
   
    print(f"Connection established with {player_name}: {addr}")
   
def setup():
  print("\n\t\t\t******WELCOME TO TAMBOLA GAME******\n")


  global SERVER
  global IP_ADDRESS 
  global PORT

  SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  SERVER.bind(IP_ADDRESS,PORT)
  SERVER.listen(10)

  print("\t\t\t Server is waiting for incoming connections....\n")
    
  acceptConnections()

 
setup()
