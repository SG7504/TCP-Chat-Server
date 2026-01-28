import socket
import threading
import os
import time

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 4000))

clients = {}  
lock = threading.Lock()


def broadcast(message, exclude=None):
    with lock:
        for user, conn in clients.items():
            if user != exclude:
                try:
                    conn.sendall((message + "\n").encode())
                except:
                    pass


def handle_client(conn, addr):
    username = None
    conn.settimeout(60)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            msg = data.decode().strip()
            if not msg:
                continue

            if username is None:
                if not msg.startswith("LOGIN "):
                    conn.sendall(b"ERR invalid-login\n")
                    continue

                requested = msg[6:].strip()
                if not requested:
                    conn.sendall(b"ERR invalid-username\n")
                    continue

                with lock:
                    if requested in clients:
                        conn.sendall(b"ERR username-taken\n")
                        continue
                    clients[requested] = conn
                    username = requested

                conn.sendall(b"OK\n")
                continue

            
            if msg == "PING":
                conn.sendall(b"PONG\n")
                continue

            
            if msg == "WHO":
                with lock:
                    for user in clients:
                        conn.sendall(f"USER {user}\n".encode())
                continue

            
            if msg.startswith("DM "):
                parts = msg.split(" ", 2)
                if len(parts) < 3:
                    continue
                target, text = parts[1], parts[2]
                with lock:
                    if target in clients:
                        clients[target].sendall(
                            f"MSG {username} (private) {text}\n".encode()
                        )
                continue

            
            if msg.startswith("MSG "):
                text = msg[4:].strip()
                broadcast(f"MSG {username} {text}", exclude=username)

    except socket.timeout:
        pass
    finally:
        conn.close()
        if username:
            with lock:
                clients.pop(username, None)
            broadcast(f"INFO {username} disconnected")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Chat server running on port {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    start_server()
