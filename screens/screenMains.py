import tkinter as tk
from googletrans import Translator
import speech_recognition as sr

import utils.utils
from screens.screenEditar import ScreenEditar


def open_editor():
   editor = ScreenEditar()
   editor.mainloop()

main_width, main_height, top_most, resizable_width, resizable_height, language_size, you_language_size, move_main, you_language, translate = utils.utils.load_config()

flag = True

class ScreenMain():
    def __init__(self, root):
        self.root = root
        # Deixa tela sempre na frente
        root.attributes("-topmost", top_most)
        # MODO DARK
        root["bg"] = "black"
        # Titulo
        root.title("Learn Language")

        # Não deixa redimensionar tela
        root.resizable(resizable_width, resizable_height)
        # Pega o tamanho da tela
        screen_width, screen_height = utils.utils.get_screen_size()

        # TAMANHO DA TELINHA EM SI
        window_width = main_width
        window_height = main_height

        # centralizar
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = 0

        # Desativa o movimento da janela
        root.overrideredirect(True)

        # Definir coordenadas para centralizar
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, int(x_coordinate), int(y_coordinate)))

        # Imagens para colocar botoes frames etc...
        self.img_editor = tk.PhotoImage(file='resources/icon-editor.png')
        self.img_sem_mic = tk.PhotoImage(file='resources/sem-mic.png')
        self.img_com_mic = tk.PhotoImage(file='resources/com-microfone.png')

        # Coloca o botão para fechar
        self.btn = tk.Button(root, text="X", command=self.on_closing)
        self.btn.pack(side=tk.RIGHT)
        self.btn.config(bg="black", fg="white", bd=0, font=("Helvetica", 10, "bold"))

        # Botao de editar
        self.btn_editor = tk.Button(root, image=self.img_editor, bg="black", command=open_editor)
        self.btn_editor.pack(side=tk.RIGHT)
        self.btn_editor.config(bg="black", bd=0)

        # Microfone Label Verde gravando audio, vermelho esta traduzindo e nao esta graavando
        self.label_listerning = tk.Label(root, image=self.img_sem_mic, bg="black")
        self.label_listerning.pack(side=tk.LEFT, padx=10, pady=10)

        # Audio Traduzido
        self.label = tk.Label(root, text="OUVINDO:", fg="white", bg="black", font=("Helvetica", language_size, "bold"))
        self.label.pack()

        # Audio Falado
        self.label_pt = tk.Label(root, text="", fg="white", bg="black", font=("Helvetica", you_language_size, "bold"))
        self.label_pt.pack()

    def transcribe_audio(self):
        # Inicializa o reconhecedor de fala
        r = sr.Recognizer()

        # Obtém o áudio a partir do microfone
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 1800
            self.label_listerning.config(image=self.img_com_mic)
            audio = r.listen(source)

        # Reconhece o áudio
        try:
            self.label_listerning.config(image=self.img_sem_mic)
            text = r.recognize_google(audio, language=you_language)
            # converte o texto em lista para validar se oque foi dito é muito grande
            words = text.split()
            if len(words) >= 17:
                #pega so as 17 palavras ditas
                text = " ".join(words[:17])

            if text:
                label_ptbr = text
                translator = Translator()
                text = translator.translate(text, dest=translate).text
                self.label_pt.config(text=label_ptbr)
                self.label.config(text=text)
        except sr.UnknownValueError:
            self.label.config(text="Não foi possível entender o que você disse")
            self.label_pt.config(text="")
        except sr.RequestError as e:
            self.label.config(text="Erro ao fazer a requisição ao Google Speech Recognition service")
            self.label_pt.config(text="")

    def on_closing(self):
        global flag
        flag = False
        self.root.destroy()
        print("Closing")
    def start_transcribing(self):
        global flag
        while flag:
            self.transcribe_audio()
