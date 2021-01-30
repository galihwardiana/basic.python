#list Kontak
listNama = []
listNomor = []

#fungsi program
def fungsiProgram():
    print('''
    --- Menu ---
    1. Daftar Kontak
    2. Tambah Kontak
    3. Keluar''')
    menu = (int(input("\nPilih menu: ")))
    while menu != 3:
        while menu == 2:
            menuDua()
        while menu == 1:
            menuSatu()
        else:
            print("\nMenu tidak tersedia")
            fungsiProgram()
    print("\nProgram Selesai!\n")
    exit()


#fungsi menu satu
def menuSatu() :
    print("\nDaftar Kontak\n")
    for x in range(0, len(listNama)):
        print(x+1,". Nama: " ,listNama[x] )
        print("    Nomor Telepon: ",listNomor[x])
    fungsiProgram()


#fungsi menu dua
def menuDua() :
    listNama.append(input("\nNama: "))
    listNomor.append(input("Nomor Telepon: "))
    print("\nKontak berhasil ditambahkan\n")
    fungsiProgram()

#jalankan program    
print("\nSelamat Datang!")
fungsiProgram()