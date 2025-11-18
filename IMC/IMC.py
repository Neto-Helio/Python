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