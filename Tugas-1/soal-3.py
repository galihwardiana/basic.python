#pendefinisian variabel
nilaiTeori = float(input("Masukkan nilai teori "))
nilaiPraktek = float(input("Masukkan nilai praktek"))

#booleans
if nilaiTeori and nilaiPraktek > 70:
    print("Selamat, Anda Lulus!")
elif nilaiTeori > 70 and nilaiPraktek < 70:
    print("Anda harus mengulang ujian praktek")
elif nilaiTeori < 70 and nilaiPraktek > 70:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")