# Nama : Aisma Haidy Putri Berry Ani Nur Rizeki
# NPM: 20241320001


import string

def analisis_teks():
    print("=== Program Analisis Teks dari File ===\n")
    
    nama_file = "sample_text.txt"
    
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            teks = file.read()
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan! Pastikan file sudah dibuat.")
        return

    teks = teks.lower()
    for tanda in string.punctuation:
        teks = teks.replace(tanda, "")

    daftar_kata = teks.split()
    
    if not daftar_kata:
        print("File kosong atau tidak ada kata yang valid.")
        return

    frekuensi = {}
    for kata in daftar_kata:
        if kata in frekuensi:
            frekuensi[kata] += 1
        else:
            frekuensi[kata] = 1
            
    sorted_frekuensi = sorted(frekuensi.items(), key=lambda item: item[1], reverse=True)
    top_10 = sorted_frekuensi[:10]

    hapax_legomena = [kata for kata, freq in frekuensi.items() if freq == 1]

    total_kata = len(daftar_kata)

    kata_unik = set(daftar_kata) 
    jumlah_kata_unik = len(kata_unik)
    
    ttr = jumlah_kata_unik / total_kata

    print(f"Total Kata (Tokens)   : {total_kata}")
    print(f"Total Kata Unik (Types): {jumlah_kata_unik}")
    
    print("\n(a) Frekuensi 10 Kata Teratas:")
    for kata, freq in top_10:
        print(f"    - '{kata}': {freq} kali")
        
    print(f"\n(b) 10 Kata Paling Sering Muncul:")
    print(f"    {[kata for kata, _ in top_10]}")
    
    print(f"\n(c) Kata yang hanya muncul sekali (Hapax Legomena):")
    print(f"    {hapax_legomena[:10]}{'...' if len(hapax_legomena) > 10 else ''}")
    print(f"    (Total ada {len(hapax_legomena)} kata unik)")
    
    print(f"\n(d) Type-Token Ratio (TTR): {ttr:.4f}")

if __name__ == "__main__":
    analisis_teks()