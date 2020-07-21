#convert harga jual beli emas
hargaBeli = input("masukkan harga beli emas :")
hargaJual = input("masukkan harga jual emas ")
totalBeli = input("masukkan jumlah rupiah pembelian :")
try:
    hargaBeli = float(hargaBeli)
    hargaJual = float(hargaJual)
    totalBeli = float(totalBeli)
except:
    print("masukkan angka")
def hasil():
    proporsional = totalBeli/hargaBeli
    hasilRp = proporsional*hargaJual
    return hasilRp
print("Uang Penjualan yang akan anda dapatkan :", hasil())