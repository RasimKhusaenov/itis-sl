"""
1. Клиент должен быть приложением командной строки (т.е. без графического интерфейса) и запускаться в ОС GNU/Linux.

2. При запуске клиент должен в интерактивном режиме запросить у пользователя IP адрес сервера.

3. После получения IP адреса клиент должен подключить к серверу по порту 1303 по IP адресу полученному от пользователя.

4. После подключения к серверу клиент должен прочитать строку и вывести её на экран, потом закрыть соединение и завершить работу.
"""
import socket

def main():
    server_ip = input("Enter server IP address: ")
    sock = socket.socket()
    sock.connect((server_ip, 1303))

    current_datetime = sock.recv(1024)
    print(current_datetime.decode("UTF-8"))
    sock.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        exit
