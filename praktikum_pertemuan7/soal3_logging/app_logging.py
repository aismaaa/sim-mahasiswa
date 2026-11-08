"""
Program konfigurasi logging untuk aplikasi Sistem Informasi.
Menggunakan RotatingFileHandler dan StreamHandler dengan level berbeda.
"""
import logging
from logging.handlers import RotatingFileHandler

# 1. Inisialisasi Logger
logger = logging.getLogger("si_akademik")
# Set level logger ke DEBUG (level terendah) agar semua pesan bisa diproses
logger.setLevel(logging.DEBUG)

# 2. Buat Formatter (Format pesan log)
formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# 3. Buat File Handler (RotatingFileHandler) untuk log DEBUG ke atas
# maxBytes=1MB, backupCount=3 (akan otomatis buat file baru jika sudah 1MB)
file_handler = RotatingFileHandler(
    filename="si_app.log", maxBytes=1 * 1024 * 1024, backupCount=3, encoding="utf-8"
)
file_handler.setLevel(
    logging.DEBUG
)  # Tangkap semua dari DEBUG, INFO, WARNING, ERROR, CRITICAL
file_handler.setFormatter(formatter)

# 4. Buat Console Handler (StreamHandler) untuk log WARNING ke atas
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)  # Hanya tangkap WARNING, ERROR, CRITICAL
console_handler.setFormatter(formatter)

# 5. Tambahkan Handler ke Logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# 6. Tes Log pada berbagai level
if __name__ == "__main__":
    print("--- Memulai Aplikasi Sistem Informasi Akademik ---\n")

    # Level DEBUG & INFO (Hanya akan masuk ke FILE, tidak muncul di terminal)
    logger.debug("Query SQL: SELECT * FROM mahasiswa WHERE nim='2021001'")
    logger.info("User 'admin' berhasil login ke sistem.")

    # Level WARNING, ERROR, CRITICAL (Akan masuk ke FILE dan muncul di TERMINAL)
    logger.warning("Penggunaan memori server mencapai 85%.")
    logger.error("Gagal mengirim notifikasi email ke dosen@univ.ac.id")
    logger.critical("Koneksi database utama terputus!")

    print(
        "\n--- Selesai. Cek file 'si_app.log' di Explorer untuk melihat semua log. ---"
    )
