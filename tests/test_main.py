import pytest
from src.models import Mahasiswa, DaftarMahasiswa


class TestMahasiswa:
    """Test untuk class Mahasiswa."""
    
    def test_buat_mahasiswa_valid(self):
        """Test buat mahasiswa dengan data valid."""
        mhs = Mahasiswa("2024SI001", "Andi Pratama", "Sistem Informasi", 2024, 3.50)
        assert mhs.nim == "2024SI001"
        assert mhs.nama == "Andi Pratama"
        assert mhs.program_studi == "Sistem Informasi"
        assert mhs.angkatan == 2024
        assert mhs.ipk == 3.50
    
    def test_nim_tidak_valid(self):
        """Test NIM kurang dari 6 karakter harus error."""
        with pytest.raises(ValueError):
            Mahasiswa("abc", "Test", "SI", 2024, 3.0)
    
    def test_ipk_diluar_range(self):
        """Test IPK di luar 0.0-4.0 harus error."""
        with pytest.raises(ValueError):
            Mahasiswa("2024SI002", "Test", "SI", 2024, 5.0)
    
    def test_ipk_diluar_range_negatif(self):
        """Test IPK negatif harus error."""
        with pytest.raises(ValueError):
            Mahasiswa("2024SI003", "Test", "SI", 2024, -1.0)
    
    def test_nama_kosong(self):
        """Test nama kosong harus error."""
        with pytest.raises(ValueError):
            Mahasiswa("2024SI004", "", "SI", 2024, 3.0)


class TestDaftarMahasiswa:
    """Test untuk class DaftarMahasiswa."""
    
    def test_tambah_dan_cari(self):
        """Test tambah mahasiswa lalu cari."""
        db = DaftarMahasiswa()
        mhs = Mahasiswa("2024SI001", "Andi", "SI", 2024)
        db.tambah(mhs)
        assert db.cari("2024SI001") == mhs
        assert db.jumlah == 1
    
    def test_nim_duplikat(self):
        """Test tambah NIM duplikat harus error."""
        db = DaftarMahasiswa()
        m1 = Mahasiswa("2024SI001", "Andi", "SI", 2024)
        m2 = Mahasiswa("2024SI001", "Budi", "SI", 2024)
        db.tambah(m1)
        with pytest.raises(ValueError):
            db.tambah(m2)
    
    def test_hapus_mahasiswa(self):
        """Test hapus mahasiswa."""
        db = DaftarMahasiswa()
        mhs = Mahasiswa("2024SI001", "Andi", "SI", 2024)
        db.tambah(mhs)
        assert db.jumlah == 1
        result = db.hapus("2024SI001")
        assert result == True
        assert db.jumlah == 0
    
    def test_hapus_nim_tidak_ada(self):
        """Test hapus NIM yang tidak ada."""
        db = DaftarMahasiswa()
        result = db.hapus("9999SI999")
        assert result == False
    
    def test_cari_nim_tidak_ada(self):
        """Test cari NIM yang tidak ada."""
        db = DaftarMahasiswa()
        result = db.cari("9999SI999")
        assert result is None