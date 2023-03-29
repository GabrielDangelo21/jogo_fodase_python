jogadores = []


# Função para saber os nomes dos jogadores


def jogador():
    print('Bem vindo ao jogo')
    sair = ''
    while sair != 'n':
        nome_jogador = input('Nome do jogador: ')
        jogadores.append(nome_jogador)
        sair = input('Tem mais jogador? s(Sim) n(Não)')


# Função para somar pontuação
def acertou():
    pontos_ate_o_momento = 0
    resposta = input('Acertou? s(Sim) n(Não): ').lower()
    if resposta == 's':
        pedidas = int(input('Quantas acertou?: '))
        pontos = 5 + pedidas
        total_pontos = pontos_ate_o_momento + int(pontos)
        print(total_pontos)


def rodadas():
    jogar = 's'
    if jogar == 's':
        print('Boa rodada a todos!')
        for i in jogadores:
            print(i)
            acertou()

    else:
        print('O jogo acabou.')
        # for i in jogadores:
        #     print(f'{i} acabou com {pontos_iniciais}.')


def jogando():
    jogador()

    for i in jogadores:
        print(f'Olá {i}, bem vindo ao jogo.')

    jogar = input('Tem mais alguma rodada? s(Sim) n(Não): ').lower()
    while jogar == 's':

        rodadas()
        jogar = input('Tem mais alguma rodada? s(Sim) n(Não): ').lower()


jogando()
