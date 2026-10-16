jarak_rumah_luar_kota = int(input("masukkan data"))
km_per_liter = 40
harga_1_liter = 10000
bahan_bakar_dimas = 1.5


perjalanan_pulang_pergi = jarak_rumah_luar_kota + jarak_rumah_luar_kota

total_bahan_bakar = perjalanan_pulang_pergi / km_per_liter

bahan_bakar_dibeli = total_bahan_bakar - bahan_bakar_dimas

total_biaya = bahan_bakar_dibeli * harga_1_liter

print("Perjalanan yang ditempuh :", perjalanan_pulang_pergi, "km")
print("Total bahan bakar keseluruhan :", total_bahan_bakar, "liter")
print("Jumlah bahan bakar yang harus dibeli :", bahan_bakar_dibeli, "liter")
print("Total biaya yang dikeluarkan :", total_biaya)
