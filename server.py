import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] Подключен {address}", file=file)
    print(f"[+] Подключен {address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{address}] {message}", file=file)
            print(f"[{address}] {message}")
            broadcast(message, client_socket)
        except:
            break
    print(f"[-] Отключен {address}", file=file)
    print(f"[-] Отключен {address}")
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(("--> " + message).encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)
    print("[*] Сервер запущен на порту 12345", file=file)
    print("[*] Сервер запущен на порту 12345")

    try:
        while True:
            client_socket, address = server.accept()
            clients.append(client_socket)
            thread = threading.Thread(target=handle_client, args=(client_socket, address))
            thread.start()
    except:
        print("[*] Сервер закрыт", file=file)
        print("[*] Сервер закрыт")

clients = []

if __name__ == "__main__":
    with open("messages.txt", "w", encoding="utf-8") as file:
        file.write("\n\n----NEW CHAT----\n")
        start_server()