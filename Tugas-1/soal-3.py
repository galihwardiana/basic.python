#pendefinisian variabel
nilaiTeori = float(input("Masukkan nilai teori "))
nilaiPraktek = float(input("Masukkan nilai praktek "))

#booleans
if nilaiTeori >= 70 and nilaiPraktek >= 70:
    print("Selamat, Anda Lulus!")
elif nilaiPraktek >= 70 and nilaiTeori < 70:
    print("Anda harus mengulang ujian teori")
elif nilaiTeori >= 70 and nilaiPraktek < 70:
    print("Anda harus mengulang ujian praktek")
else:
    print("Anda harus mengulang ujian teori dan praktek")