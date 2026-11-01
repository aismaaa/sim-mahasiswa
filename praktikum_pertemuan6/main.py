# Nama: Aisma Haidy Putri Berry Ani Nur Rizeki
# NPM: 20241320001


from utilitas_akademik import konversi_nilai_huruf, hitung_ipk, generate_transkrip

def main():
    print("=== Program Sistem Informasi Mahasiswa ===\n")

    nama_mhs = "Aisma Haidy Putri Berry Ani Nur Rizeki"
    nim_mhs = "20241320001" 
    nilai_mhs = [88, 92, 75, 80, 95]

    print(f"Menguji konversi nilai 92: {konversi_nilai_huruf(92)}\n")

    hasil_transkrip = generate_transkrip(nama_mhs, nim_mhs, nilai_mhs)
    print(hasil_transkrip)

if __name__ == '__main__':
    main()