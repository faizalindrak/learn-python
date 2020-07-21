#program hitung lembur harian in progress
gaji = input("Masukkan gaji : ")
hariKerja = input("Masukkan total hari kerja dalam satu minggu :")
jamLembur = input("Masukkan total jam lembur hari ini :")
try:
    gaji = float(gaji)
    hariKerja = float(hariKerja)
    jamLembur = float(jamLembur)
except:
    print("tolong masukkan angka")

rate = gaji/173

if int(hariKerja) == int(6):
    if int(jamLembur) <= 7:
        basicPay = jamLembur*rate*2
        outputPay = basicPay
    elif int(jamLembur) == 8:
        basicPay = jamLembur*rate*2
        addPay = (jamLembur-7)*(rate*1)
        outputPay = basicPay + addPay
    elif int(jamLembur) >= 9:
        basicPay = jamLembur*rate*2
        addPay = (jamLembur-7)*(rate*1)
        morePay = (jamLembur-8)*(rate*1)
        outputPay = basicPay+addPay+morePay
else:
    outputPay = "error"
print (int(outputPay))
