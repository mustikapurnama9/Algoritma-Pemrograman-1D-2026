total_belanja=int(input("total belanja:"))
diskon = 0
if total_belanja % 100000 == 0:
    total_harga=0
elif total_belanja % 50000 == 0:
    diskon=total_belanja * 50 // 100
    total_harga=total_belanja-diskon
elif total_belanja % 10000 == 0:
    diskon=total_belanja * 20 // 100
    total_harga=total_belanja-diskon
elif total_belanja >= 200000:
    diskon=total_belanja * 10 // 100
    total_harga=total_belanja-diskon
else:
    total_harga=total_belanja

point = "point bertambah" if total_belanja > 0 else "tidak ada point"

print("total awal belanja", total_belanja)
print("diskon", diskon)
print("total harga setelah diskon", total_harga)
print("status point", point)