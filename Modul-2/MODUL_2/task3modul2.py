suhu = int(input("masukkan suhu reaktor: "))
tekanan_gas = float(input("masukkan tekanan gas: "))

if suhu >1000 :
    if tekanan_gas > 50 :
        peringatan = "MELTDOWN! SEGERA EVAKUASI!"
    else :
        peringatan = "Bahaya suhu : segera turun kan daya!"
if 500 <suhu <= 1000 :
    if tekanan_gas > 30 :
        peringatan = "Tekanan tidak stabil!"
    else :
        peringatan = "Operasi reaktor normal!"
else :
    peringatan = "Reaktor belum cukup panas!"

print("suhu :", suhu)
print("tekanan Gas :", tekanan_gas)
print("peringatan reaktor :", peringatan)
print("cetak maksimal!") if suhu> 800 else print("pompa normal!")