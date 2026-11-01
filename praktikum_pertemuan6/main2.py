# File: main.py
# Program utama untuk menguji package sistem_informasi

# Import fungsi dari dalam package menggunakan notasi titik (dot notation)
from sistem_informasi.service.crud import create, read, read_all, update, delete
from sistem_informasi.utils.helpers import cetak_garis, format_output

def main():
    print("=== TESTING PACKAGE SISTEM INFORMASI ===\n")

    # 1. CREATE
    print("1. Menambah Data (Create):")
    create("2021001", "Aisma", 3.90)
    create("2021002", "Budi", 3.50)
    create("2021003", "Cici", 3.75)
    cetak_garis()

    # 2. READ ALL
    print("2. Menampilkan Semua Data (Read All):")
    semua_data = read_all()
    for nim, data in semua_data.items():
        print(f"[{nim}]:")
        format_output(data)
    cetak_garis()

    # 3. UPDATE
    print("3. Update Data Budi (Update):")
    status, pesan = update("2021002", ipk_baru=3.80)
    print(f"Status: {status}, Pesan: {pesan}")
    print(f"Data Budi sekarang: {read('2021002')}")
    cetak_garis()

    # 4. DELETE
    print("4. Hapus Data Cici (Delete):")
    status, pesan = delete("2021003")
    print(f"Status: {status}, Pesan: {pesan}")
    
    print("\nData Akhir:")
    format_output(read_all())

if __name__ == "__main__":
    main()