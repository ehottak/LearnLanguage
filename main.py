import tkinter as tk
from googletrans import Translator
import speech_recognition as sr
import threading


def transcribe_audio():
    # Inicializa o reconhecedor de fala
    r = sr.Recognizer()

    # Obtém o áudio a partir do microfone
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 1800
        labelListerning.config(image=imgCMic)
        audio = r.listen(source)

    # Reconhece o áudio
    try:
        labelListerning.config(image=imgSMic)
        text = r.recognize_google(audio, language='pt-BR')
        if text:
            labelPtBr = text
            translator = Translator()
            text = translator.translate(text, dest='en').text
            labelpt.config(text=labelPtBr)
            label.config(text=text)
    except sr.UnknownValueError:
        label.config(text="Não foi possível entender o que você disse")
        labelpt.config(text="")
    except sr.RequestError as e:
        label.config(text="Erro ao fazer a requisição ao Google Speech Recognition service")
        labelpt.config(text="")


def toggle_window_movement(event=None):
    # Alterna o estado de movimento da janela
    global window_movement_enabled
    window_movement_enabled = not window_movement_enabled
    root.overrideredirect(not window_movement_enabled)


def start_transcribing():
    while True:
        transcribe_audio()


root = tk.Tk()

# Deixa tela sempre na frente
root.attributes("-topmost", True)
# MODO DARK
root["bg"] = "black"
# Pega o tamanho da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# TAMANHO DA TELINHA EM SI
window_width = 1000
window_height = 50

# centralizar
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = 0

# Desativa o movimento da janela
window_movement_enabled = False
root.overrideredirect(True)

# Definir coordenadas para centralizar
root.geometry("{}x{}+{}+{}".format(window_width, window_height, int(x_coordinate), int(y_coordinate)))

btn = tk.Button(root, text="X", command=toggle_window_movement)

# Coloca o botão no canto inferior direito da janela
btn.pack(side=tk.RIGHT, anchor=tk.N)
btn.config(bg="black", fg="white", bd=0)

imgSMic = tk.PhotoImage(file='sem-mic.png')
imgCMic = tk.PhotoImage(file='com-microfone.png')

labelListerning = tk.Label(root, image=imgSMic, bg="black")
labelListerning.pack(side=tk.LEFT, anchor=tk.N)

label = tk.Label(root, text="OUVINDO:", fg="white", bg="black")
label.pack()

labelpt = tk.Label(root, text="", fg="white", bg="black")
labelpt.pack()

if __name__ == '__main__':
    thread = threading.Thread(target=start_transcribing)
    thread.start()
    root.mainloop()
