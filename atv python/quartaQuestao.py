#4 - Construa uma Fila de Prioridade utilizando a linguagem Python em que 
# sejam implementadas as funções para inserção de um novo elemento (inteiro) na fila e a remoção do elemento de mais alta prioridade 
import numpy as np

class FilaPrioridade:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.n_elementos = 0
    self.valores = np.empty(self.capacidade, dtype=int)

  def __fila_vazia(self):
    return self.n_elementos == 0

  def __fila_cheia(self):
    return self.n_elementos == self.capacidade 
  
  def enfileirar(self, valor):
    if self.__fila_cheia():
      print('A fila está completa')
      return
    
    if self.n_elementos == 0:
      self.valores[self.n_elementos] = valor
      self.n_elementos += 1
    else:
      x = self.n_elementos - 1
      while x >= 0:
        if valor > self.valores[x]:
          self.valores[x + 1] = self.valores[x]
        else:
          break
        x -= 1
      self.valores[x + 1] = valor
      self.n_elementos += 1

  def desenfileirar(self):
    if self.__fila_vazia():
      print('A fila está vazia')
      return

    valor = self.valores[self.n_elementos - 1]
    self.n_elementos -= 1
    return valor     
  
  def primeiroConsultar(self):
    if self.__fila_vazia():
      return -1
    return self.valores[self.n_elementos - 1]