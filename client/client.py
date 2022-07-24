

import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((HOST, PORT))

def receiver_runner(name):
    while True:
        try:
            data = my_socket.recv(1024).decode('ascii')
            handle_message(data)
        except:
            print("An error has occured!")
            my_socket.close()

def handle_message(data):
    if data == "test":
        send_message("Hello world!")

# To be binded by front-end team members
def send_message(message):
    my_socket.sendall(b"%s", message)

receiver_thread = threading.thread(target=receiver_runner)
receiver_thread.start()