class Produk:
    # Class attribute (atribut milik kelas)
    pajak_ppn = 0.11  # PPN 11%

    def __init__(self, kode, nama, harga, stok):
        # Atribut publik dan privat (Encapsulation)
        self.kode = kode
        self.nama = nama
        self.__harga = harga   # Private attribute
        self.__stok = stok     # Private attribute

    # Getter menggunakan @property untuk mengakses atribut privat
    @property
    def harga(self):
        return self.__harga

    # Setter untuk validasi perubahan harga
    @harga.setter
    def harga(self, nilai_baru):
        if nilai_baru >= 0:
            self.__harga = nilai_baru
        else:
            print("Error: Harga tidak boleh negatif!")

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, jumlah_baru):
        if jumlah_baru >= 0:
            self.__stok = jumlah_baru
        else:
            print("Error: Stok tidak boleh negatif!")

    # Instance method biasa
    def info_produk(self):
        return f"[{self.kode}] {self.nama} - Rp{self.__harga:,.0f} (Stok: {self.__stok})"

    # Class method untuk mengubah tarif pajak bagi seluruh produk
    @classmethod
    def ubah_pajak(cls, tarif_baru):
        cls.pajak_ppn = tarif_baru
        print(f"Tarif PPN berhasil diubah menjadi {tarif_baru * 100:.0f}%")

    # Static method sebagai fungsi bantuan format mata uang
    @staticmethod
    def format_rupiah(nominal):
        return f"Rp{nominal:,.0f}".replace(",", ".")


class TransaksiKasir:
    def __init__(self, nama_kasir):
        self.nama_kasir = nama_kasir
        self.__keranjang = []  # Private attribute menyimpan daftar belanja

    def tambah_barang(self, produk, jumlah):
        if produk.stok >= jumlah:
            produk.stok -= jumlah  # Menggunakan setter stok
            subtotal = produk.harga * jumlah
            self.__keranjang.append({
                "produk": produk,
                "jumlah": jumlah,
                "subtotal": subtotal
            })
            print(f"Berhasil menambahkan {jumlah}x {produk.nama} ke keranjang.")
        else:
            print(f"Maaf, stok {produk.nama} tidak mencukupi (tersisa {produk.stok}).")

    def cetak_struk(self):
        print("\n" + "=" * 40)
        print("           STRUK PEMBAYARAN")
        print(f"Kasir : {self.nama_kasir}")
        print("=" * 40)
        
        total_belanja = 0
        for item in self.__keranjang:
            prod = item["produk"]
            jml = item["jumlah"]
            sub = item["subtotal"]
            total_belanja += sub
            print(f"{prod.nama} ({jml}x) \t: {Produk.format_rupiah(sub)}")
            
        nilai_pajak = total_belanja * Produk.pajak_ppn
        total_akhir = total_belanja + nilai_pajak
        
        print("-" * 40)
        print(f"Subtotal \t\t: {Produk.format_rupiah(total_belanja)}")
        print(f"PPN ({Produk.pajak_ppn*100:.0f}%) \t\t: {Produk.format_rupiah(nilai_pajak)}")
        print(f"TOTAL BAYAR \t\t: {Produk.format_rupiah(total_akhir)}")
        print("=" * 40)


# ==========================================
# CONTOH PENGGUNAAN (PEMBUATAN OBJECT)
# ==========================================
if __name__ == "__main__":
    # 1. Membuat object dari class Produk
    p1 = Produk("BRG01", "Kopi Susu Gula Aren", 18000, 20)
    p2 = Produk("BRG02", "Roti Bakar Cokelat", 15000, 10)

    print("=== DAFTAR MENU ===")
    print(p1.info_produk())
    print(p2.info_produk())
    print()

    # 2. Menguji Setter (mengubah harga produk)
    p1.harga = 20000 

    # 3. Membuat object dari class TransaksiKasir
    kasir1 = TransaksiKasir("Andika")
    kasir1.tambah_barang(p1, 2)
    kasir1.tambah_barang(p2, 1)

    # 4. Mencetak struk transaksi
    kasir1.cetak_struk()