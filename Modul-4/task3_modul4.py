

while True:
    n = int(input("masukkan bilangan bulat positif: "))

    if n >= 1:
        break
    print("masukkan ulang ,bilangan tersebut bukan bilangan positif")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for s in range(1, 2 * (n - i)+ 2):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")

    print()