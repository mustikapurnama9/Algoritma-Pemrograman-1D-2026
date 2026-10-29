total_gaji = 0

for i in range(1,2):
    print(f"data hari ke-{i}")

    while True:
        lembur = int(input("masukkan jam lembur(1-8):"))
        if 0 < lembur <= 8:
            break
        print("jam lembur tidak sesuai ketentuan. masukkan ulang") 

    shift_malam = input("apakah shift malam? (y/t)")

    gaji_harian = 100000
    if shift_malam == 'y':
        gaji_harian + 50000

    if 1 <= lembur <= 3:
        gaji_harian += (lembur * 25000)
    elif 4 == lembur:
        gaji_harian += 100000
    elif 6 == lembur:
        gaji_harian += 200000
    elif 8 == lembur:
        gaji_harian += 300000
    elif lembur > 8:
        print("jumlah lembur melebihi batas, tidak dihitung")

    total_gaji += gaji_harian

print(f"total gaji mingguan {total_gaji}")