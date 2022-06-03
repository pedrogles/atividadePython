# 1 - Construa uma Pilha utilizando a linguagem Python. Dada uma sequência contendo N (N>0) números inteiros, imprimi-la na ordem inversa.

seq = []
while True:
    n = int(input())
    if (n > 0):
        seq.append(n)
    else:
        break

for i in seq[::-1]:
    print (i)