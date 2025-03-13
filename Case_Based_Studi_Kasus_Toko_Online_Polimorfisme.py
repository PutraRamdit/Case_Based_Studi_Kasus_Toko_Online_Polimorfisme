class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    
    def tampilkanInfo(self):
        return f"Nama: {self.nama}, Harga: {self.harga}, Stok: {self.stok}"

class Buku(Produk):
    def __init__(self, nama, harga, stok, penulis, penerbit):
        super().__init__(nama, harga, stok)
        self.penulis = penulis
        self.penerbit = penerbit
    
    def tampilkanInfo(self):
        return f"[Buku] {super().tampilkanInfo()}, Penulis: {self.penulis}, Penerbit: {self.penerbit}"

class Elektronik(Produk):
    def __init__(self, nama, harga, stok, merek, garansi):
        super().__init__(nama, harga, stok)
        self.merek = merek
        self.garansi = garansi
    
    def tampilkanInfo(self):
        return f"[Elektronik] {super().tampilkanInfo()}, Merek: {self.merek}, Garansi: {self.garansi} tahun"

class Pakaian(Produk):
    def __init__(self, nama, harga, stok, ukuran, warna):
        super().__init__(nama, harga, stok)
        self.ukuran = ukuran
        self.warna = warna
    
    def tampilkanInfo(self):
        return f"[Pakaian] {super().tampilkanInfo()}, Ukuran: {self.ukuran}, Warna: {self.warna}"

class Inventaris:
    def __init__(self):
        self.daftar_produk = []
    
    def tambahProduk(self, produk):
        self.daftar_produk.append(produk)
        print(f"{produk.nama} telah ditambahkan ke inventaris.")
    
    def hapusProduk(self, nama):
        for produk in self.daftar_produk:
            if produk.nama == nama:
                self.daftar_produk.remove(produk)
                print(f"{nama} telah dihapus dari inventaris.")
                return
        print(f"Produk {nama} tidak ditemukan.")
    
    def cariProduk(self, nama):
        for produk in self.daftar_produk:
            if produk.nama == nama:
                print(produk.tampilkanInfo())
                return
        print(f"Produk {nama} tidak ditemukan.")
    
    def tampilkanSemuaProduk(self):
        if not self.daftar_produk:
            print("Inventaris kosong.")
        else:
            for produk in self.daftar_produk:
                print(produk.tampilkanInfo())

# Contoh penggunaan
inventaris = Inventaris()

buku1 = Buku("Python Programming", 150000, 10, "Guido van Rossum", "O'Reilly")
elektronik1 = Elektronik("Laptop Asus", 8000000, 5, "Asus", 2)
pakaian1 = Pakaian("Kaos Polo", 120000, 20, "L", "Biru")

inventaris.tambahProduk(buku1)
inventaris.tambahProduk(elektronik1)
inventaris.tambahProduk(pakaian1)

print("\nDaftar Produk di Inventaris:")
inventaris.tampilkanSemuaProduk()

print("\nMencari Produk 'Laptop Asus':")
inventaris.cariProduk("Laptop Asus")

print("\nMenghapus Produk 'Kaos Polo':")
inventaris.hapusProduk("Kaos Polo")

print("\nDaftar Produk Setelah Penghapusan:")
inventaris.tampilkanSemuaProduk()