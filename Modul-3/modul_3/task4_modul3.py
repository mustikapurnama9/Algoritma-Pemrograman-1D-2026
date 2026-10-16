kuota_penuh = 0

for i in range(10):
    if kuota_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi!")
        break

    print(f"\nMahasiswa ke-{i + 1}")
    nama = input("Nama mahasiswa: ")
    ipk = float(input("IPK: "))
    penghasilan = float(input("Penghasilan orang tua per bulan (Rp): "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat IPK.")
        continue

    if penghasilan <= 3000000:
        print("Hasil seleksi: Beasiswa penuh")
        kuota_penuh += 1
    elif penghasilan <= 5000000:
        print("Hasil seleksi: Beasiswa sebagian")
    else:
        print("Hasil seleksi: Tidak mendapatkan beasiswa")

    print(f"Jumlah penerima beasiswa penuh: {kuota_penuh}")

print("\n=== SELEKSI SELESAI ===")
print(f"Total penerima beasiswa penuh: {kuota_penuh}")
