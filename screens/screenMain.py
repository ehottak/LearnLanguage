import tkinter as tk
from googletrans import Translator
import speech_recognition as sr
from utils import utils
from screens.screenEditar import ScreenEditar

flag = True

class ScreenMain():
    def __init__(self, root):
        self.root = root

        self.load_config()
        self.move_windown = self.move == "False"
        # Deixa tela sempre na frente
        root.attributes("-topmost", True)
        # MODO DARK
        root["bg"] = "black"
        # Titulo
        root.title("Learn Language")

        # Não deixa redimensionar tela
        root.resizable(self.resizable_width, self.resizable_height)
        # Pega o tamanho da tela
        screen_width, screen_height = utils.get_screen_size()

        # TAMANHO DA TELINHA EM SI
        self.window_width = self.main_width
        self.window_height = self.main_height

        # centralizar
        self.x_coordinate = (screen_width / 2) - (self.window_width / 2)
        self.y_coordinate = 0

        # Desativa o movimento da janela
        self.root.overrideredirect(self.move_windown)

        # Definir coordenadas para centralizar
        root.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, int(self.x_coordinate), int(self.y_coordinate)))

        # Imagens para colocar botoes frames etc...
        self.img_editor = tk.PhotoImage(file='resources/icon-editor.png')
        self.img_sem_mic = tk.PhotoImage(file='resources/sem-mic.png')
        self.img_com_mic = tk.PhotoImage(file='resources/com-microfone.png')

        # Coloca o botão para fechar
        self.btn = tk.Button(root, text="X", command=self.on_closing)
        self.btn.pack(side=tk.RIGHT)
        self.btn.config(bg="black", fg="white", bd=0, font=("Helvetica", 10, "bold"))

        # Botao de editar
        self.btn_editor = tk.Button(root, image=self.img_editor, bg="black", command=self.open_editor)
        self.btn_editor.pack(side=tk.RIGHT)
        self.btn_editor.config(bg="black", bd=0)

        # Microfone Label Verde gravando audio, vermelho esta traduzindo e nao esta graavando
        self.label_listerning = tk.Label(root, image=self.img_sem_mic, bg="black")
        self.label_listerning.pack(side=tk.LEFT, padx=10, pady=10)

        # Audio Traduzido
        self.label = tk.Label(root, text="OUVINDO:", fg="white", bg="black",
                              font=("Helvetica", self.language_size, "bold"))
        self.label.pack()

        # Audio Falado
        self.label_pt = tk.Label(root, text="", fg="white", bg="black",
                                 font=("Helvetica", self.you_language_size, "bold"))
        self.label_pt.pack(side=tk.BOTTOM)

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
            text = r.recognize_google(audio, language=self.you_language)
            print(self.you_language)
            # converte o texto em lista para validar se oque foi dito é muito grande
            words = text.split()
            if len(words) >= 17:
                # pega so as 17 palavras ditas
                text = " ".join(words[:17])

            if text:
                label_ptbr = text
                translator = Translator()
                text = translator.translate(text, dest=self.translate).text
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


    def on_save(self):
        self.load_config()
        self.on_save_config()


    def start_transcribing(self):

        global flag
        while flag:
            self.transcribe_audio()

    def open_editor(self):
        editor = ScreenEditar(self)
        editor.mainloop()

    def load_config(self):
        self.main_width, self.main_height, self.move, self.resizable_width, self.resizable_height, self.language_size, self.you_language_size, self.move_main, self.you_language, self.translate = utils.load_config()

        return self.main_width, self.main_height, self.move, self.resizable_width, self.resizable_height, self.language_size, self.you_language_size, self.move_main, self.you_language, self.translate

    def on_save_config(self):
        main_width, main_height, move, resizable_width, resizable_height, language_size, you_language_size, move_main, you_language, translate = self.load_config()
        screen_width, screen_height = utils.get_screen_size()
        x_coordinate = (screen_width / 2) - (main_width / 2)
        self.root.geometry("{}x{}+{}+{}".format(main_width, main_height, int(x_coordinate), int(0)))
        self.label_pt.config(font=("Helvetica", you_language_size, "bold"))
        self.label.config(font=("Helvetica", language_size, "bold"))
        self.move_windown = move == "False"
        self.root.overrideredirect(self.move_windown)



