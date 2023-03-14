# simple tcp server listening on port 80, binding to all interfaces
import socket

# create a socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = '0.0.0.0'

port = 80

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))

    msg='Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('utf8'))
    clientsocket.close()