"""
Modul ini berisi definisi hierarki custom exception untuk Sistem Informasi Perpustakaan.
"""


# 1. Base Exception (Induk)
class PerpustakaanError(Exception):
    """Exception dasar untuk semua error di sistem perpustakaan."""

    pass


# 2. Child Exceptions (Anak)
class BukuNotFoundError(PerpustakaanError):
    """Exception ketika buku yang dicari tidak ada di katalog."""

    pass


class BukuTidakTersediaError(PerpustakaanError):
    """Exception ketika buku ada, tapi stoknya habis."""

    pass


class AnggotaNotFoundError(PerpustakaanError):
    """Exception ketika ID anggota tidak terdaftar di sistem."""

    pass
