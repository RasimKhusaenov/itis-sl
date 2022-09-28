"""
1. Сервер должен быть приложением командной строки (т.е. без графического интерфейса) и запускаться в ОС GNU/Linux.

2. При запуске сервер должен открыть на прослушивание порт 1303 на всех интерфейсах и ожидать подключения клиентской программы.

3. Когда будет установлено клиентское подключение отправить клиенту строку с текущей датой и временем в формате 22.09.2022 17:30 и закрыть соединение.

4. После отправки сообщения клиенту и закрытия соединения сервер должен снова ожидать подключение от клиента.
"""
import socket
from datetime import datetime

def main():
    sock = socket.socket()
    sock.bind(("0.0.0.0", 1303))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        current_datetime = datetime.now().strftime("%d.%m.%Y %H:%M")
        conn.send(current_datetime.encode("UTF-8"))
        conn.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        exit
