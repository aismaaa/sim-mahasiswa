# diskon_biaya.py
print("=== Kalkulator Diskon Biaya Kuliah ===")

# 1. Input Data
spp = float(input("Masukkan Biaya SPP (Rp): "))
anak_karyawan = input("Apakah anak karyawan? (y/n): ").lower() == 'y'
ipk = float(input("Masukkan IPK: "))
tepat_waktu = input("Apakah bayar tepat waktu? (y/n): ").lower() == 'y'

# 2. Hitung Diskon Utama (Hanya ambil yang terbesar)
if anak_karyawan:
    diskon_persen = 25
    kategori = "Anak Karyawan"
elif ipk >= 3.8:
    diskon_persen = 20
    kategori = "Prestasi IPK Tinggi"
elif ipk >= 3.5:
    diskon_persen = 15
    kategori = "Prestasi IPK Baik"
elif ipk >= 3.0:
    diskon_persen = 10
    kategori = "IPK Memuaskan"
else:
    diskon_persen = 0
    kategori = "Tidak ada diskon"

# 3. Tambah Diskon Tepat Waktu (Kumulatif)
if tepat_waktu:
    diskon_persen += 5

# 4. Hitung Nominal
potongan = spp * (diskon_persen / 100)
bayar = spp - potongan

# 5. Tampilkan Hasil
print("\n--- Rincian Pembayaran ---")
print(f"Kategori Diskon   : {kategori}")
print(f"Total Persentase  : {diskon_persen}%")
print(f"Potongan Biaya    : Rp {potongan:,.0f}")
print(f"Yang harus dibayar: Rp {bayar:,.0f}")