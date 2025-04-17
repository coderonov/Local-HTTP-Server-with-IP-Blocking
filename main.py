import http.server
import socketserver
import os
import threading
import socket
from tkinter import Tk
from tkinter.filedialog import askdirectory

blocked_ips = set()
blocked_message = "Access denied: Your IP is blocked."
refresh_interval = 5

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"{self.client_address[0]} - - [{self.log_date_time_string()}] {format % args}")

    def do_GET(self):
        if self.client_address[0] in blocked_ips:
            self.send_response(403)
            self.send_header("Refresh", f"{refresh_interval}; url=/")
            self.end_headers()
            self.wfile.write(blocked_message.encode())
        else:
            try:
                super().do_GET()
            except (ConnectionResetError, ConnectionAbortedError) as e:
                print(f"Ошибка соединения: {e}")
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_device_info():
    hostname = socket.gethostname()
    local_ip = get_local_ip()
    return f"Имя устройства: {hostname}, IP-адрес: {local_ip}"

def start_server(directory):
    os.chdir(directory)
    PORT = 8000
    handler = CustomRequestHandler
    with socketserver.TCPServer((get_local_ip(), PORT), handler) as httpd:
        print(f"Сервер запущен по адресу: http://{get_local_ip()}:{PORT}")
        print("Нажмите Ctrl+C для остановки сервера.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер остановлен.")

def block_ip(ip):
    blocked_ips.add(ip)
    print(f"IP-адрес {ip} заблокирован.")

def unblock_ip(ip):
    if ip in blocked_ips:
        blocked_ips.remove(ip)
        print(f"IP-адрес {ip} разблокирован.")
    else:
        print(f"IP-адрес {ip} не был заблокирован.")

def set_blocked_message(message):
    global blocked_message
    blocked_message = message
    print(f"Сообщение для заблокированных пользователей изменено на: {message}")

def set_refresh_interval(interval):
    global refresh_interval
    refresh_interval = interval
    print(f"Интервал перезагрузки страницы изменен на: {interval} секунд.")

def select_directory():
    Tk().withdraw()
    directory = askdirectory(title="Выберите папку с сайтом")
    
    if directory:
        print(f"Выбрана папка: {directory}")
        server_thread = threading.Thread(target=start_server, args=(directory,))
        server_thread.daemon = True
        server_thread.start()
        
        print(get_device_info())
        
        while True:
            command = input("Введите команду (block <IP>, unblock <IP>, set_msg <message>, set_refresh <seconds>, exit): ")
            if command.lower() == "exit":
                print("Завершение программы.")
                break
            elif command.startswith("block "):
                ip = command.split(" ")[1]
                block_ip(ip)
            elif command.startswith("unblock "):
                ip = command.split(" ")[1]
                unblock_ip(ip)
            elif command.startswith("set_msg "):
                message = command[len("set_msg "):]
                set_blocked_message(message)
            elif command.startswith("set_refresh "):
                interval = int(command.split(" ")[1])
                set_refresh_interval(interval)
            else:
                print("Неизвестная команда.")
    else:
        print("Папка не выбрана. Программа завершена.")

if __name__ == "__main__":
    select_directory()
