from socket import *
import random

def actions():
    method = connectionSocket.recv(1024).decode()
    method = method.upper()
    numberResult = False 

    if method.strip() == "RANDOM":
        connectionSocket.send("Random has been selected".encode())
        while numberResult == False:
            numberResult = number()
        
        if int(numberResult[0]) <= int(numberResult[1]):
            return random.randint(int(numberResult[0]), int(numberResult[1]))
        else:
            return random.randint(int(numberResult[1]), int(numberResult[0]))
        
    elif method.strip() == "ADD":
        connectionSocket.send("Add has been selected".encode())
        while numberResult == False:
            numberResult = number()
        return int(numberResult[0]) + int(numberResult[1])
    
    elif method.strip() == "SUBTRACT":
        connectionSocket.send("Subtract has been selected".encode())
        while numberResult == False:
            numberResult = number()
        return int(numberResult[0])-int(numberResult[1])
    
    else:
        connectionSocket.send("False".encode())
        return False


def number():
    number = connectionSocket.recv(1024).decode()
    number = number.split()

    if len(number) !=2:
        return False
    else:
        for item in number:
            if item.isnumeric() == False:
                return False
            return number 


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:

    connectionSocket, addr = serverSocket.accept()

    result = False 

    while result == False:
        result = actions()
    

    connectionSocket.send(("The result is "+str(result)).encode())
    connectionSocket.close()

