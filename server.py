import socket
import threading
import time
import acc_telemetry as acct
from utils import param_to_message


def handle_client(client_socket, client_address):
    while True:
        physics = acct.read_physics()
        graphics = acct.read_graphics()
        if physics["speedKmh"] == 0:
            continue
        message = param_to_message(
            timestamp=str(int(time.time())),
            gas=str(round(physics["gas"], 2)),
            brake=str(round(physics["brake"], 2)),
            speedKmh=str(int(physics["speedKmh"])),
            laps=str(graphics['completedLaps']),
            steerAngle=str(round(physics["steerAngle"], 2)),
            abs=str(int(physics["abs"]))
        )
        print(message)
        client_socket.send(message.encode())


def start():
    while True:
        physics = acct.read_physics()
        graphics = acct.read_graphics()
        if physics["speedKmh"] == 0:
            continue
        message = param_to_message(
            timestamp=str(int(time.time())),
            gas=str(round(physics["gas"], 2)),
            brake=str(round(physics["brake"], 2)),
            speedKmh=str(int(physics["speedKmh"])),
            laps=str(graphics['completedLaps']),
            steerAngle=str(round(physics["steerAngle"], 2)),
            abs=str(int(physics["abs"]))
        )
        print(message)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "localhost"
    port = 12346

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
