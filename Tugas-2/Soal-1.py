#list Kontak
listNama = []
listNomor = []

#fungsi program
def fungsiProgram():
    print("\nSelamat Datang!")
    print('''
    --- Menu ---
    1. Daftar Kontak
    2. Tambah Kontak
    3. Keluar''')
    menu = int(input("\nPilih menu: "))
    while menu != 3:
        while menu == 2:
            menuDua()
        while menu == 1:
            menuSatu()
        while menu != 1 or menu != 2 or menu != 3 :
            print("\nMenu tidak tersedia")
            fungsiProgram()
    print("\nProgram Selesai!\n")
    exit()


#fungsi menu satu
def menuSatu() :
    print("\nDaftar Kontak")
    for x in range(0, len(listNama)):
        print(x+1,". Nama: " ,listNama[x] )
        print("    Nomor Telepon: ",listNomor[x])
    fungsiProgram()


#fungsi menu dua
def menuDua() :
    listNama.append(str(input("\nNama: ")))
    listNomor.append(input("Nomor Telepon: "))
    print("\nKontak berhasil ditambahkan\n")
    fungsiProgram()

fungsiProgram()