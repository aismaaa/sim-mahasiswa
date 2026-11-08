"""
Modul berisi fungsi-fungsi akademik yang akan diuji (Unit Tested).
"""


def hitung_ipk(nilai_list):
    """Menghitung IPK dari list dictionary nilai."""
    if not nilai_list:
        return 0.0

    total_bobot = sum(n["bobot"] * n["sks"] for n in nilai_list)
    total_sks = sum(n["sks"] for n in nilai_list)

    if total_sks == 0:
        return 0.0

    return total_bobot / total_sks


def validasi_nim(nim):
    """Validasi format NIM: harus string dan terdiri dari 10 digit angka."""
    if not isinstance(nim, str):
        return False
    return len(nim) == 10 and nim.isdigit()


def konversi_nilai_huruf(nilai_angka):
    """Mengkonversi nilai angka (0-100) ke huruf (A, B+, B, dst)."""
    if not (0 <= nilai_angka <= 100):
        raise ValueError("Nilai harus berada di antara 0 dan 100.")

    if nilai_angka >= 85:
        return "A"
    elif nilai_angka >= 80:
        return "A-"
    elif nilai_angka >= 75:
        return "B+"
    elif nilai_angka >= 70:
        return "B"
    elif nilai_angka >= 65:
        return "B-"
    elif nilai_angka >= 60:
        return "C+"
    elif nilai_angka >= 55:
        return "C"
    elif nilai_angka >= 40:
        return "D"
    else:
        return "E"
