baris = int(input("masukkan baris lampu : "))
lampu_perbaris = int(input("masukkan jumlah lampu per baris :"))

for i in range(1, baris + 1):
    print(f"memeriksa baris{i}")
    for j in range(1, lampu_perbaris + 1):
        if j % 3 == 0:
            print(f"lampu{j}: mengalami gangguan")
        else:
            print(f"lampu{j}: berfungsi normal")
print("harap memeriksa sumber listrik utama taman")