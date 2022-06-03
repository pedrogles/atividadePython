#3 - Construa um programa em Python de acordo com situação problema descrita: Um grupo
#de soldados está cercado e não há esperança de vitória, porém existe somente um cavalo
#disponível para escapar e buscar por reforços. Para determinar qual soldado deve escapar
#para encontrar ajuda, eles formam um círculo (Fila Circular) e sorteiam um número de um
#chapéu. Começando por um soldado sorteado aleatoriamente, uma contagem é realizada
#até o número sorteado. Quando a contagem terminar, o soldado em que a contagem
#parou é removido do círculo, um novo número é sorteado e a contagem recomeça no
#soldado seguinte ao que foi eliminado. A cada rodada, portanto, o círculo diminui em um,
#até que somente um soldado reste e seja escolhido para a tarefa.

import numpy as np
from random import randint

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numeroElementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)
    
    def filaVazia(self):
        return self.numeroElementos == 0
    
    def filaCheia(self):
        return self.numeroElementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.filaCheia():
            print("A Fila está Cheia")
            return
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numeroElementos += 1

    def desenfileirar(self):
        if self.filaVazia():
            print("A Fila está Vazia")
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numeroElementos -= 1
        return temp
    
    def primeiro(self):
        if self.filaVazia():
            return -1
        return self.valores[self.inicio]

def linha():
    print("\033[1;34m-=-\033[m"*20)


def comandoInvalido():
    print("\033[1;31mOpção inválida. Tente novamente!\033[m")


print("* FILA CIRCULAR *")

while True:
    linha()
    try:
        quant = int(input("Insira a quantidade de soldados: "))
        break
    except:
        comandoInvalido()
fila = FilaCircular(quant)

linha()
for i in range(quant):
    while True:
        try:
            soldado = int(input(f"Nº de identificação do {i+1}º soldado: "))
            break
        except:
            comandoInvalido()
    fila.enfileirar(soldado)


for j in range(randint(1, 10)):
    fila.inicio += 1
    if fila.inicio == fila.capacidade:
        fila.inicio = 0
    if fila.final == fila.capacidade - 1:
        fila.final = -1
    fila.final += 1
for i in range(fila.numeroElementos - 1):
    for j in range(randint(1, 10)):
        fila.inicio += 1
        if fila.inicio == fila.capacidade:
            fila.inicio = 0
        if fila.final == fila.capacidade - 1:
            fila.final = -1
        fila.final += 1
    fila.desenfileirar()

linha()
print(f'Soldado escolhido: {fila.primeiro()}')
linha()