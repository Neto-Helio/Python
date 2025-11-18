import random
from time import sleep

# LISTA
lista = ('Pedra', 'Papel', 'Tesoura')
# ENTRADAS
pc = random.randint(0, 2)
jogador = int(input("""Escolha sua opção:
0. Pedra
1. Papel
2. Tesoura
Escolha: """))
print("=" * 10)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
# SAIDA
print("=" * 10)
print("Computador: {}".format(lista[pc]))
print("  X")
print("Jogador: {}".format(lista[jogador]))
print("=" * 10)
# CONDIÇÕES
if pc == 0:  # Pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("Você VENCEU!!")
    elif jogador == 2:
        print("Você PERDEU!!")
if pc == 1:  # Papel
    if jogador == 0:
        print("Você PERDEU!!")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("Você VENCEU!!")
if pc == 2:  # Tesoura
    if jogador == 0:
        print("Você VENCEU!!")
    elif jogador == 1:
        print("Você PERDEU!!")
    elif jogador == 2:
        print("EMPATE")