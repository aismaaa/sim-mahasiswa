# Nama : Aisma Haidy Putri Berry Ani Nur Rizeki
# NPM: 20241320001


def analisis_beasiswa():
    print("=== Program Analisis Penerima Beasiswa ===\n")

    input_A = input("Masukkan ID penerima Beasiswa A (pisahkan dengan koma): ")
    input_B = input("Masukkan ID penerima Beasiswa B (pisahkan dengan koma): ")

    set_A = set(x.strip() for x in input_A.split(','))
    set_B = set(x.strip() for x in input_B.split(','))

    kedua_beasiswa = set_A & set_B  

    hanya_A = set_A - set_B  

    hanya_B = set_B - set_A  

    semua_unik = set_A | set_B  


    print("\n--- Hasil Analisis ---")
    print(f"Data Beasiswa A: {set_A}")
    print(f"Data Beasiswa B: {set_B}")
    print(f"(a) Menerima kedua beasiswa (A ∩ B) : {kedua_beasiswa}")
    print(f"(b) Hanya menerima Beasiswa A (A - B): {hanya_A}")
    print(f"(c) Hanya menerima Beasiswa B (B - A): {hanya_B}")
    print(f"(d) Semua mahasiswa unik (A ∪ B)    : {semua_unik}")

if __name__ == "__main__":
    analisis_beasiswa()