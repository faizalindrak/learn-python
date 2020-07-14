#Conditional Steps

aStr = "Halo Dunia"
try:
    outputStr = int(aStr) #jika kode ini gagal maka program akan tetap jalan
except:
    outputStr = 0

print("Pertama", outputStr)

bStr = "1001"
try:
    outputStr = int(bStr)
except:
    outputStr = 0
print("Kedua ",outputStr)

print("program selesai")