import tkinter as tk

from utils import utils
from utils.utils import save_config


class ScreenEditar(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        # Titulo
        self.title('EDITOR')

        # MODO DARK
        self["bg"] = "black"

        # Desativa o movimento da janela
        self.overrideredirect(True)

        # Não deixar Redimensionar
        self.resizable(False, False)

        # Deixa tela sempre na frente
        self.attributes("-topmost", True)

        # Configuracao de tamanho e local aonde a janela nasce
        win_config_width = 500
        win_config_height = 500

        # CENTRALIZAR NO MEIO DA TELA
        screen_width, screen_height = utils.get_screen_size()
        wind_x_coord = (screen_width / 2) - (win_config_width / 2)
        wind_y_coord = (screen_height / 2) - (win_config_height / 2)

        # Tamanho da Janela e aonde vai ficar a janela
        self.geometry("{}x{}+{}+{}".format(win_config_width, win_config_height, int(wind_x_coord), int(wind_y_coord)))

        # imagens
        self.imgSave = tk.PhotoImage(file='./resources/icon-salvar.png')

        # Botao salvar
        btnSave = tk.Button(self, command=self.on_save, image=self.imgSave)
        btnSave.pack(side=tk.RIGHT)
        btnSave.config(bg="black", bd=0)

    def on_save(self):
        save_config()
        self.destroy()



# main_width, main_height, color_main, color_edit, top_most, resizible_width, resizible_height, language_size, you_language_size, move_main, you_language, translate = load_config()
# apply_config(main_width, main_height, color_main, color_edit, top_most, resizible_width, resizible_height, language_size, you_language_size, move_main, you_language, translate)