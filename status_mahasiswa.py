# status_mahasiswa.py
print("=== Input Data 5 Mahasiswa ===")
data_mahasiswa = []

# 1. Input data menggunakan loop
for i in range(1, 6):
    print(f"\n--- Mahasiswa ke-{i} ---")
    nim = input("NIM: ")
    nama = input("Nama: ")
    ipk = float(input("IPK: "))
    sks = int(input("SKS Tempuh: "))
    
    # Simpan ke dalam list dictionary
    data_mahasiswa.append({
        "nim": nim, 
        "nama": nama, 
        "ipk": ipk, 
        "sks": sks
    })

# 2. Tampilkan Laporan Status
print("\n" + "="*60)
print("LAPORAN STATUS MAHASISWA")
print("="*60)
print(f"{'NIM':<10} {'Nama':<15} {'IPK':<5} {'SKS':<5} {'Status'}")
print("-"*60)

for mhs in data_mahasiswa:
    # Aturan Bisnis
    if mhs["ipk"] < 1.5:
        status = "Tidak Aktif"
    elif mhs["ipk"] < 2.0:
        status = "Peringatan"
    else: # IPK >= 2.0
        if mhs["sks"] >= 18:
            status = "Aktif"
        else:
            status = "Peringatan" # SKS kurang
            
    print(f"{mhs['nim']:<10} {mhs['nama']:<15} {mhs['ipk']:<5} {mhs['sks']:<5} {status}")