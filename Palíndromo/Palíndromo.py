frase = str(input("Escreva a frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra]
print("Você digitou: {} e o inverso fica: {}".format(junto, inverso))
if inverso == junto:
    print("Esta frase é um palíndromo")
else:
    print("Esta frase não é um palíndromo")