pt = int(input("Estrva o primeiro termo da PA: ").strip())
ut = int(input("Estrva o último termo da PA: ").strip())
r = int(input("Escreva a razão da PA: ").strip())

for c in range(pt, ut, r):
    print(c)