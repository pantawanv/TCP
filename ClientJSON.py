from socket import*
import json 

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

data = {
    "method": input('Enter method: '),
    "number1": input('Enter first number: '),
    "number2": input('Enter second number: ')
}

json_object = json.dumps(data)
clientSocket.send(json_object.encode())
response = clientSocket.recv(1024).decode()
print(response)

clientSocket.close()