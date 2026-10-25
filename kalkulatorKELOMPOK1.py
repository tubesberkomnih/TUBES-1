# Kelompok 1 "Kalkulator Imut"
# Salwa Hatimah 19826206
# Rayyani Ummu Mutiah 19826218
# Ashimah Layla El Hanafiah 19826077
# Marsandra Yusra 19826050
# Muhammad Raihan 19826056

# KAMUS
# pi, angka, hasil, sudut, rad, sin_x, cos_x, suku, fak : float
# pilihan, i, k, n, nomor, aksi : int
# ulang : bool
# angka_list, riwayat : list

# ALGORITMA
pi = 3.141592653589793
suku_n = 10
batas_riwayat = 10
riwayat = []
ulang = True

# FUNGSI FAKTORIAL
def faktorial(n):
    fak = 1
    for i in range(1, n + 1):
        fak = fak * i
    return fak

# FUNGSI SINUS DENGAN DERET TAYLOR
def hitung_sinus(derajat):
    sudut = derajat % 360
    if sudut > 180:
        sudut = sudut - 360
    rad = sudut * (pi / 180.0)
    sin_x = 0.0
    for k in range(0, suku_n):
        suku = rad ** (2 * k + 1)
        fak = faktorial(2 * k + 1)
        if k % 2 == 0:
            sin_x = sin_x + suku / fak
        else:
            sin_x = sin_x - suku / fak
    if abs(sin_x) < 0.0000000001:
        sin_x = 0.0
    return sin_x

# FUNGSI KOSINUS DENGAN DERET TAYLOR
def hitung_kosinus(derajat):
    sudut = derajat % 360
    if sudut > 180:
        sudut = sudut - 360
    rad = sudut * (pi / 180.0)
    cos_x = 0.0
    for k in range(0, suku_n):
        suku = rad ** (2 * k)
        fak = faktorial(2 * k)
        if k % 2 == 0:
            cos_x = cos_x + suku / fak
        else:
            cos_x = cos_x - suku / fak
    if abs(cos_x) < 0.0000000001:
        cos_x = 0.0
    return cos_x

# FUNGSI AKAR KUADRAT 
def hitung_akar(angka):
    if angka < 0:
        return None
    if angka == 0:
        return 0.0
    tebakan = angka
    if angka < 1:
        tebakan = 1.0
    for i in range(100):
        tebakan_baru = (tebakan + angka / tebakan) / 2
        if abs(tebakan_baru - tebakan) < 0.0000000001:
            tebakan = tebakan_baru
            break
        tebakan = tebakan_baru
    return tebakan

# FUNGSI MENYIMPAN RIWAYAT
def simpan_riwayat(ekspresi, hasil):
    riwayat.append([ekspresi, hasil])
    if len(riwayat) > batas_riwayat:
        riwayat.pop(0)

# FUNGSI MENAMPILKAN RIWAYAT
def tampilkan_riwayat():
    if len(riwayat) == 0:
        print("Belum ada riwayat kalkulasi.")
    else:
        print("\nRIWAYAT KALKULASI")
        for i in range(len(riwayat)):
            print(str(i + 1) + ". " + riwayat[i][0]
                  + " = " + str(riwayat[i][1]))

# PROGRAM UTAMA
while ulang:
    print("KALKULATOR IMUT")
    print("1. Operasi Dasar")
    print("2. Sinus")
    print("3. Kosinus")
    print("4. Tangen")
    print("5. Akar Kuadrat")
    print("6. Riwayat Kalkulasi")
    print("7. Keluar")
    try:
        pilihan = int(input("Pilih menu (1-7): "))
    except ValueError:
        print("Masukkan pilihan berupa angka.")
        continue

    # OPERASI DASAR
    if pilihan == 1:
        teks = input(
            "Masukkan minimal 2 angka, pisahkan dengan spasi: "
        )
        try:
            angka_list = [float(x) for x in teks.split()]
        except ValueError:
            print("Input angka tidak valid.")
            continue
        if len(angka_list) < 2:
            print("Minimal harus memasukkan 2 angka.")
            continue
        operator = input("Pilih operator (+, -, *, /): ")
        if operator not in ["+", "-", "*", "/"]:
            print("Operator tidak valid.")
            continue
        hasil = angka_list[0]
        valid = True
        for i in range(1, len(angka_list)):
            angka = angka_list[i]
            if operator == "+":
                hasil = hasil + angka
            elif operator == "-":
                hasil = hasil - angka
            elif operator == "*":
                hasil = hasil * angka
            elif operator == "/":
                if angka == 0:
                    print("Error: tidak dapat membagi dengan nol.")
                    valid = False
                    break
                hasil = hasil / angka
        if valid:
            ekspresi = (" " + operator + " ").join(
                [str(x) for x in angka_list]
            )
            print("Hasil:", hasil)
            simpan_riwayat(ekspresi, hasil)

    # SINUS, KOSINUS, DAN TANGEN
    elif pilihan >= 2 and pilihan <= 4:
        try:
            sudut = float(input("Masukkan sudut dalam derajat: "))
        except ValueError:
            print("Sudut harus berupa angka.")
            continue
        sin_x = hitung_sinus(sudut)
        cos_x = hitung_kosinus(sudut)
        if pilihan == 2:
            hasil = sin_x
            ekspresi = "sin(" + str(sudut) + ")"
        elif pilihan == 3:
            hasil = cos_x
            ekspresi = "cos(" + str(sudut) + ")"
        else:
            if abs(cos_x) < 0.0000000001:
                print("Error: nilai tangen tidak terdefinisi.")
                continue
            hasil = sin_x / cos_x
            ekspresi = "tan(" + str(sudut) + ")"
        print("Hasil:", hasil)
        simpan_riwayat(ekspresi, hasil)

    # AKAR KUADRAT
    elif pilihan == 5:
        try:
            angka = float(input("Masukkan angka: "))
        except ValueError:
            print("Input harus berupa angka.")
            continue
        hasil = hitung_akar(angka)
        if hasil is None:
            print("Akar bilangan negatif tidak terdefinisi "
                  "dalam bilangan real.")
        else:
            print("Hasil:", hasil)
            simpan_riwayat("akar(" + str(angka) + ")", hasil)

    # PENGELOLAAN RIWAYAT
    elif pilihan == 6:
        tampilkan_riwayat()
        if len(riwayat) == 0:
            continue
        print("\n1. Gunakan hasil riwayat")
        print("2. Hapus satu riwayat")
        print("3. Hapus semua riwayat")
        print("4. Kembali")
        try:
            aksi = int(input("Pilih tindakan (1-4): "))
        except ValueError:
            print("Pilihan tidak valid.")
            continue

        # MENGGUNAKAN HASIL RIWAYAT
        if aksi == 1:
            try:
                nomor = int(input("Pilih nomor riwayat: "))
            except ValueError:
                print("Nomor harus berupa angka.")
                continue
            if nomor < 1 or nomor > len(riwayat):
                print("Nomor riwayat tidak tersedia.")
                continue
            hasil_lama = riwayat[nomor - 1][1]
            print("Hasil yang dipilih:", hasil_lama)
            operator = input("Pilih operator (+, -, *, /): ")
            if operator not in ["+", "-", "*", "/"]:
                print("Operator tidak valid.")
                continue
            try:
                angka_baru = float(input("Masukkan angka berikutnya: "))
            except ValueError:
                print("Input harus berupa angka.")
                continue
            if operator == "+":
                hasil_baru = hasil_lama + angka_baru
            elif operator == "-":
                hasil_baru = hasil_lama - angka_baru
            elif operator == "*":
                hasil_baru = hasil_lama * angka_baru
            else:
                if angka_baru == 0:
                    print("Error: tidak dapat membagi dengan nol.")
                    continue
                hasil_baru = hasil_lama / angka_baru
            ekspresi_baru = (
                "(" + riwayat[nomor - 1][0] + ") "
                + operator + " " + str(angka_baru)
            )
            print("Hasil:", hasil_baru)
            simpan_riwayat(ekspresi_baru, hasil_baru)

        # MENGHAPUS SATU RIWAYAT
        elif aksi == 2:
            try:
                nomor = int(input("Nomor riwayat yang dihapus: "))
            except ValueError:
                print("Nomor harus berupa angka.")
                continue
            if 1 <= nomor <= len(riwayat):
                riwayat.pop(nomor - 1)
                print("Riwayat berhasil dihapus.")
            else:
                print("Nomor riwayat tidak tersedia.")

        # MENGHAPUS SEMUA RIWAYAT
        elif aksi == 3:
            konfirmasi = input(
                "Yakin menghapus semua riwayat? (ya/tidak): "
            ).lower()
            if konfirmasi == "ya":
                riwayat.clear()
                print("Semua riwayat telah dihapus.")
            else:
                print("Penghapusan dibatalkan.")
        elif aksi == 4:
            continue
        else:
            print("Pilihan tindakan tidak valid.")

    # KELUAR
    elif pilihan == 7:
        print("Terima kasih telah menggunakan Kalkulator Imut!")
        ulang = False
    else:
        print("Pilihan menu tidak valid.")