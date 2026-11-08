"""
KODE BERSIH: Hasil Refactoring dari kode_kotor.py
Mengikuti prinsip Clean Code dan PEP 8.
"""
from typing import Any, Dict, Optional

# 2. REPLACE MAGIC NUMBER: Mengganti angka ajaib dengan konstanta (UPPER_SNAKE_CASE)
HARGA_PER_SKS = 500000
DISKON_RATE = 0.1
ADMIN_FEE = 5000
TIPE_BEASISWA_PENUH = 1
TIPE_BEASISWA_SEBAGIAN = 2


# 3. EXTRACT METHOD: Memecah logika duplikat menjadi fungsi kecil
def _hitung_biaya_dengan_diskon(sks: int) -> float:
    """Menghitung total biaya dengan potongan diskon."""
    biaya_normal = sks * HARGA_PER_SKS
    diskon = biaya_normal * DISKON_RATE
    return biaya_normal - diskon + ADMIN_FEE


def _hitung_biaya_normal(sks: int) -> float:
    """Menghitung total biaya tanpa diskon."""
    return (sks * HARGA_PER_SKS) + ADMIN_FEE


def proses_diskon_mahasiswa(data_mhs: Optional[Dict[str, Any]], tipe_mhs: int) -> float:
    """
    Menghitung total biaya kuliah mahasiswa berdasarkan SKS dan tipe beasiswa.

    Args:
        data_mhs (dict): Data mahasiswa (harus berisi 'status' dan 'sks').
        tipe_mhs (int): Tipe mahasiswa (1=Beasiswa Penuh, 2=Sebagian, 0=Reguler).

    Returns:
        float: Total biaya yang harus dibayar.
    """
    # 5. REMOVE DEAD CODE: Variabel 'tanggal_hari_ini' dihapus.

    # 4. GUARD CLAUSE: Mengurangi deep nesting dengan return lebih awal
    if not data_mhs:
        return 0.0
    if data_mhs.get("status") != "aktif":
        return 0.0
    if data_mhs.get("sks", 0) <= 0:
        return 0.0

    sks = data_mhs["sks"]

    # Logika diskon yang sudah tidak duplikat
    if tipe_mhs in (TIPE_BEASISWA_PENUH, TIPE_BEASISWA_SEBAGIAN):
        return _hitung_biaya_dengan_diskon(sks)

    return _hitung_biaya_normal(sks)


# Tes Kode Bersih
if __name__ == "__main__":
    data_andi = {"status": "aktif", "sks": 20}
    print("Kode Bersih - Andi (Tipe 1):", proses_diskon_mahasiswa(data_andi, 1))
