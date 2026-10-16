
data_mahasiswa = []
jumlah_kategori = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

for i in range(10):
    print(f"\nMahasiswa ke-{i + 1}")

    nama = input("Nama mahasiswa: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        kategori = "A"
    elif nilai_akhir >= 75:
        kategori = "B"
    elif nilai_akhir >= 65:
        kategori = "C"
    elif nilai_akhir >= 50:
        kategori = "D"
    else:
        kategori = "E"

    jumlah_kategori[kategori] += 1

    data_mahasiswa.append({
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": nilai_akhir,
        "kategori": kategori
    })

print("\n=== DAFTAR NILAI MAHASISWA ===")

for m in data_mahasiswa:
    print(f"\nNama        : {m['nama']}")
    print(f"Nilai tugas : {m['tugas']}")
    print(f"Nilai UTS   : {m['uts']}")
    print(f"Nilai UAS   : {m['uas']}")
    print(f"Nilai akhir : {m['akhir']:.2f}")
    print(f"Kategori    : {m['kategori']}")

nilai_tertinggi = max(data_mahasiswa, key=lambda m: m["akhir"])
nilai_terendah = min(data_mahasiswa, key=lambda m: m["akhir"])

rata_rata = sum(m["akhir"] for m in data_mahasiswa) / len(data_mahasiswa)

print("\n=== REKAPITULASI NILAI ===")

for kategori, jumlah in jumlah_kategori.items():
    print(f"Jumlah kategori {kategori}: {jumlah} mahasiswa")

print(f"\nNilai tertinggi: {nilai_tertinggi['akhir']:.2f}")
print(f"Nama mahasiswa : {nilai_tertinggi['nama']}")

print(f"\nNilai terendah : {nilai_terendah['akhir']:.2f}")
print(f"Nama mahasiswa : {nilai_terendah['nama']}")

print(f"\nRata-rata nilai akhir: {rata_rata:.2f}")
