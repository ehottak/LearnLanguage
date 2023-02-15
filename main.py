import tkinter as tk
import threading
from screens.screenMain import ScreenMain
import sys
import os


MAX_FILE_SIZE = 5000000  # 5MB

if os.path.exists("log.log") and os.stat("log.log").st_size > MAX_FILE_SIZE:
    os.remove("log.log")

if __name__ == '__main__':
    sys.stdout = open("log.txt", "w")
    sys.stderr = open("log.txt", "w")
    root = tk.Tk()
    mainTela = ScreenMain(root)
    root.protocol("WM_DELETE_WINDOW", mainTela.on_closing)
    thread = threading.Thread(target=mainTela.start_transcribing, daemon=True)
    thread.start()
    root.mainloop()
    sys.stdout.close()
    sys.stderr.close()
