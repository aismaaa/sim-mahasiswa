# ringkasan_algoritma.py

# 1. Data Dummy Mahasiswa (Untuk hitung persentase Aktif vs Tidak Aktif)
daftar_mahasiswa = [
    {"nama": "Andi", "ipk": 3.5, "sks": 20},
    {"nama": "Budi", "ipk": 1.8, "sks": 15},
    {"nama": "Cici", "ipk": 3.9, "sks": 22},
    {"nama": "Dodi", "ipk": 1.2, "sks": 10},
]

aktif = 0
tidak_aktif = 0
for mhs in daftar_mahasiswa:
    if mhs["ipk"] >= 2.0 and mhs["sks"] >= 18:
        aktif += 1
    else:
        tidak_aktif += 1

total_mhs = len(daftar_mahasiswa)
persen_aktif = (aktif / total_mhs) * 100

# 2. Data Dummy Diskon (Untuk hitung rata-rata diskon)
daftar_diskon = [25, 20, 5, 10, 30] # dalam persen
rata_rata_diskon = sum(daftar_diskon) / len(daftar_diskon)

# 3. Data Dummy Stok (Untuk hitung persentase butuh restock)
daftar_stok = [45, 5, 0, 18, 12, 30]
butuh_restock = 0
for stok in daftar_stok:
    if stok <= 20: # Aman kalau > 20, selain itu butuh restock
        butuh_restock += 1

persen_restock = (butuh_restock / len(daftar_stok)) * 100

# Tampilkan Laporan Ringkasan
print("="*45)
print("RINGKASAN ALGORITMA SISTEM INFORMASI")
print("="*45)
print(f"1. Persentase Mahasiswa Aktif      : {persen_aktif:.1f}% ({aktif} dari {total_mhs})")
print(f"2. Persentase Mahasiswa Tidak Aktif: {100 - persen_aktif:.1f}% ({tidak_aktif} dari {total_mhs})")
print(f"3. Rata-rata Diskon Diberikan      : {rata_rata_diskon:.1f}%")
print(f"4. Persentase Item Butuh Restock   : {persen_restock:.1f}% ({butuh_restock} dari {len(daftar_stok)})")
print("="*45)