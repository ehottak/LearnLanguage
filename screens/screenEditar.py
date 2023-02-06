import tkinter as tk

from utils import utils

main_width, main_height, top_most, resizable_width, resizable_height, language_size, you_language_size, move_main, you_language, translate = utils.load_config()


class ScreenEditar(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(ScreenEditar, self).__init__(master, **kw)
        self.resizable(False, False)
        # Pega o tamanho da tela
        screen_width, screen_height = utils.get_screen_size()

        # TAMANHO DA TELINHA EM SI
        window_width = 200
        window_height = 400

        # centralizar
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        self.title('EDIT')
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, int(x_coordinate), int(y_coordinate)))

        self.frame_width = tk.Frame(self)
        self.frame_width.configure(height=60, width=200)
        self.label_width = tk.Label(self.frame_width)
        self.label_width.configure(
            background="#000000",
            foreground="#ffffff",
            text='Width')
        self.label_width.pack(fill="x", side="top")
        self.width_scale = tk.Scale(self.frame_width, command=self.set_width)
        self.main_width = tk.IntVar()
        self.width_scale.configure(
            background="#000000",
            foreground="#ffffff",
            from_=1000,
            highlightbackground="#000000",
            highlightcolor="#000000",
            orient="horizontal",
            to=2560,
            troughcolor="#ffffff",
            variable=self.main_width)

        self.width_scale.pack(fill="x", side="top")
        self.frame_width.pack(side="top")
        self.frame_width.pack_propagate(0)

        self.frame_height = tk.Frame(self)
        self.frame_height.configure(height=60, width=200)
        self.label_height = tk.Label(self.frame_height)
        self.label_height.configure(
            background="#000000",
            foreground="#ffffff",
            text='Height')
        self.label_height.pack(fill="x", side="top")
        self.height_scale = tk.Scale(self.frame_height, command=self.set_height)
        self.main_height = tk.IntVar()
        self.height_scale.configure(
            background="#000000",
            foreground="#ffffff",
            from_=50,
            highlightbackground="#000000",
            highlightcolor="#000000",
            orient="horizontal",
            to=200,
            troughcolor="#ffffff",
            variable=self.main_height)
        self.height_scale.pack(fill="x", side="top")
        self.frame_height.pack(side="top")
        self.frame_height.pack_propagate(0)
        self.frame_language_translate = tk.Frame(self)
        self.frame_language_translate.configure(height=60, width=200)
        self.label_language_translate = tk.Label(self.frame_language_translate)
        self.label_language_translate.configure(
            background="#000000",
            foreground="#ffffff",
            relief="flat",
            state="normal",
            text='Language Translate Size')
        self.label_language_translate.pack(fill="x", side="top")
        self.language_translate_scale = tk.Scale(self.frame_language_translate,command=self.set_size_trasnlate)
        self.language_size = tk.IntVar()
        self.language_translate_scale.configure(
            background="#000000",
            foreground="#ffffff",
            from_=2,
            highlightbackground="#000000",
            highlightcolor="#000000",
            orient="horizontal",
            to=40,
            troughcolor="#ffffff",
            variable=self.language_size)
        self.language_translate_scale.pack(fill="x", side="top")
        self.frame_language_translate.pack(side="top")
        self.frame_language_translate.pack_propagate(0)

        self.frame_you_language = tk.Frame(self)
        self.frame_you_language.configure(height=60, width=200)
        self.labe_you_language = tk.Label(self.frame_you_language)
        self.labe_you_language.configure(
            background="#000000",
            foreground="#ffffff",
            relief="flat",
            text='You Language Size')
        self.labe_you_language.pack(fill="x", side="top")
        self.you_language_scale = tk.Scale(self.frame_you_language, command=self.set_size_you_lang)
        self.you_language_size = tk.IntVar()
        self.you_language_scale.configure(
            background="#000000",
            foreground="#ffffff",
            from_=2,
            highlightbackground="#000000",
            highlightcolor="#000000",
            orient="horizontal",
            state="normal",
            takefocus=False,
            to=40,
            troughcolor="#ffffff",
            variable=self.you_language_size)
        self.you_language_scale.pack(fill="x", side="top")
        self.frame_you_language.pack(side="top")
        self.frame_you_language.pack_propagate(0)

        self.frame_moved = tk.Frame(self)
        self.frame_moved.configure(background="#000000", height=40, width=200)
        self.label_moved = tk.Label(self.frame_moved)

        self.label_moved.configure(
            background="#000000",
            foreground="#ffffff",
            relief="flat",
            text='Moved')
        self.label_moved.pack(fill="x", side="top")
        self.moved_win = tk.StringVar(value='Select')
        self.moved = tk.Menubutton(self.frame_moved)
        self.moved.menu = tk.Menu(self.moved, tearoff=0)
        self.moves=["True", "False"]

        for moved in self.moves:
            self.moved.menu.add_command(label=moved,command=lambda language=moved: self.change_move_win(moved))

        self.moved['menu'] = self.moved.menu


        self.moved.configure(
            activebackground="#ffffff",
            activeforeground="#000000",
            background="#000000",
            foreground="#ffffff",
            indicatoron=True,
            textvariable=self.moved_win,
            width=10)
        self.moved.pack(side="top")
        self.frame_moved.pack(side="top")
        self.frame_moved.pack_propagate(0)

        self.frame_ = tk.Frame(self)
        self.frame_.configure(background="#000000", height=50, width=200)
        self.label_you_language = tk.Label(self.frame_)
        self.label_you_language.configure(
            background="#000000",
            foreground="#ffffff",
            text='You Language')
        self.label_you_language.pack(fill="x", side="top")

        self.you_language = tk.StringVar(value='Select')
        self.you_language_select = tk.Menubutton(self.frame_)
        self.you_language_select.menu = tk.Menu(self.you_language_select,  tearoff=0)

        self.languages_you = utils.get_languages()

        for language in self.languages_you:
            self.you_language_select.menu.add_command(label=language,
                                                   command=lambda language=language: self.change_language_you(language))

        self.you_language_select['menu'] = self.you_language_select.menu

        self.you_language_select.configure(
            activebackground="#ffffff",
            activeforeground="#000000",
            background="#000000",
            foreground="#ffffff",
            indicatoron="true",
            textvariable=self.you_language,
            width=10)
        self.you_language_select.pack(side="top")

        self.frame_.pack(side="top")
        self.frame_.pack_propagate(0)

        self.frame_trasnlate_to = tk.Frame(self)
        self.frame_trasnlate_to.configure(
            background="#000000", height=50, width=200)
        self.label_translate_to = tk.Label(self.frame_trasnlate_to)

        self.label_translate_to.configure(
            background="#000000",
            foreground="#ffffff",
            justify="left",
            text='Trasnlate To')
        self.label_translate_to.pack(fill="x", side="top")

        self.translate_list = tk.StringVar(value='Select')
        self.translate_select = tk.Menubutton(self.frame_trasnlate_to)
        self.translate_select.menu = tk.Menu(self.translate_select, tearoff=0)

        self.languages = utils.get_translate_languages()

        for language in self.languages:
            self.translate_select.menu.add_command(label=language,
                                                   command=lambda language=language: self.change_language(language))

        self.translate_select['menu'] = self.translate_select.menu

        self.translate_select.configure(
            activebackground="#ffffff",
            activeforeground="#000000",
            background="#000000",
            foreground="#ffffff",
            indicatoron="true",
            textvariable=self.translate_list,
            width=10)

        self.translate_select.pack(side="top")

        self.frame_trasnlate_to.pack(side="top")
        self.frame_trasnlate_to.pack_propagate(0)

        self.frame_buttons = tk.Frame(self)
        self.frame_buttons.configure(
            background="#000000", height=25, width=200)
        self.save = tk.Button(self.frame_buttons)
        self.save.configure(
            background="#ffffff",
            borderwidth=0,
            justify="left",
            relief="groove",
            text='Save',
            width=10)
        self.save.pack(side="left")
        self.save.configure(command=self.on_save)
        self.cancel = tk.Button(self.frame_buttons)
        self.cancel.configure(
            background="#ffffff",
            borderwidth=0,
            justify="right",
            relief="groove",
            text='Cancel',
            width=10)
        self.cancel.pack(side="right")
        self.cancel.configure(command=self.on_cancel)
        self.frame_buttons.pack(side="top")
        self.frame_buttons.pack_propagate(0)
        self.configure(height=200, width=200)

    def on_save(self):
        # (main_width, main_height, color_main, color_edit, top_most, resizable_width, resizable_height, language_size,
        #  you_language_size, move_main, you_language, translate
        utils.save_config(self.main_width.get(), self.main_height.get())
        self.destroy()


    def on_cancel(self):
        self.destroy()

    def change_language(self, language):
        self.translate_list.set(language)
        self.master.update_idletasks()
    def change_language_you(self, language):
        self.you_language.set(language)
        self.master.update_idletasks()

    def change_move_win(self,moved):
        self.moved_win.set(moved)
        self.master.update_idletasks()

    def set_width(self, value):
        self.main_width.set(int(value))

    def set_height(self, value):
        self.main_height.set(int(value))

    def set_size_you_lang(self, value):
        self.you_language_size.set(int(value))

    def set_size_trasnlate(self, value):
        self.language_size.set(int(value))



# main_width, main_height, color_main, color_edit, top_most, resizible_width, resizible_height, language_size, you_language_size, move_main, you_language, translate = load_config()
# apply_config(main_width, main_height, color_main, color_edit, top_most, resizible_width, resizible_height, language_size, you_language_size, move_main, you_language, translate)
