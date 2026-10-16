
jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = float(input("Masukkan jarak penumpang (km): "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak tidak valid, silakan masukkan ulang!")
        continue

    # Menghitung tarif berdasarkan jarak
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    # Menghitung jumlah penumpang
    jumlah_penumpang += 1

    # Diskon setiap penumpang ke-5, ke-10, dan seterusnya
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Diskon 50% diberikan!")

    # Menghitung pendapatan dan jarak
    total_pendapatan += tarif
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print("Tarif yang harus dibayar: Rp", tarif)

# Menampilkan hasil akhir
print("\n===== HASIL AKHIR =====")
print("Jumlah penumpang:", jumlah_penumpang)
print("Total pendapatan: Rp", total_pendapatan)

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print("Jarak terjauh:", jarak_terjauh, "km")
    print("Rata-rata jarak:", rata_rata, "km")
else:
    print("Jarak terjauh: 0 km")
    print("Rata-rata jarak: 0 km")
