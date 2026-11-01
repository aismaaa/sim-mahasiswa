# Nama : Aisma Haidy Putri Berry Ani Nur Rizeki
# NPM: 20241320001


def proses_kalimat():
    print("=== Program Analisis Kalimat ===\n")
   
    kalimat = input("Masukkan sebuah kalimat: ")

    daftar_kata = kalimat.split()
    jumlah_kata = len(daftar_kata)

    jumlah_karakter = len(kalimat)

    if daftar_kata:
        kata_terpanjang = max(daftar_kata, key=len)
    else:
        kata_terpanjang = "Tidak ada kata"

    kalimat_title = kalimat.title()

    print("\n--- Hasil Analisis ---")
    print(f"Kalimat asli        : '{kalimat}'")
    print(f"(a) Jumlah kata     : {jumlah_kata}")
    print(f"(b) Jumlah karakter : {jumlah_karakter}")
    print(f"(c) Kata terpanjang : '{kata_terpanjang}'")
    print(f"(d) Title Case      : '{kalimat_title}'")

if __name__ == "__main__":
    proses_kalimat()