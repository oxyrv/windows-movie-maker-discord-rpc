import psutil
import win32gui
import win32process
import json
from pypresence import Presence
from pypresence.types import ActivityType
import time

with open("config.json", "r") as cfg_file:
    cfg_data = json.load(cfg_file)

def config(data):
    return cfg_data.get(data, "")

class cfg:
    client_id = config('client_id')

rpc = Presence(cfg.client_id)
rpc.connect()

def get_window_title_by_pid(target_pid):
    titles = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            if pid == target_pid:
                title = win32gui.GetWindowText(hwnd)
                if title:
                    titles.append(title)

    win32gui.EnumWindows(enum_handler, None)
    return titles

def moviemaker():
    pid = None

    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and proc.info['name'].lower() == "moviemaker.exe":
            pid = proc.info['pid']
            break

    if not pid:
        print("[X] Windows Movie Maker 2012 isn't started.")
        rpc.clear()
        return

    titles = get_window_title_by_pid(pid)

    if not titles:
        print("[!] Proccess found but no window detected.")
    else:
        msg = "\n".join(f"{t}" for t in titles)
        print(f"[+] Found Movie Maker: {msg}")
        msg = msg.replace(" - Movie Maker", "")
        rpc.update(
            activity_type=ActivityType.PLAYING,
            state=f"Working on: {msg}",
            details="Windows Movie Maker 2012",
            large_image='wmm',
            large_text=f"Windows Movie Maker 2012"
        )

try:
    while True:
        moviemaker()
        time.sleep(15)
except KeyboardInterrupt:
    rpc.clear()
    rpc.close()
    print("\nWMM-RPC has been terminated.")