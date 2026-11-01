# Nama : Aisma Haidy Putri Berry Ani Nur Rizeki
# NPM: 20241320001


inventaris = {
    "Laptop": (15000000, 5),
    "Mouse": (150000, 20),
    "Keyboard": (300000, 15)
}

def tambah_barang(nama, harga, stok):
    if nama in inventaris:
        print(f"[Gagal] Barang '{nama}' sudah ada di inventaris!")
    else:
        inventaris[nama] = (harga, stok)
        print(f"[Sukses] Barang '{nama}' berhasil ditambahkan.")

def update_stok(nama, stok_baru):
    if nama in inventaris:
        harga_lama = inventaris[nama][0] 
        inventaris[nama] = (harga_lama, stok_baru)
        print(f"[Sukses] Stok '{nama}' berhasil diupdate menjadi {stok_baru}.")
    else:
        print(f"[Gagal] Barang '{nama}' tidak ditemukan!")

def cari_barang_rentang(min_harga, max_harga):
    print(f"\n--- Barang dengan harga Rp{min_harga:,} - Rp{max_harga:,} ---")
    ditemukan = False
    for nama, (harga, stok) in inventaris.items():
        if min_harga <= harga <= max_harga:
            print(f"- {nama}: Harga Rp{harga:,}, Stok {stok}")
            ditemukan = True
    if not ditemukan:
        print("Tidak ada barang yang ditemukan pada rentang harga tersebut.")

def hitung_total_nilai():
    total = 0
    for harga, stok in inventaris.values():
        total += (harga * stok)
    return total

def main():
    print("=== Program Inventaris Toko ===\n")
    print("Data Awal Inventaris:")
    for nama, (harga, stok) in inventaris.items():
        print(f"- {nama}: Harga Rp{harga:,}, Stok {stok}")

    print("\n1. Menambah barang baru...")
    tambah_barang("Monitor", 2500000, 10)
    tambah_barang("Mouse", 100000, 5) 

    print("\n2. Mengupdate stok...")
    update_stok("Laptop", 3)
    update_stok("Headset", 10)

    print("\n3. Mencari barang...")
    cari_barang_rentang(100000, 1000000)

    print("\n4. Menghitung total nilai inventaris...")
    total_nilai = hitung_total_nilai()
    print(f"Total Nilai Keseluruhan Inventaris: Rp{total_nilai:,}")

if __name__ == "__main__":
    main()