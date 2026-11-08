"""
Program utama Sistem Informasi Perpustakaan.
Mendemonstrasikan penggunaan dan penanganan custom exception.
"""

# Import custom exception yang sudah kita buat
from perpustakaan_exception import (
    AnggotaNotFoundError,
    BukuNotFoundError,
    BukuTidakTersediaError,
    PerpustakaanError,
)

# --- DATABASE SIMULASI ---
KATALOG_BUKU = {
    "978-013-468599-1": {"judul": "Clean Code", "stok": 2},
    "978-020-163361-0": {"judul": "Design Patterns", "stok": 0},  # Stok habis
}

DAFTAR_ANGGOTA = ["A001", "A002", "A003"]


# --- FUNGSI LOGIKA BISNIS ---
def pinjam_buku(id_anggota: str, isbn: str) -> str:
    """
    Fungsi untuk memproses peminjaman buku.
    Akan melempar (raise) custom exception jika ada kondisi yang tidak valid.
    """
    # 1. Cek apakah anggota terdaftar
    if id_anggota not in DAFTAR_ANGGOTA:
        raise AnggotaNotFoundError(f"Anggota dengan ID '{id_anggota}' tidak terdaftar.")

    # 2. Cek apakah buku ada di katalog
    if isbn not in KATALOG_BUKU:
        raise BukuNotFoundError(
            f"Buku dengan ISBN '{isbn}' tidak ditemukan di katalog."
        )

    buku = KATALOG_BUKU[isbn]

    # 3. Cek apakah stok buku tersedia
    if buku["stok"] <= 0:
        raise BukuTidakTersediaError(
            f"Buku '{buku['judul']}' sedang tidak tersedia (stok habis)."
        )

    # 4. Jika semua aman, kurangi stok
    buku["stok"] -= 1
    return f"Peminjaman berhasil! Anggota {id_anggota} meminjam '{buku['judul']}'."


# --- PROGRAM UTAMA (DEMO) ---
def demo_peminjaman(id_anggota, isbn):
    print(f"\n--- Mencoba Peminjaman: Anggota {id_anggota}, ISBN {isbn} ---")
    try:
        pesan = pinjam_buku(id_anggota, isbn)
        print(f"[SUKSES] {pesan}")

    except AnggotaNotFoundError as e:
        print(f"[GAGAL - Anggota] {e}")
    except BukuNotFoundError as e:
        print(f"[GAGAL - Buku] {e}")
    except BukuTidakTersediaError as e:
        print(f"[GAGAL - Stok] {e}")
    except PerpustakaanError as e:
        # Ini akan menangkap semua error PerpustakaanError lainnya jika ada
        print(f"[GAGAL - Umum] Terjadi error perpustakaan: {e}")


if __name__ == "__main__":
    print("=== DEMO SISTEM INFORMASI PERPUSTAKAAN ===")

    # Skenario 1: Sukses
    demo_peminjaman("A001", "978-013-468599-1")

    # Skenario 2: Anggota tidak terdaftar
    demo_peminjaman("A999", "978-013-468599-1")

    # Skenario 3: Buku tidak ditemukan
    demo_peminjaman("A002", "978-000-000-000-0")

    # Skenario 4: Stok buku habis
    demo_peminjaman("A003", "978-020-163361-0")
