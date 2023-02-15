import tkinter as tk

from utils import utils


class ScreenCredit(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="black")
        self.pack(fill='both', expand=True)
        screen_width, screen_height = utils.get_screen_size()
        screen_width = screen_width / 2
        screen_height = screen_height / 2
        master.winfo_toplevel().geometry("{}x{}".format(int(screen_width),int(screen_height)))
        self.create_widgets()

    def create_widgets(self):
        texto = 'Prazer Usuário! Meu nome é Eduardo Hotta e sou o criador deste programa incrível que você está usando' \
                '.\n\n\nA ideia por trás dele é bem simples: você fala, ele traduz e mostra na tela a tradução para a língua que você escolher.\n\n\n'\
                'O objetivo é ajudar você a aprender a escrita e a leitura.A criação deste programa foi um projeto solo que começou em 2023.\n\n\n' \
                'Agora que está pronto, estou muito animado em compartilhar com você e ajudá-lo a alcançar seus objetivos linguísticos.\n\n\n' \
                'Espero que você aproveite ao máximo todas as funcionalidades do programa e que ele seja útil em sua jornada de aprendizado.\n\n\n'\
                'Obrigado por usá-lo e bons estudos!'
        # Texto com as informações do programa
        self.info_label = tk.Label(self, text=texto, font=('Arial', 15), justify='center', fg='white', bg='black')
        self.info_label.config(padx=10, pady=10)
        self.info_label.pack(side='top', pady=10)
        # Configurações de animação
        self.text_y = self.winfo_height() + 500  # Inicia o texto acima da janela
        self.text_dy = -1  # Velocidade de movimento do texto
        self.after(10, self.update_text)  # Inicia o loop de animação

    def update_text(self):
        # Atualiza a posição do texto
        self.text_y += self.text_dy
        if self.text_y < -self.info_label.winfo_height():
            self.text_y = self.winfo_height() + 100  # Reposiciona o texto acima da janela quando chegar ao fim
        self.info_label.place(relx=0.5, rely=0, y=self.text_y, anchor='n')
        # Chama a função novamente em 20 milissegundos para criar o efeito de animação
        self.after(20, self.update_text)

