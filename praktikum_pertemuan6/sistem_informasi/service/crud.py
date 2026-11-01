# File: sistem_informasi/service/crud.py
# Berisi logika CRUD (Create, Read, Update, Delete)

# Database in-memory (Dictionary)
database_mahasiswa = {}

def create(nim, nama, ipk):
    """Create: Menambah mahasiswa baru."""
    if nim in database_mahasiswa:
        return False, f"NIM {nim} sudah ada!"
    
    # Kita pakai fungsi dari modul model (bisa di-import jika mau, tapi kita buat dict langsung biar simpel)
    database_mahasiswa[nim] = {"nama": nama, "ipk": ipk, "status": "Aktif"}
    return True, f"Mahasiswa {nama} berhasil ditambahkan."

def read(nim):
    """Read: Mencari satu mahasiswa berdasarkan NIM."""
    return database_mahasiswa.get(nim, None)

def read_all():
    """Read: Menampilkan semua mahasiswa."""
    return database_mahasiswa

def update(nim, nama_baru=None, ipk_baru=None):
    """Update: Mengubah data mahasiswa."""
    if nim not in database_mahasiswa:
        return False, "NIM tidak ditemukan!"
        
    if nama_baru:
        database_mahasiswa[nim]["nama"] = nama_baru
    if ipk_baru:
        database_mahasiswa[nim]["ipk"] = ipk_baru
        
    return True, "Data berhasil diupdate."

def delete(nim):
    """Delete: Menghapus mahasiswa."""
    if nim not in database_mahasiswa:
        return False, "NIM tidak ditemukan!"
        
    del database_mahasiswa[nim]
    return True, "Data berhasil dihapus."