
# Meminta tinggi setengah menara
n = int(input("Masukkan tinggi setengah menara (2-15): "))

while n < 2 or n > 15:
    print("Tinggi tidak valid! Masukkan angka 2 sampai 15.")
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

# Bagian atas: membesar
for i in range(1, n + 1):
    # Membuat spasi agar rata tengah
    print(" " * (n - i), end="")

    # Angka naik dari 1 sampai i
    for j in range(1, i + 1):
        print(j % 10, end="")

    # Angka turun kembali ke 1
    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

# Bagian bawah: mengecil
for i in range(n - 1, 0, -1):
    # Membuat spasi agar rata tengah
    print(" " * (n - i), end="")

    # Angka naik dari 1 sampai i
    for j in range(1, i + 1):
        print(j % 10, end="")

    # Angka turun kembali ke 1
    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()
