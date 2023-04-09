from kivy.app import App
# from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Pessoa:
    def __init__(self, nome, pontos=0):
        self.nome = nome
        self.pontos = pontos


class Jogo(GridLayout):
    def __init__(self, **kwargs):
        super(Jogo, self).__init__(**kwargs)

        self.cols = 2

        self.jogadores = []

        self.cont = 0
        self.add_widget(Label(text="Quantos jogadores?"))
        self.qtd_jogadores = TextInput(input_filter=int)
        self.qtd_jogadores_int = self.qtd_jogadores.text
        self.add_widget(self.qtd_jogadores)
        print(type(self.cont))

        while (self.cont < self.qtd_jogadores_int):
            self.add_widget(Label(text="Qual o nome do jogador?"))
            self.jogador = TextInput(input_filter=int)
            self.jogadores.append(Pessoa(self.jogador))
            self.cont += 1


class Jogando(App):
    def build(self):
        return Jogo()


if __name__ == "__main__":
    Jogando().run()

'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        self.qtd_jogadores = TextInput(
            text='Quantos jogadores?'
        )
        submit = Button(text='Submit', on_press=self.submit)
        layout.add_widget(self.qtd_jogadores)
        layout.add_widget(submit)
        return layout

    def submit(self, obj):
        print("Jogadores: " + self.qtd_jogadores.text)


MainApp().run()
'''
