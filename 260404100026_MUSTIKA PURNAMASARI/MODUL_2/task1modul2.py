kode = int(input("masukkan password 3 digit: "))

digit_1 = kode // 100
digit_2 = (kode // 10) % 10
digit_3 = kode % 10

nilai_awal = digit_1 * digit_3

if digit_2 % 2 == 1:
    nilai_tahap1 = nilai_awal + 25
else:
    nilai_tahap1 = nilai_awal - digit_2

if nilai_tahap1 % 3 == 0:
    nilai_akhir = nilai_tahap1 // 3
else:
    nilai_akhir = nilai_tahap1 * 2

if nilai_akhir > 50:
    kategori = "kategori A"
elif nilai_akhir > 20:
    kategori = "kategori B"
else:
    kategori = "password ditolak"

if nilai_akhir % 2 == 0:
    siklus = "genap"
else:
    siklus = "ganjil"

print(f"digit anda: ", digit_1, digit_2, digit_3)
print(f"nilai pelacak awal : ",nilai_awal)
print(f"nilai pelacak setelah perubahan pertama: ",nilai_tahap1)
print(f"nilai pelacak setelah perubahan kedua: ",nilai_akhir)
print(f"status password: ",kategori)
print(f"siklus pelacak: ",siklus)