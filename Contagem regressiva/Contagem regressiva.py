from time import sleep

for c in range(10, 0, -1):
    if c > 5:
        print("\033[:31m {}".format(c))
    else:
        print("\033[:32m {}".format(c))
    sleep(1)
print("FELIZ ANO NOVOO!! 🎆🎆")