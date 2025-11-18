n = int(input("Quantos numeros quer colocar? "))
num = []
for c in range(0, n):
    n1 = int(input("Quais são os numeros: "))
    num.append(n1)
pares = sum(n for n in num if n % 2 == 0)
print(pares)