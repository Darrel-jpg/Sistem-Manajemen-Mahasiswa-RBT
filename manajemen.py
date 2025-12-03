from rbt import RedBlackTree
import csv
import os
import time
from tabulate import tabulate

class ManajemenMahasiswa:
    def __init__(self):
        self.tree = RedBlackTree()
        self.csv_file = "data_mahasiswa.csv"
        self.load_from_csv()
    
    def load_from_csv(self):
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['NIM', 'Nama', 'Jurusan', 'IPK'])
            print(f"File {self.csv_file} dibuat.")
            return
        
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.tree.insert(
                        row['NIM'],
                        row['Nama'],
                        row['Jurusan'],
                        float(row['IPK'])
                    )
        except Exception as e:
            print(f"Error saat memuat data: {e}")
    
    def save_to_csv(self):
        try:
            students = self.tree.get_all_students()
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['NIM', 'Nama', 'Jurusan', 'IPK'])
                for student in students:
                    writer.writerow([student.nim, student.nama, student.jurusan, student.ipk])
            return True
        except Exception as e:
            print(f"Error saat menyimpan data: {e}")
            return False
    
    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def tambah_mahasiswa(self):
        self.clear()
        print("\n=== TAMBAH MAHASISWA ===")
        try:
            nim = input("NIM: ").strip()
            if not nim:
                print("NIM tidak boleh kosong!")
                return
            
            if self.tree.search(nim) != self.tree.NIL:
                print("NIM sudah terdaftar!")
                return
            
            nama = input("Nama: ").strip()
            jurusan = input("Jurusan: ").strip()
            ipk = float(input("IPK: "))
            
            if ipk < 0 or ipk > 4:
                print("IPK harus antara 0-4!")
                return
            
            self.tree.insert(nim, nama, jurusan, ipk)
            self.save_to_csv()
            print("Mahasiswa berhasil ditambahkan!")
        except ValueError:
            print("Input tidak valid!")
    
    def cari_mahasiswa(self):
        self.clear()
        print("\n=== CARI MAHASISWA ===")
        nim = input("Masukkan NIM: ").strip()
        node = self.tree.search(nim)
        
        if node == self.tree.NIL:
            print("Mahasiswa tidak ditemukan!")
        else:
            print("\nData Mahasiswa:")
            print(f"NIM     : {node.nim}")
            print(f"Nama    : {node.nama}")
            print(f"Jurusan : {node.jurusan}")
            print(f"IPK     : {node.ipk:.2f}")
    
    def hapus_mahasiswa(self):
        self.clear()
        print("\n=== HAPUS MAHASISWA ===")
        nim = input("Masukkan NIM: ").strip()
        
        if self.tree.delete_node(nim):
            self.save_to_csv()
            print("Mahasiswa berhasil dihapus!")
        else:
            print("Mahasiswa tidak ditemukan!")

    def tampilkan_semua(self):
        self.clear()
        print("\n=== DAFTAR MAHASISWA ===")
        students = self.tree.get_all_students()
        
        if not students:
            print("Belum ada data mahasiswa.")
            return
        
        headers = ["NIM", "Nama", "Jurusan", "IPK"]
        data_tabel = []
        
        for student in students:
            data_tabel.append([
                student.nim, 
                student.nama, 
                student.jurusan, 
                f"{student.ipk:.2f}"
            ])
        
        print(f"\nTotal: {len(students)} mahasiswa\n")
        print(tabulate(data_tabel, headers=headers, tablefmt="fancy_grid", numalign="decimal"))
    
    def update_mahasiswa(self):
        self.clear()
        print("\n=== UPDATE DATA MAHASISWA ===")
        nim = input("Masukkan NIM: ").strip()
        node = self.tree.search(nim)
        
        if node == self.tree.NIL:
            print("Mahasiswa tidak ditemukan!")
            return
        
        print("\nData Saat Ini:")
        print(f"NIM     : {node.nim}")
        print(f"Nama    : {node.nama}")
        print(f"Jurusan : {node.jurusan}")
        print(f"IPK     : {node.ipk:.2f}")
        print("\nTekan Enter untuk tidak mengubah")
        
        try:
            nama = input("Nama baru: ").strip()
            jurusan = input("Jurusan baru: ").strip()
            ipk_str = input("IPK baru: ").strip()
            
            if nama:
                node.nama = nama
            if jurusan:
                node.jurusan = jurusan
            if ipk_str:
                ipk = float(ipk_str)
                if ipk < 0 or ipk > 4:
                    print("IPK harus antara 0-4!")
                    return
                node.ipk = ipk
            
            self.save_to_csv()
            print("Data mahasiswa berhasil diupdate!")
        except ValueError:
            print("Input tidak valid!")
    
    def statistik(self):
        self.clear()
        print("\n=== STATISTIK MAHASISWA ===")
        students = self.tree.get_all_students()
        
        if not students:
            print("Belum ada data mahasiswa.")
            return
        
        total = len(students)
        total_ipk = sum(s.ipk for s in students)
        avg_ipk = total_ipk / total
        max_ipk = max(students, key=lambda s: s.ipk)
        min_ipk = min(students, key=lambda s: s.ipk)
        
        print(f"\nTotal Mahasiswa: {total}")
        print(f"Rata-rata IPK: {avg_ipk:.2f}")
        print(f"IPK Tertinggi: {max_ipk.ipk:.2f} ({max_ipk.nama})")
        print(f"IPK Terendah: {min_ipk.ipk:.2f} ({min_ipk.nama})")
        
        jurusan_dict = {}
        for s in students:
            if s.jurusan not in jurusan_dict:
                jurusan_dict[s.jurusan] = []
            jurusan_dict[s.jurusan].append(s)
        
        print("\nJumlah Mahasiswa per Jurusan:")
        for jurusan, mhs in jurusan_dict.items():
            avg_ipk_jurusan = sum(m.ipk for m in mhs) / len(mhs)
            print(f"  • {jurusan}: {len(mhs)} mahasiswa (Rata-rata IPK: {avg_ipk_jurusan:.2f})")
    
    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print("SISTEM MANAJEMEN MAHASISWA")
            print("=" * 50)
            print("1. Tambah Mahasiswa")
            print("2. Cari Mahasiswa")
            print("3. Update Mahasiswa")
            print("4. Hapus Mahasiswa")
            print("5. Tampilkan Semua Mahasiswa")
            print("6. Statistik")
            print("0. Keluar")
            print("=" * 50)
            
            pilihan = input("Pilih menu (0-6): ").strip()
            if pilihan == "1":
                self.tambah_mahasiswa()
            elif pilihan == "2":
                self.cari_mahasiswa()
            elif pilihan == "3":
                self.update_mahasiswa()
            elif pilihan == "4":
                self.hapus_mahasiswa()
            elif pilihan == "5":
                self.tampilkan_semua()
            elif pilihan == "6":
                self.statistik()
            elif pilihan == "0":
                print("\nTerima kasih telah menggunakan sistem ini", end='', flush=True)
                for i in range(3):
                    time.sleep(0.8)
                    print('!', end='', flush=True)
                self.clear()
                break
            else:
                print("Pilihan tidak valid!")
            
            input("\nTekan Enter untuk melanjutkan...")