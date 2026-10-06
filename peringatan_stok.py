# peringatan_stok.py

# Data inventaris (8 item sesuai soal)
inventaris = [
    {"kode": "B001", "nama": "Buku Python", "stok": 45, "harga": 85000},
    {"kode": "B002", "nama": "Buku Database", "stok": 12, "harga": 95000},
    {"kode": "B003", "nama": "Flashdisk 16GB", "stok": 5, "harga": 50000},
    {"kode": "B004", "nama": "Kabel USB", "stok": 0, "harga": 25000},
    {"kode": "B005", "nama": "Mouse Wireless", "stok": 18, "harga": 120000},
    {"kode": "B006", "nama": "Keyboard", "stok": 25, "harga": 150000},
    {"kode": "B007", "nama": "Monitor 24 inch", "stok": 8, "harga": 1500000},
    {"kode": "B008", "nama": "Headset", "stok": 30, "harga": 300000},
]

total_nilai = 0
butuh_restock = 0

print("="*65)
print("LAPORAN STATUS INVENTARIS")
print("="*65)

for item in inventaris:
    stok = item["stok"]
    nilai = stok * item["harga"]
    total_nilai += nilai

    # Aturan Bisnis Stok
    if stok == 0:
        status = "HABIS"
        prioritas = "CRITICAL"
        butuh_restock += 1
    elif stok <= 10:
        status = "RENDAH"
        prioritas = "HIGH"
        butuh_restock += 1
    elif stok <= 20:
        status = "PERINGATAN"
        prioritas = "MEDIUM"
        butuh_restock += 1
    else:
        status = "AMAN"
        prioritas = "LOW"

    print(f"{item['kode']} | {item['nama']:<15} | Stok: {stok:>3} | Status: {status:<10} | [{prioritas}]")

print("="*65)
print(f"Total Nilai Inventaris : Rp {total_nilai:,}")
print(f"Item Butuh Restock     : {butuh_restock} dari {len(inventaris)} item")