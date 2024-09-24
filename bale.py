# Kode ANSI untuk warna
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

#Pilihan mau menghitung apa
print (f"{GREEN}pilihlah salah satu dibawah ini!!{RESET}")
print (f"1. menghitung luas {BLUE}SEGI TIGA{RESET}")
print (f"2. menghitung luas {BLUE}SEGI PANJANG{RESET}")
print (f"3. menghitung luas volume {BLUE}BOLA{RESET}")
print (f"4. menghitung luas volume {BLUE}KUBUS{RESET}")
pilihan = input (f"masukkan pilihan {YELLOW}(1/2/3/4) :{RESET}")

# Fungsi untuk menghitung luas segitiga
if pilihan== "1" :
    #pilihan untuk mau menghitung segtiga apa
    print (f"{GREEN}pilihlah salah satu dibawah ini!!{RESET}")
    print (f"1. menghitung luas segitiga {BLUE}SAMA SISI{RESET}")
    print (f"2. menghitung luas segitiga {BLUE}SAMA KAKI{RESET}")
    print (f"3. menghitung luas segitiga {BLUE}SEMBARANG{RESET}")
    pilihan = input (f"{YELLOW}masukkan pilihan (1/2/3) :{RESET}")

    #fungsi menghitung segitiga sama sisi
    if pilihan== "1" :
        import math
        def hitung_luas_segitiga_sama_sisi(sisi):
            luas = (math.sqrt(3) / 4) * (sisi ** 2)
            return luas
        # Input panjang sisi segitiga
        sisi = float(input("Masukkan panjang sisi segitiga sama sisi: "))
        # Menghitung luas
        luas = hitung_luas_segitiga_sama_sisi(sisi)
        # Menampilkan hasil
        print(f"Luas segitiga sama sisi dengan sisi {sisi} adalah {BLUE}{luas:.2f}{RESET}")
        
    #Fungsi menghitung segitiga sama kaki
    elif pilihan== "2" :
        import math
        def hitung_luas_segitiga_sama_kaki(alas, sisi):
            # Menghitung tinggi segitiga menggunakan teorema Pythagoras
            tinggi = math.sqrt(sisi**2 - (alas/2)**2)
            # Menghitung luas segitiga
            luas = (alas * tinggi) / 2
            return luas
        # Input panjang alas dan sisi segitiga
        alas = float(input("Masukkan panjang alas segitiga sama kaki: "))
        sisi = float(input("Masukkan panjang sisi segitiga sama kaki: "))
        # Menghitung luas
        luas = hitung_luas_segitiga_sama_kaki(alas, sisi)
        # Menampilkan hasil
        print(f"Luas segitiga sama kaki dengan alas {alas} dan sisi {sisi} adalah {BLUE}{luas:.2f}{RESET}")

    # fungsi menghitung segitiga sembarang
    elif pilihan== "3" :
        import math
        def hitung_luas_segitiga_sembarang(a, b, c):
            # Menghitung setengah keliling (s)
            s = (a + b + c) / 2
            # Menghitung luas menggunakan rumus Heron
            luas = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return luas
        # Input panjang ketiga sisi segi tiga
        a = float(input("Masukkan panjang sisi a: "))
        b = float(input("Masukkan panjang sisi b: "))
        c = float(input("Masukkan panjang sisi c: "))
        # Menghitung luas
        luas = hitung_luas_segitiga_sembarang(a, b, c)
        # Menampilkan hasil
        print(f"Luas segitiga sembarang dengan sisi {a}, {b}, dan {c} adalah {BLUE}{luas:.2f}{RESET}")

    else :
        print (f"{RED}pilihan mu eyoy_ pyogyam agi ucaak <:{RESET}")


# Fungsi untuk menghitung luas persegi panjang
elif pilihan == "2" :
    def hitung_luas_persegi_panjang(panjang, lebar):
        luas = panjang * lebar
        return luas
    # Meminta input dari pengguna
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    # Menghitung luas persegi panjang
    luas = hitung_luas_persegi_panjang(panjang, lebar)
    # Menampilkan hasil
    print(f"Luas persegi panjang adalah: {BLUE}{luas}{RESET}")


# Fungsi untuk menghitung volume bola
elif pilihan == "3" :
    import math
    def hitung_volume_bola(jari_jari):
        volume = (4/3) * math.pi * (jari_jari ** 3)
        return volume
    # Meminta input dari pengguna
    jari_jari = float(input("Masukkan jari-jari bola: "))
    # Menghitung volume bola
    volume = hitung_volume_bola(jari_jari)
    # Menampilkan hasil
    print(f"Volume bola adalah: {BLUE}{volume}{RESET}")


# Fungsi untuk menghitung volume kubus
elif pilihan == "4" :
    def hitung_volume_kubus(sisi):
        volume = sisi ** 3
        return volume
    # Meminta input dari pengguna
    sisi = float(input("Masukkan panjang sisi kubus: "))
    # Menghitung volume kubus
    volume = hitung_volume_kubus(sisi)
    # Menampilkan hasil
    print(f"Volume kubus adalah:{BLUE} {volume} {RESET}")
else :
    print (F"{RED} pilihan mu eyoy_ pyogyam agi ucaak <:{RESET}")

    