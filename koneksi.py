import mysql.connector
from mysql.connector.errors import Error
from mysql.connector import errorcode

try:
	import database as db 
	try:
		db = db.Database("mahasiswa_db") #nama database
		db.setServer("localhost") #Nama server
		db.setUsername("root") # username database
		db.setPassword("") # password database
		print("Berhasil terhubung ke Database")
		db.createDatabase()
		db.setTableName("mahasiswa") #nama table
		db.createTable()

	except mysql.connector.Error as err:

	  if err.errno == 1045:
	    print("Username atau Password Database salah !!") 
	  if err.errno == 1049:
	    print("Database tidak ditemukan") 



	  	

except ImportError:
	print("Modul tidak ditemukan,mohon di periksa kembali")
