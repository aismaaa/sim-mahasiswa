# File: sistem_informasi/model/mahasiswa.py
# Berisi definisi struktur data Mahasiswa

def buat_mahasiswa(nim, nama, ipk):
    """Fungsi untuk membuat template dictionary mahasiswa."""
    return {
        "nim": nim,
        "nama": nama,
        "ipk": ipk,
        "status": "Aktif"
    }