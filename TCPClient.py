from socket import*

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

resultAnswer = "False"
numberAnswer = "False"

while resultAnswer.strip() == "False":
    sentence = input('Enter either random, add or subtract: ')
    clientSocket.send(sentence.encode())
    resultAnswer = clientSocket.recv(1024).decode()
    print('From server: ', resultAnswer)


while numberAnswer.strip() == "False":
    numbers = input('Enter two numbers with space in between: ')
    clientSocket.send(numbers.encode())
    numberAnswer = clientSocket.recv(1024).decode()
    print('From server: ', numberAnswer)


clientSocket.close()