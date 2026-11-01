# Nama: Aisma Haidy Putri Berry Ani Nur Rizeki
# NPM: 20241320001


def validasi_data(data, schema, *field_wajib, **opsi_tambahan):
    """
    Fungsi untuk memvalidasi dictionary berdasarkan schema.
    
    :param data: Dictionary data yang akan divalidasi.
    :param schema: Dictionary berisi aturan (tipe data, min, max).
    :param *field_wajib: Nama-nama field yang HARUS ada di data (Positional args).
    :param **opsi_tambahan: Opsi tambahan seperti 'pesan_awal' (Keyword args).
    :return: Tuple (is_valid: bool, errors: list)
    """
    errors = []
    is_valid = True

    for field in field_wajib:
        if field not in data:
            errors.append(f"Field '{field}' tidak ditemukan dalam data!")
            is_valid = False

    for field, aturan in schema.items():
        if field not in data:
            continue
            
        nilai = data[field]

        tipe_diharapkan = aturan.get("tipe")
        if tipe_diharapkan and not isinstance(nilai, tipe_diharapkan):
            errors.append(f"Field '{field}' harus bertipe {tipe_diharapkan.__name__}, tapi didapat {type(nilai).__name__}.")
            is_valid = False

        if "min" in aturan and nilai < aturan["min"]:
            errors.append(f"Field '{field}' nilai {nilai} terlalu kecil (min: {aturan['min']}).")
            is_valid = False
            
        if "max" in aturan and nilai > aturan["max"]:
            errors.append(f"Field '{field}' nilai {nilai} terlalu besar (max: {aturan['max']}).")
            is_valid = False

    pesan_awal = opsi_tambahan.get("pesan_awal", "Ditemukan kesalahan:")
    
    if not is_valid:
        print(f"\n--- {pesan_awal} ---")
        for err in errors:
            print(f"❌ {err}")
    else:
        print(f"\n✅ {pesan_awal} Data valid dan sesuai schema!")

    return is_valid, errors


if __name__ == "__main__":
    print("=== Program Validasi Data Mahasiswa ===\n")

    schema_nilai = {
        "umur": {"tipe": int, "min": 17, "max": 30},
        "ipk": {"tipe": float, "min": 0.0, "max": 4.0},
        "nama": {"tipe": str}
    }

    print("1. Menguji Data Valid:")
    data_valid = {"nama": "Aisma", "umur": 20, "ipk": 3.85}
    status1, error1 = validasi_data(data_valid, schema_nilai, "nama", "umur", pesan_awal="Hasil Validasi 1:")

    print("\n2. Menguji Data Tidak Valid:")
    data_invalid = {"nama": 123, "umur": 15, "ipk": 5.0} 
    status2, error2 = validasi_data(data_invalid, schema_nilai, "nama", "umur", "ipk", pesan_awal="Hasil Validasi 2:")

    print(f"\nStatus akhir data 1: {status1}")
    print(f"Status akhir data 2: {status2}")