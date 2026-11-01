import requests
import json

def main():
    print("=== Program Analisis Data dari REST API ===\n")

    url = "https://jsonplaceholder.typicode.com/posts"
    print(f"Sedang mengambil data dari {url} ...")
    
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json() 
        print(f"✅ Berhasil mengambil {len(posts)} data post!\n")

        post_user_1 = list(filter(lambda p: p['userId'] == 1, posts))
        print(f"🔍 Ditemukan {len(post_user_1)} post dari User ID 1.")

        judul_post = list(map(lambda p: p['title'], post_user_1))

        judul_sorted = sorted(judul_post, key=lambda x: len(x))
        
        print(f"📊 Judul terpendek: '{judul_sorted[0]}'")
        print(f"📊 Judul terpanjang: '{judul_sorted[-1]}'\n")

        nama_file = "hasil_analisis.json"
        print(f"💾 Menyimpan hasil ke file '{nama_file}' ...")

        with open(nama_file, "w", encoding="utf-8") as file:
            json.dump(judul_sorted, file, indent=4, ensure_ascii=False)
            
        print("✅ Data berhasil disimpan!")
        
    else:
        print(f"❌ Gagal mengambil data. Status code: {response.status_code}")

if __name__ == "__main__":
    main()