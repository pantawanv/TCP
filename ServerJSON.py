from socket import *
import random
import json

def actions(data):

    numberResult = False 

    method = data["method"].upper()
    number1 = data["number1"]
    number2 = data["number2"]

    numberResult = isnumber(number1,number2)
    if numberResult != True:
        return numberResult
    

    
    if method.strip() == "RANDOM":

        if int(number1) <= int(number2):
            return "The result is: " + str(random.randint(int(number1), int(number2)))
        else:
            return "The result is: " + str(random.randint(int(number2), int(number1)))
        
       
    elif method.strip() == "ADD":
        return "The result is: " + str(int(number1)+int(number2))
    

    elif method.strip() == "SUBTRACT":
        return "The result is: " + str(int(number1)-int(number2))
    
    else:
        return "Method: " + method + "does not exist"


def isnumber(number1, number2):
    if number1.isnumeric() == False or number2.isnumeric() == False:
        return "Numbers " + number1 + " or " + number2 + " are not valid" 
    else: 
        return True


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:

    connectionSocket, addr = serverSocket.accept()

    data = connectionSocket.recv(1024).decode()
    json_data = json.loads(data)
    result = actions(json_data)
    connectionSocket.send(result.encode())

    connectionSocket.close()

