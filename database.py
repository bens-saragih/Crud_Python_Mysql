

import mysql.connector 

class Database:

	def __init__(self,nama_database):
		self.__nama_database = nama_database


	def setServer(self,server):
		self.__server = server


	def setUsername(self,username):
		self.__username = username

	def setPassword(self,password):
		self.__password = password


	def setTableName(self,namaTable):
		self.__nama_table = namaTable


	def createDatabase(self):
		db = mysql.connector.connect(
			host = self.__server,
			user = self.__username,
			passwd = self.__password
			)

		cursor = db.cursor()
		cursor.execute("CREATE DATABASE IF NOT EXISTS "+self.__nama_database)

		if cursor.rowcount == 1:
			return ("Database "+self.__nama_database+" berhasil dibuat")	

		else:
			return ("Database "+self.__nama_database+" sudah ada")



	def koneksiDb(self):
		db = mysql.connector.connect(
			host = self.__server,
			user = self.__username,
			passwd = self.__password,
			database = self.__nama_database
			)

		self.__db = db

	def createTable(self):
		self.koneksiDb()

		cursor = self.__db.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS "+self.__nama_table+" (nim INT PRIMARY KEY, nama VARCHAR(50), fakultas VARCHAR(50), prodi VARCHAR(50), alamat VARCHAR(100))")
		
		if cursor.rowcount == 1:
			print("Table "+self.__nama_table+" berhasil dibuat")
		else:
	 		print("Table "+self.__nama_table+" sudah ada")







