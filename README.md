# 📡 Local HTTP Server with IP Blocking

A Python script for running a local HTTP server with the ability to block IP addresses, set a custom block message, and automatically refresh the page for blocked users.

## 🛋️ Features

- Launch an HTTP server in a selected directory
- Block/unblock specific IP addresses
- Custom message display for blocked users
- Automatic page refresh for blocked clients
- Logging of HTTP requests

## 🚀 Getting Started

1. Make sure you have Python 3 installed
2. Download or clone this repository
3. Run the script:

```bash
python main.py
```

4. Choose a folder with your HTML/files
5. The server will be available at `http://<IP>:8000`

## ⚙️ Console Commands

- `block <IP>` — block an IP address
- `unblock <IP>` — unblock an IP address
- `set_msg <text>` — set a custom block message
- `set_refresh <seconds>` — set the page refresh interval
- `exit` — exit the program

## 📦 Dependencies

All libraries used are from Python's standard library:

- `http.server`
- `socketserver`
- `os`
- `threading`
- `socket`
- `tkinter`

> ⚠️ On Linux, you may need to install `tkinter`:
>
> ```bash
> sudo apt install python3-tk
> ```

## 📅 Use Cases

- Testing local HTML websites
- Educational use and lab assignments
- Quick HTML project sharing over a network
- Server with basic access control

# 📡 Local HTTP Server with IP Blocking

Python-скрипт для запуска локального HTTP-сервера с возможностью блокировки IP-адресов, установки сообщения блокировки и автоматической перезагрузки страницы для заблокированных IP.

## 🛋️ Возможности

- Запуск HTTP-сервера в выбранной директории
- Блокировка/разблокировка IP-адресов
- Пользовательское сообщение при блокировке
- Автоматическая перезагрузка страницы для заблокированных
- Логирование HTTP-запросов

## 🚀 Запуск

1. Убедитесь, что у вас установлен Python 3
2. Скачайте или склонируйте репозиторий
3. Запустите скрипт:

```bash
python main.py
```

4. Выберите директорию с HTML/файлами
5. Сервер будет доступен по адресу `http://<IP>:8000`

## ⚙️ Управление через консоль

- `block <IP>` — заблокировать IP
- `unblock <IP>` — разблокировать IP
- `set_msg <текст>` — установить сообщение блокировки
- `set_refresh <секунды>` — установить интервал обновления страницы
- `exit` — выход из программы

## 📦 Зависимости

Все библиотеки используются из стандартной библиотеки Python:

- `http.server`
- `socketserver`
- `os`
- `threading`
- `socket`
- `tkinter`

> ⚠️ На Linux возможно понадобится доустановка `tkinter`:
> ```bash
> sudo apt install python3-tk
> ```

## 📅 Применение

- Тестирование локальных HTML-сайтов
- Обучение и лабораторные работы
- Быстрая демонстрация HTML-проектов в сети
- Сервер с контролем доступа
 
