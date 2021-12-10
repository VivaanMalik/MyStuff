import socket
HOST ='192.168.1.163'
PORT = 8801 # 2222
server = socket.socket()
server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to the server')
while True:
    print(client.recv(1024).decode())
    # with open ('nosus.txt', 'w') as file:
    #     file.write(client.recv(1024).decode())