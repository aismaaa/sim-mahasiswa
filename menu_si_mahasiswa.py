# menu_si_mahasiswa.py

def cek_status():
    print("\n--- Cek Status Mahasiswa ---")
    try:
        ipk = float(input("Masukkan IPK: "))
        sks = int(input("Masukkan SKS Tempuh: "))
        
        if ipk >= 2.0 and sks >= 18:
            status = "Aktif"
        elif 1.5 <= ipk < 2.0:
            status = "Peringatan"
        else:
            status = "Tidak Aktif"
            
        print(f"Status Mahasiswa: {status}")
    except ValueError:
        print("Error: Input harus berupa angka!")

def hitung_diskon():
    print("\n--- Hitung Diskon Biaya ---")
    try:
        spp = float(input("Masukkan Biaya SPP (Rp): "))
        anak_karyawan = input("Anak karyawan? (y/n): ").lower() == 'y'
        ipk = float(input("Masukkan IPK: "))
        tepat_waktu = input("Bayar tepat waktu? (y/n): ").lower() == 'y'
        
        # Hitung diskon utama
        if anak_karyawan:
            diskon = 25
        elif ipk >= 3.8:
            diskon = 20
        elif ipk >= 3.5:
            diskon = 15
        elif ipk >= 3.0:
            diskon = 10
        else:
            diskon = 0
            
        # Tambah diskon tepat waktu
        if tepat_waktu:
            diskon += 5
            
        bayar = spp - (spp * (diskon / 100))
        print(f"Diskon yang didapat: {diskon}%")
        print(f"Biaya yang harus dibayar: Rp {bayar:,.0f}")
    except ValueError:
        print("Error: Input harus berupa angka!")

def cek_stok():
    print("\n--- Cek Peringatan Stok ---")
    inventaris = [
        {"nama": "Buku Python", "stok": 45},
        {"nama": "Flashdisk", "stok": 5},
        {"nama": "Kabel USB", "stok": 0},
        {"nama": "Mouse", "stok": 18},
    ]
    
    for item in inventaris:
        if item["stok"] == 0:
            status = "HABIS"
        elif item["stok"] <= 10:
            status = "RENDAH"
        elif item["stok"] <= 20:
            status = "PERINGATAN"
        else:
            status = "AMAN"
        print(f"{item['nama']:<15} | Stok: {item['stok']:>3} | Status: {status}")

# Program Utama (Menu Loop)
while True:
    print("\n" + "="*40)
    print("MENU SISTEM INFORMASI MAHASISWA")
    print("="*40)
    print("1. Cek Status Mahasiswa")
    print("2. Hitung Diskon Biaya")
    print("3. Cek Peringatan Stok")
    print("0. Keluar")
    
    pilihan = input("\nPilih menu (0-3): ")
    
    if pilihan == "1":
        cek_status()
    elif pilihan == "2":
        hitung_diskon()
    elif pilihan == "3":
        cek_stok()
    elif pilihan == "0":
        print("Terima kasih, program selesai!")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")