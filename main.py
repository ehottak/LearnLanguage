import tkinter as tk
import threading
from screens.screenMains import ScreenMain



if __name__ == '__main__':
    root = tk.Tk()
    mainTela = ScreenMain(root)
    root.protocol("WM_DELETE_WINDOW", mainTela.on_closing)
    thread = threading.Thread(target=mainTela.start_transcribing)
    thread.setDaemon(True)
    thread.start()
    root.mainloop()
