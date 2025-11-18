print("Seja bem vindo ao menu de programas do Helio Neto")
escolha = int(input("""
Escolha qual programa gostaria de ver:
0. Tabuada
1. Termo e razão de uma PA
2. Soma de números pares
3. Comtagem regressiva
4. Jokenpo
5. Contagem de desconto
6. IMC
7. Formação de triangulo
Escolha: """))
print("~" *50)

if escolha == 0: # Tabuada
    n1 = int(input("Digite qual tabuada queira ver: "))
    for c in range(0, 11):
        print('{} x {} = {}'.format(n1, c, n1 * c))
#**************************************************************************************
elif escolha == 1: #Termo e razão de uma PA
    pt = int(input("Estrva o primeiro termo da PA: ").strip())
    ut = int(input("Estrva o último termo da PA: ").strip())
    r = int(input("Escreva a razão da PA: ").strip())

    for c in range(pt, ut, r):
        print(c)
#**************************************************************************************
elif escolha == 2: #Soma de números pares
    n = int(input("Quantos numeros quer colocar? "))
    num = []
    for c in range(0, n):
        n1 = int(input("Quais são os numeros: "))
        num.append(n1)
    pares = sum(n for n in num if n % 2 == 0)
    print(pares)
#**************************************************************************************
elif escolha == 3: #Contagem regressiva
    from time import sleep

    for c in range(10, 0, -1):
        if c > 5:
            print("\033[:31m {}".format(c))
        else:
            print("\033[:32m {}".format(c))
        sleep(1)
    print("FELIZ ANO NOVOO!! 🎆🎆")
#**************************************************************************************
elif escolha == 4: #JOKENPO
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
    sleep(0.5)
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
#**************************************************************************************
elif escolha == 5: #Contagem de desconto
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
#**************************************************************************************
elif escolha == 6: #IMC
    print("\033[0:34m-=-\033[m" * 30)

    # ENTRADA
    alt = float(input("Escreva sua altura: ").strip())
    peso = float(input("Escreva seu peso: ").strip())

    # CALCULOS
    imc = peso / (alt ** 2)

    # SAIDA
    if imc <= 18.4:
        print(
            "Com sua altura de {} e seu peso de {}Kg o valor do seu IMC é de: {:.1f} sendo assim estando abaixo do peso!".format(
                alt, peso, imc))
    elif imc >= 18.5 and imc <= 24.9:
        print(
            "Com sua altura de {} e seu peso de {}Kg o valor do seu IMC é de: {:.1f} sendo assim estando no seu peso ideal!".format(
                alt, peso, imc))
    elif imc >= 25 and imc <= 29.9:
        print(
            "Com sua altura de {} e seu peso de {}Kg o valor do seu IMC é de: {:.1f} sendo assim estando sobre peso!".format(
                alt, peso, imc))
    elif imc >= 30 and imc <= 39.9:
        print(
            "Com sua altura de {} e seu peso de {}Kg o valor do seu IMC é de: {:.1f} sendo assim estando com obesidade!".format(
                alt, peso, imc))
    elif imc >= 40:
        print(
            "Com sua altura de {} e seu peso de {}Kg o valor do seu IMC é de: {:.1f} sendo assim estando com obesidade morbida!".format(
                alt, peso, imc))
#**************************************************************************************
elif escolha == 7: #Formação de triangulo
    print("\033[0:34m-=-\033[m" * 30)
    # ENTRADA
    a = float(input("Escreva valor de A: ").strip())
    b = float(input("Escreva valor de B: ").strip())
    c = float(input("Escreva valor de C: ").strip())
    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c and b == c:
            print("Pode ser formado um Triangulo Equilátero")
        elif a == b or a == c or b == c:
            print("Pode ser formado um Triangulo Isósceles")
        else:
            print("Pode ser formado um Triangulo Escaleno")
    else:
        print("Não pode ser formado um Tringulo")
    print("\033[0:34m-=-\033[m" * 30)
