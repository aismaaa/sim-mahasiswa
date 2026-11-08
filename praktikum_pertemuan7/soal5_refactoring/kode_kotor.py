"""
KODE KOTOR: Mengandung 5 Code Smell
"""


def proses_diskon_mahasiswa(data_mhs, tipe_mhs):
    # 1. DEAD CODE: Variabel ini tidak pernah digunakan
    tanggal_hari_ini = "2026-11-08"

    if data_mhs is not None:
        # 4. DEEP NESTING: If bersarang terlalu dalam (lebih dari 3 level)
        if data_mhs.get("status") == "aktif":
            if data_mhs.get("sks") > 0:
                # 2. MAGIC NUMBER: Angka 500000, 0.1, dan 5000 tanpa penjelasan
                if tipe_mhs == 1:
                    # 3. DUPLICATE CODE: Logika ini sama persis dengan tipe 2
                    diskon = data_mhs["sks"] * 500000 * 0.1
                    total = (data_mhs["sks"] * 500000) - diskon + 5000
                    return total

                elif tipe_mhs == 2:
                    # 3. DUPLICATE CODE
                    diskon = data_mhs["sks"] * 500000 * 0.1
                    total = (data_mhs["sks"] * 500000) - diskon + 5000
                    return total

                else:
                    total = (data_mhs["sks"] * 500000) + 5000
                    return total
    return 0


# Tes Kode Kotor
data_andi = {"status": "aktif", "sks": 20}
print("Kode Kotor - Andi (Tipe 1):", proses_diskon_mahasiswa(data_andi, 1))
