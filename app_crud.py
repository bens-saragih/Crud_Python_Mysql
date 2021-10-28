import mysql.connector
from mysql.connector.errors import Error
from mysql.connector import errorcode
from prettytable import PrettyTable


class CRUD:
	def __init__(self):
		self.__localhost     = "localhost"
		self.__username      = "root"
		self.__password      = ""
		self.__nama_database = "Mahasiswa_DB" 
		self.__nama_table    = "Mahasiswa"
		self.buatKoneksi()


	def buatKoneksi(self):
		
		db = mysql.connector.connect(
		  host     = self.__localhost,
		  user     = self.__username,
		  passwd   = self.__password,
		  database = self.__nama_database
		)

		self.__db = db



	# Membuat method untuk create data Mahasiswa
	def create(self):

		# DEBUG 
		i = 1	# Inisialisasi nilai awal
		while i < 2 :  # Kondisi, jika i lebih kecil dari 2 maka kode akan di jalankan

			try: # Semua kode yang ada di dalam block try akan di cek, jika False akan dilempar ke except 
				nim = int(input("Masukan NIM: ")) # inputan dari user harus bertipe data integer

			except ValueError: # Jika inputan nim berisi tipe data kecuali integer maka akan di tangkap oleh eksepsi ValueError
				print("Masukan hanya Angka !!") # Disini kita membuat pesan errornya
				continue # akan terus mengulang ke atas jika eksepsi ValueError masi ada. 

			# Jika kode yang ada di dalam try benar maka, kode di bawah ini akan di jalankan
			nama = input("Masukan nama: ") # menerima inputan untuk Nama Mahasiswa
			fakultas = input("Masukan fakultas: ") # menerima inputan untuk Nama Fakultas
			prodi = input("Masukan prodi: ") # menerima inputan untuk Nama Prodi
			alamat = input("Masukan alamat: ") # menerima inputan untuk alamat Mahasiswa

			# Jika semua inputan telah berisi maka, kode di bawah ini akan di eksekusi 

			# membuat variabel bernama cursor.
			# self.__db.cursor artinya kita memanggil variabel self.__db yaitu variabel yang 
			# bertugas sebagai koneksi ke MYSQL atau Database kita.
			# Lalu kita memanggil salah satu method dari self.__db yaitu cursor()
			# cursor() bertugas untuk mengeksekusi perintah SQL nantinya.
			cursor = self.__db.cursor()  

			# membuat variabel bernama nilai, yang berisi semua data dari inputan di atas
			nilai = (nim,nama,fakultas,prodi,alamat)

			# membuat variabel query, disini kita akan memasukan query atau perintah untuk membuat/create data Mahasiswa
			query = "INSERT INTO "+self.__nama_table+" (nim,nama,fakultas,prodi,alamat) VALUES(%s, %s, %s, %s, %s)"
			
			try:
				cursor.execute(query,nilai)
				self.__db.commit()
			except mysql.connector.Error as err:
				if err.errno == 1062:
					print("NIM Sudah digunakan,masukan NIM yang lain")
					continue
			if cursor.rowcount == 1:
				print("\n")
				print("Berhasil menambahkan",nama)
				i+=1
				
			 # Increment, nilai variabel i akan di tambah 1 
	def read(self):
		cursor = self.__db.cursor()
		cursor.execute("SELECT * FROM "+self.__nama_table+"")
		hasil = cursor.fetchall()
		print("\n")
		print(" DAFTAR DATA MAHASISWA ".center(70,"="))
		print("\n")
		#print("NIM 		Nama 			  Fakultas 		  Prodi 			Alamat")
		tabel = PrettyTable(["Nim", "Nama", "Fakultas", "Prodi", "Alamat"])
		data = []
		print("\n")

		for i in hasil:

			a = i[0]
			b = i[1]
			c = i[2]
			d = i[3]
			e = i[4]


			tabel.add_row([a,b,c,d,e])
			
		print(tabel)
		print("\n")
		print("="*70)

	def update(self):
		i = 1
		while i < 2:
			try:
				nim = int(input("Masukan dan update berdasarkan NIM: "))
				cursor = self.__db.cursor()
				cursor.execute("SELECT * FROM "+self.__nama_table+" WHERE nim =%s ", (nim,))
				hasil = cursor.fetchone()
			except ValueError:
				print("Masukan hanya angka !!")
				continue
			if cursor.rowcount < 0:# jika data satu akan lebih kecil dari 0 karena
				print("Tidak ada data yang cocok")

			else:

			
				print("\n")
				print("="*25," DATA MAHASISWA ",hasil[1],"="*25)
				tabel = PrettyTable(["Nim", "Nama", "Fakultas", "Prodi", "Alamat"])
				print("\n")
				a = hasil[0]
				b = hasil[1]
				c = hasil[2]
				d = hasil[3]
				e = hasil[4]
				tabel.add_row([a,b,c,d,e])
				print(tabel)
				print("\n")
				print("="*70)

				nama = input("Masukan nama baru: ")
				fakultas = input("Masukan fakultas baru: ")
				prodi = input("Masukan prodi baru: ")
				alamat = input("Masukan alamat baru: ")

				cursor = self.__db.cursor()
				cursor.execute("UPDATE "+self.__nama_table+" SET nama=%s, fakultas=%s, prodi=%s, alamat=%s WHERE nim=%s ", (nama, fakultas, prodi, alamat, nim))
				self.__db.commit()

				if cursor.rowcount == 1:
					print("\n")
					print("Data yang bernama "+nama+" berhasil di update")
					i+=1


	def delete(self):
		i = 1
		while i < 2:
			try:
				nim = int(input("Hapus menggunakan NIM: "))
				cursor =  self.__db.cursor()

				cursor.execute("DELETE FROM "+self.__nama_table+" WHERE nim =%s ", (nim,))
				self.__db.commit()
			except ValueError:
				print("Masukan hanya angka !!")
				continue
			if cursor.rowcount == 0:
				print("Nim tidak ditemukan")
			else:
				print("\n")
				print("Data dari NIM ",nim," berhasil di hapus")
				i+=1

	def cari_data(self):
		i = 1
		while i < 2:
			cursor = self.__db.cursor()
			key = input("Masukan NIM atau Nama Mahasiswa: ")
			#query = "SELECT * FROM "+self.__nama_table+" WHERE nim LIKE %s OR nama LIKE %s"
			#nilai = ("%{}%".format(key), "%{}%".format(key))
			#cursor.execute(query,nilai)
			cursor.execute("SELECT * FROM "+self.__nama_table+" WHERE nim=%s OR nama=%s",(key, key))
			hasil = cursor.fetchone()

			if cursor.rowcount < 0:# jika data satu akan lebih kecil dari 0 karena
				print("Tidak ada data yang cocok")
			else:
				print("\n")
				print("="*25," DATA MAHASISWA ",hasil[1],"="*25)
				tabel = PrettyTable(["Nim", "Nama", "Fakultas", "Prodi", "Alamat"])
				print("\n")
				a = hasil[0]
				b = hasil[1]
				c = hasil[2]
				d = hasil[3]
				e = hasil[4]
				tabel.add_row([a,b,c,d,e])
				print(tabel)
				print("\n")
				print("="*70)
				i+=1

cruds = CRUD()
#cruds.update()
def show_menu():
  print("\n")
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")
  print("\n")
  #clear screen,untuk linux
  #os.system("date")

  if menu == "1":
    cruds.create()
  elif menu == "2":
    cruds.read()
  elif menu == "3":
    cruds.update()
  elif menu == "4":
    cruds.delete()
  elif menu == "5":
    cruds.cari_data()
  elif menu == "0":
   	exit()

  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu()
