#program hitung lembur harian
gaji = input("Masukkan gaji : ")
hariKerja = input("Masukkan total hari kerja dalam satu minggu :")
jamLembur = input("Masukkan total jam lembur hari ini :")
rate = gaji
salah = ""
salah2 = ""
salah3 = ""
try:
    int(rate)
except:
    salah = "anda tidak memasukkan angka"
try:
    int(hariKerja)
except:
    salah2 = "anda tidak memasukkan angka"
try:
    int(jamLembur)
except:
    salah3 = "anda tidak memasukkan angka"
print(salah,salah2,salah3)

if hariKerja == int(6):
    print("aaa")
    if jamLembur <= 7:
        basicPay = jamLembur*rate*2
        outputPay = basicPay
    elif jamLembur == 8:
        basicPay = jamLembur*rate*2
        addPay = (jamLembur-7)*(rate*1)
        outputPay = basicPay + addPay
    elif jamLembur >= 9:
        basicPay = jamLembur*rate*2
        addPay = (jamLembur-7)*(rate*1)
        morePay = (jamLembur-8)*(rate*1)
        outputPay = basicPay+addPay+morePay
else:
    outputPay = "error"
print (outputPay)
