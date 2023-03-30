jogadores = []


class Pessoa:

    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos


p1 = Pessoa('Gabriel', 0)
jogadores.append(p1)
p2 = Pessoa('Kleye', 0)
jogadores.append(p2)
p3 = Pessoa('Belinha', 0)
jogadores.append(p3)


def acertou():
    for i, j in enumerate(jogadores):
        pontos_ate_o_momento = jogadores[i].pontos
        resposta = input('Acertou? s(Sim) n(Não): ').lower()
        if resposta == 's':
            pedidas = int(input('Quantas acertou?: '))
            pontos = 5 + pedidas
            jogadores[i].pontos = pontos_ate_o_momento + int(pontos)
            print(jogadores[i].pontos)


def rodadas():
    jogar = 's'
    if jogar == 's':
        print('Boa rodada a todos!')
        for i, j in enumerate(jogadores):
            print(jogadores[i].nome)
            acertou()


def jogando():

    for i in jogadores:
        print(f'Olá {i.nome}, bem vindo ao jogo.')

    jogar = input('Tem mais alguma rodada? s(Sim) n(Não): ').lower()
    while jogar == 's':

        rodadas()
        jogar = input('Tem mais alguma rodada? s(Sim) n(Não): ').lower()

    print('O jogo acabou.')


jogando()
