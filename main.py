jogadores = []


class Pessoa:
    def __init__(self, nome, pontos=0):
        self.nome = nome
        self.pontos = pontos


# Adicionando dinâmicamente os jogadores
cont = 0
qtd_jogadores = int(input('Quantos jogadores? '))

while cont < qtd_jogadores:
    jogador = input('Qual o nome do jogador? ')
    jogadores.append(Pessoa(jogador))
    cont += 1

# Conferindo se o jogador acertou


def acertou():
    cont = 0
    while cont < qtd_jogadores:
        pontos_ate_o_momento = jogadores[cont].pontos
        print(jogadores[cont].nome)
        resposta = input('Acertou? s(Sim) n(Não): ').lower()
        if resposta == 's':
            pedidas = int(input('Quantas acertou?: '))
            pontos = 5 + pedidas
            jogadores[cont].pontos = pontos_ate_o_momento + int(pontos)
            print(
                f'{jogadores[cont].nome} está com {jogadores[cont].pontos}'
                ' pontos.')
            cont += 1
        elif resposta == 'n':
            print(f'{jogadores[cont].nome} está com {jogadores[cont].pontos}'
                  ' pontos.')
            cont += 1

# Mostrando os pontos de cada jogador


def mostraPontos():
    cont = 0
    while cont < qtd_jogadores:
        print(f'{jogadores[cont].nome} {jogadores[cont].pontos} pontos.')
        cont += 1

# Jogando


def jogando():

    cont = 0
    while cont < qtd_jogadores:
        print(f'Olá {jogadores[cont].nome}, bem vindo ao jogo.')
        cont += 1

    jogar = 's'
    while jogar == 's':
        acertou()
        mostraPontos()
        jogar = input('Tem mais alguma rodada? s(Sim) n(Não): ').lower()

    print('O jogo acabou.')
    mostraPontos()


jogando()
