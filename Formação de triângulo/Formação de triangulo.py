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
