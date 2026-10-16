#memilih 3 jenis tiket
tipe_tiket = (input("reguler, VIP, VVIP :"))
#menentukan harganya tiket
harga_reguler  = 40000
VIP = 75000
VVIP = 100000

while True:

    if  reguler == tipe_tiket :
        print(harga_reguler)
    elif tipe_tiket == VIP:
        print(VIP)
    elif tipe_tiket == VVIP:
        print(VVIP)
else:
    print(input("masukkan tipe tiket"))
#untuk memilih membeli minuman karna dia membeli tiket reguler
if tipe_tiket == reguler :
#untuk memilih input ya atau tidak untuk membeli minuman
    membeli_minuman = (input('y','n'))
#menggunakan operator aritmetika + dan percabangan if
    if membeli_minuman == y:
        print("total harga", harga_reguler + 10.000)
    else:
        print(f"dianjurkan membeli minuman{membeli_minuman}")

 
        
        



 


