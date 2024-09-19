# Usando o laço for
for andar in range(20, 0, -1):
    if andar == 13:
        continue  # Pular o 13º andar
    print(andar)


# Usando o laço while
andar = 20
while andar > 0:
    if andar != 13:
        print(andar)
    andar -= 1