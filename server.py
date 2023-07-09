import socket
import threading
import time
import acc_telemetry as acct


def handle_client(client_socket, client_address):
    while True:
        message = (",".join(map(str, acct.read_physics()))) + "\n"
        print(message)
        client_socket.send(message.encode())

        # time.sleep(1)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "localhost"
    port = 12345

    server_socket.bind((host, port))

    server_socket.listen(5)
    print("Server is waiting {}:{}".format(host, port))

    while True:
        client_socket, client_address = server_socket.accept()
        print("New connection : {}:{}".format(client_address[0], client_address[1]))

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == '__main__':
    start_server()
