import socket
import json
import time

HOST = '127.0.0.1'
PORT = 5555


def send_msg(sock, msg):
    sock.send(msg.encode())


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

moves = ["UP", "RIGHT", "DOWN", "LEFT"]
buffer = ""
i = 0

while True:
    data = client.recv(1024).decode()
    if not data:
        break

    buffer += data

    while "\n" in buffer:
        line, buffer = buffer.split("\n", 1)

        if not line.strip():
            continue

        print("FROM SERVER:", repr(line))

        state = json.loads(line)

        move = moves[i%4]
        i += 1
        client.send((move + "\n").encode())
