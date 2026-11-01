# Nama: Aisma Haidy Putri Berry Ani Nur Rizeki
# NPM: 20241320001



def konversi_nilai_huruf(nilai_angka):
    """Mengubah nilai angka (0-100) menjadi huruf (A-E)."""
    if nilai_angka >= 85:
        return 'A'
    elif nilai_angka >= 70:
        return 'B'
    elif nilai_angka >= 55:
        return 'C'
    elif nilai_angka >= 40:
        return 'D'
    else:
        return 'E'

def hitung_ipk(list_nilai):
    """Menghitung IPK sederhana (rata-rata nilai)."""
    if not list_nilai:
        return 0.0
    total = sum(list_nilai)
    ipk = total / len(list_nilai)
    return round(ipk, 2)

def generate_transkrip(nama, nim, list_nilai):
    """Membuat string transkrip nilai mahasiswa."""
    ipk = hitung_ipk(list_nilai)
    
    transkrip = f"=== TRANSKRIP NILAI ===\n"
    transkrip += f"Nama : {nama}\n"
    transkrip += f"NIM  : {nim}\n"
    transkrip += f"---------------------\n"
    
    for i, nilai in enumerate(list_nilai, 1):
        huruf = konversi_nilai_huruf(nilai)
        transkrip += f"Mata Kuliah {i}: {nilai} ({huruf})\n"
        
    transkrip += f"---------------------\n"
    transkrip += f"IPK Semester: {ipk}\n"
    
    return transkrip

if __name__ == '__main__':
    print("=== Testing Modul Utilitas Akademik ===")
    print("1. Test Konversi Nilai:")
    print(f"   90 -> {konversi_nilai_huruf(90)}")
    print(f"   75 -> {konversi_nilai_huruf(75)}")
    
    print("\n2. Test Hitung IPK:")
    print(f"   [85, 90, 78] -> {hitung_ipk([85, 90, 78])}")