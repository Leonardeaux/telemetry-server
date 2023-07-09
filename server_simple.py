import socket
import acc_telemetry as acct


def server(s):
    s.bind(('localhost', 12345))

    while True:
        message = (" ,".join(map(str, acct.read_physics()))) + "\n"
        print(message)

        s.listen(5)
        conn, addr = s.accept()
        conn.sendall(message.encode('utf-8'))


if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server(socket)