# Nama: Aisma Haidy Putri Berry Ani Nur Rizeki
# NPM: 20241320001


import statistics
import math

def hitung_statistik(data):
    """
    Fungsi untuk menghitung berbagai nilai statistik deskriptif.
    Mengembalikan hasil dalam bentuk Dictionary.
    """
    if not data:
        return {"error": "Data tidak boleh kosong!"}

    mean_val = statistics.mean(data)

    median_val = statistics.median(data)

    try:
        modus_val = statistics.mode(data)
    except statistics.StatisticsError:
        modus_val = "Tidak ada modus tunggal"

    range_val = max(data) - min(data)

    if len(data) > 1:
        std_dev_val = statistics.stdev(data)
    else:
        std_dev_val = 0.0

    return {
        "mean": round(mean_val, 2),
        "median": median_val,
        "modus": modus_val,
        "range": range_val,
        "std_dev": round(std_dev_val, 2)
    }

if __name__ == "__main__":
    print("=== Program Analisis Statistik Sederhana ===\n")

    nilai_mahasiswa = [85, 90, 78, 92, 85, 88, 70, 85, 95]
    
    print(f"Data Nilai: {nilai_mahasiswa}\n")
    print("--- Hasil Perhitungan ---")

    hasil = hitung_statistik(nilai_mahasiswa)

    for kunci, nilai in hasil.items():
        print(f"- {kunci.upper()}: {nilai}")