"""
Unit test untuk modul akademik menggunakan framework unittest.
"""
import unittest

from akademik import hitung_ipk, konversi_nilai_huruf, validasi_nim


class TestHitungIPK(unittest.TestCase):
    """Test untuk fungsi hitung_ipk."""

    def test_ipk_normal(self):
        """Happy path: perhitungan IPK normal."""
        nilai = [{"bobot": 4.0, "sks": 3}, {"bobot": 3.0, "sks": 2}]
        # (4*3 + 3*2) / (3+2) = 18 / 5 = 3.6
        self.assertAlmostEqual(hitung_ipk(nilai), 3.6)

    def test_ipk_list_kosong(self):
        """Edge case: list kosong harus return 0.0."""
        self.assertEqual(hitung_ipk([]), 0.0)


class TestValidasiNIM(unittest.TestCase):
    """Test untuk fungsi validasi_nim."""

    def test_nim_valid(self):
        """Happy path: NIM 10 digit angka."""
        self.assertTrue(validasi_nim("2021001234"))

    def test_nim_terlalu_pendek(self):
        """Edge case: NIM kurang dari 10 digit."""
        self.assertFalse(validasi_nim("202100123"))

    def test_nim_ada_huruf(self):
        """Input tidak valid: ada huruf."""
        self.assertFalse(validasi_nim("2021AB1234"))


class TestKonversiNilai(unittest.TestCase):
    """Test untuk fungsi konversi_nilai_huruf."""

    def test_nilai_A(self):
        self.assertEqual(konversi_nilai_huruf(90), "A")

    def test_nilai_E(self):
        self.assertEqual(konversi_nilai_huruf(30), "E")

    def test_nilai_batas_bawah(self):
        """Edge case: nilai 0 harus E."""
        self.assertEqual(konversi_nilai_huruf(0), "E")

    def test_nilai_batas_atas(self):
        """Edge case: nilai 100 harus A."""
        self.assertEqual(konversi_nilai_huruf(100), "A")

    def test_nilai_negatif_error(self):
        """Input tidak valid: nilai negatif harus raise ValueError."""
        with self.assertRaises(ValueError):
            konversi_nilai_huruf(-5)

    def test_nilai_lebih_100_error(self):
        """Input tidak valid: nilai > 100 harus raise ValueError."""
        with self.assertRaises(ValueError):
            konversi_nilai_huruf(105)


if __name__ == "__main__":
    # Menjalankan test dengan mode verbose (detail)
    unittest.main(verbosity=2)
