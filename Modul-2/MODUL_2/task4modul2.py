pin = int(input("masukkan pin 3 digit: "))
jam_datang = float(input("jam kedatangan (0-23): "))

digit_1 = pin // 100
digit_2 = (pin //10) % 10
digit_3 = pin % 10

if pin % 5 == 0:
    if jam_datang < 12.00 :
        pesan = "garasi pagi terbuka"
    else:
        pesan = "garasi malam terbuka, lampu dinyalakan"
elif pin % 2 == 0:
    if (digit_1 + digit_3) == digit_2:
        pesan = "garasi VIP terbuka khusus bos"
    else:
        pesan = "kode genap ditolak, alarm berbunyi!"
else:
    pesan = "akses ditolak!"


print("pin : ", pin)
print("pesan akses pintu : ", pesan)
print("mode malam merekam") if jam_datang > 18 else print("mode siang standby")
