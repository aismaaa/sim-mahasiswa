# Nama : Aisma Haidy Putri Berry Ani Nur Rizeki
# NPM: 20241320001


def analisis_nilai():
    print("=== Program Analisis Nilai Mahasiswa ===\n")
    
    input_nilai = input("Masukkan daftar nilai (pisahkan dengan koma, contoh: 85, 90, 78, 60): ")
    
    try:
        nilai_list = [float(x.strip()) for x in input_nilai.split(',')]
    except ValueError:
        print("Input tidak valid! Pastikan kamu hanya memasukkan angka dan koma.")
        return

    if not nilai_list:
        print("List nilai kosong!")
        return

    rata_rata = sum(nilai_list) / len(nilai_list)

    nilai_tertinggi = max(nilai_list)
    nilai_terendah = min(nilai_list)

    frekuensi = {} 
    
    for nilai in nilai_list:
        if nilai >= 85:
            kategori = 'A'
        elif nilai >= 70:
            kategori = 'B'
        elif nilai >= 55:
            kategori = 'C'
        elif nilai >= 40:
            kategori = 'D'
        else:
            kategori = 'E'

        if kategori in frekuensi:
            frekuensi[kategori] += 1
        else:
            frekuensi[kategori] = 1

    print("\n--- Hasil Analisis ---")
    print(f"Data nilai   : {nilai_list}")
    print(f"(a) Rata-rata      : {rata_rata:.2f}")
    print(f"(b) Nilai Tertinggi: {nilai_tertinggi}")
    print(f"(b) Nilai Terendah : {nilai_terendah}")
    
    print(f"(d) Frekuensi Kategori:")
    for kat in sorted(frekuensi.keys()):
        print(f"    - Kategori {kat}: {frekuensi[kat]} mahasiswa")

if __name__ == "__main__":
    analisis_nilai()