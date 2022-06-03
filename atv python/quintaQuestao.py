#5 - Escreva um programa em Python que simule o controle de uma pista de decolagem de aviões em um aeroporto. Neste programa, o usuário deve ser capaz de realizar as seguintes tarefas: 
#Listar o número de aviões aguardando na fila de decolagem;
#Autorizar a decolagem do primeiro avião da fila;
#Adicionar um avião à fila de espera;
#Listar todos os aviões na fila de espera;
#Listar as características do primeiro avião da fila.
import numpy as np

class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numeroElementos = 0
        self.valores = np.empty(self.capacidade, dtype=dict)

    def filaVazia(self):
        return self.numeroElementos == 0

    def filaCheia(self):
        return self.numeroElementos == self.capacidade

    def enfileirar(self, valor):
        if self.filaCheia():
            print('A fila está completa')
        else:
            self.valores[self.numeroElementos] = valor
            self.numeroElementos += 1

    def desenfileirar(self):
        if self.filaVazia():
            print('A fila está vazia')
        else:
            for x in range(self.numeroElementos - 1):
                temp = self.valores[x + 1]
                self.valores[x + 1] = None
                self.valores[x] = temp
            self.numeroElementos -= 1

    def primeiro(self):
        if self.filaVazia():
            return -1
        else:
            return self.valores[self.inicio]

def colorindoLinha(): 
    print("\033[43m☺☻\033[m"*15)

def tratarErro():
    print("\033[1;31mOpção inválida. Tente novamente!\033[m")


print("\033[31m -- AEROPORTO CASTOR PLINO -- \033[m")

while True:
    try:
        colorindoLinha()
        qtd = int(input("Quantos aviões DESEJA incluir na pista (digite o número):"))
        break
    except:
        tratarErro()
fila = Fila(qtd)


while True:
    while True:
        try:
            colorindoLinha()
            print("---- SELECIONE UMA DAS OPÇÕES ----")
            print("1 - Listar o número de aviões que estão na fila.")
            print("2 - Autorizar a decolagem do primeiro avião da fila.")
            print("3 - Adicionar um avião à fila de espera.")
            print("4 - Listar todos os aviões na fila de espera.")
            print("5 - Listar as características do primeiro avião da fila.")
            print("6 - Tchauzinho.")
            escolha = int(input("Digite a opção (o número): "))
            break
        except:
            tratarErro()
    print()

    if escolha == 1:
        if fila.filaVazia():
            print("A fila está vazia!")
        else:
            print(f"Aviões na fila: {fila.numeroElementos}")


    elif escolha == 2:
        if fila.filaVazia():
            print("A fila está vazia!")
        else:
            print(f"Avião número {fila.valores[0]['Número']} Maverick no AR...")
            fila.desenfileirar()


    elif escolha == 3:
        if fila.filaCheia():
            print("A fila está cheia!")
        else:
            print("CRIE OS DADOS DO AVIÃO:")
            while True:
                try:
                    numero = int(input("Número do avião: "))
                    break
                except:
                    tratarErro()
            while True:
                try:
                    descricao = str(input("Descrição: "))
                    break
                except:
                    tratarErro()
            aviao = {'Número': numero, 'Descrição': descricao}
            fila.enfileirar(aviao.copy())


    elif escolha == 4:
        if fila.filaVazia():
            print("A fila está vazia!")
        else:
            print("FILA DE ESPERA: ",)
            for y in range(fila.numeroElementos):
                print(f"{y+1}º: (Nº: {fila.valores[y]['Número']}, Descrição: {fila.valores[y]['Descrição']})")
            print()


    elif escolha == 5:
        if fila.filaVazia():
            print("A fila está vazia!")
        else:
            print(f"Primeiro avião da fila: (Nº: {fila.valores[0]['Número']}, Descrição: {fila.valores[0]['Descrição']})")


    elif escolha == 6:
        print("Finalizando programa...")
        break
        exit()
    else:
        tratarErro()