"""
Program membaca data mahasiswa dari CSV dengan penanganan exception lengkap.
"""
import csv


def baca_data_mahasiswa(nama_file):
    file_handle = None
    data_valid = []

    try:
        # Coba buka file (Bisa memicu FileNotFoundError)
        file_handle = open(nama_file, mode="r", encoding="utf-8")
        reader = csv.DictReader(file_handle)

        # Proses setiap baris
        for nomor_baris, baris in enumerate(reader, start=2):
            try:
                # Konversi IPK ke float (Bisa memicu ValueError jika 'abc')
                ipk = float(baris["ipk"])

                data_valid.append(
                    {
                        "nim": baris["nim"],
                        "nama": baris["nama"],
                        "ipk": ipk,
                        "semester": int(baris["semester"]),
                    }
                )
            except ValueError:
                print(
                    f"[WARNING] Data tidak valid di baris {nomor_baris} (IPK bukan angka). Dilewati."
                )

    except FileNotFoundError:
        print(f"[ERROR] File '{nama_file}' tidak ditemukan. Pastikan nama file benar.")
    except csv.Error as e:
        print(f"[ERROR] Format CSV rusak atau tidak valid: {e}")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan tidak terduga: {e}")

    else:
        # Blok ELSE: Hanya jalan jika TIDAK ADA exception di blok try utama
        print("\n" + "=" * 40)
        print("RINGKASAN DATA MAHASISWA")
        print("=" * 40)
        print(f"Total data valid yang terbaca: {len(data_valid)} mahasiswa")

        if data_valid:
            rata_ipk = sum(m["ipk"] for m in data_valid) / len(data_valid)
            print(f"Rata-rata IPK: {rata_ipk:.2f}")
        print("=" * 40)

    finally:
        # Blok FINALLY: SELALU jalan, untuk memastikan file ditutup (Resource Cleanup)
        if file_handle and not file_handle.closed:
            file_handle.close()
            print(f"\n[INFO] File '{nama_file}' berhasil ditutup dengan aman.")


# --- PROGRAM UTAMA ---
if __name__ == "__main__":
    print("--- Uji Coba 1: Membaca file yang ada ---")
    baca_data_mahasiswa("data_mahasiswa.csv")

    print("\n--- Uji Coba 2: Membaca file yang TIDAK ADA ---")
    baca_data_mahasiswa("file_hantu.csv")
