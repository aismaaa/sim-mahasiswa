# validasi_data.py

def validasi_nim(nim):
    if len(nim) != 10 or not nim.isdigit():
        return "NIM harus 10 digit angka"
    tahun = int(nim[:4])
    if tahun < 2000 or tahun > 2037:
        return "Tahun masuk NIM tidak valid (2000-2037)"
    return None

def validasi_ipk(ipk):
    if ipk < 0.0 or ipk > 4.0:
        return "IPK harus antara 0.0 sampai 4.0"
    return None

def validasi_sks(sks):
    if sks < 0 or sks > 24:
        return "SKS harus antara 0 sampai 24"
    return None

def validasi_semester(semester):
    if semester < 1 or semester > 14:
        return "Semester harus antara 1 sampai 14"
    return None

# Program Utama
print("=== Program Validasi Data Mahasiswa ===")
nim = input("Masukkan NIM (10 digit): ")
ipk = float(input("Masukkan IPK: "))
sks = int(input("Masukkan SKS: "))
semester = int(input("Masukkan Semester: "))

# Cek semua validasi
error_list = []

err_nim = validasi_nim(nim)
if err_nim: error_list.append(err_nim)

err_ipk = validasi_ipk(ipk)
if err_ipk: error_list.append(err_ipk)

err_sks = validasi_sks(sks)
if err_sks: error_list.append(err_sks)

err_sem = validasi_semester(semester)
if err_sem: error_list.append(err_sem)

# Tampilkan Hasil
print("\n--- Hasil Validasi ---")
if len(error_list) == 0:
    print("✅ Semua data VALID!")
else:
    print("❌ Ditemukan Error:")
    for err in error_list:
        print(f"- {err}")