import os
import sys
from typing import List


def sapa(nama: str) -> str:
    """Memberikan sapaan."""
    return f"Halo, {nama}!"


def jumlahkan(angka: List[int]) -> int:
    """Menjumlahkan list angka."""
    return sum(angka)


if __name__ == "__main__":
    print(sapa("Aisma"))
    print(jumlahkan([1, 2, 3, 4, 5]))
