print("\033[0:34m-=-\033[m" * 30)
# ENTRADA
valor = float(input("Qual o valor da compra? R$ ").strip())
pag = int(input("""Escolha o método de pagamento:
1. A vista dinheiro ou pix.
2. A vista no cartão.
3. Até 2X no cartão.
4. 3X ou mais no cartão.""").strip())

# SAIDA
print("\033[0:34m-=-\033[m" * 30)
if pag == 1:
    total = valor - (valor * 10 / 100)
    print("Você ganhou 10% de desconto e irá pagar R$ {:.2f}!!".format(total))
elif pag == 2:
    total = valor - (valor * 5 / 100)
    print("Você ganhou 5% de desconto e irá pagar R$ {:.2f}!!".format(total))
elif pag == 3:
    print("Você irá pagar R$ {:.2f}!!".format(valor))
elif pag == 4:
    total = valor + (valor * 20 / 100)
    print("Você pagará com 20% de juros e irá pagar R$ {:.2f}!!".format(total))
else:
    print("Método invalido tente novamente!!")