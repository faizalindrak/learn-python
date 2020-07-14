#Assignment of COURSERA Python Chapter 3
jam = input("Masukkan jam kerja : ")
tingkat = input("Masukkan rate gaji perjam : ")
jam = float(jam)
tingkat = float(tingkat)
if jam > 10:
    regBayar = jam * tingkat
    addBayar = (jam - 40) * (tingkat*0.5)
    outputBayar = regBayar + addBayar
else:
    outputBayar = jam * tingkat
print(outputBayar)