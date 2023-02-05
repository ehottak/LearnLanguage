import json
import tkinter as tk

def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def save_config(main_width, main_height, color_main, color_edit, top_most, resizable_width, resizable_height, language_size, you_language_size, move_main, you_language, translate):
    config = {
        "main_width": main_width,
        "main_height": main_height,
        "color_main": color_main,
        "color_edit": color_edit,
        "top_most": top_most,
        "resizable_width": resizable_width,
        "resizable_height": resizable_height,
        "language_size": language_size,
        "you_language_size": you_language_size,
        "move_main": move_main,
        "you_language": you_language,
        "translate": translate
    }

def load_config():
    with open("config.cfg", "r") as f:
        config = json.load(f)

    main_width = config["main_width"]
    main_height = config["main_height"]
    color_main = config["color_main"]
    color_edit = config["color_edit"]
    top_most = config["top_most"]
    resizable_width = config["resizable_width"]
    resizable_height = config["resizable_height"]
    language_size = config["language_size"]
    you_language_size = config["you_language_size"]
    move_main = config["move_main"]
    you_language = config["you_language"]
    translate = config["translate"]

    return main_width, main_height, color_main, color_edit, top_most, resizable_width, resizable_height, language_size, you_language_size, move_main, you_language, translate
