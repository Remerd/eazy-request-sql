import pymysql

def db_request(host, user, passwd, db, columns):
	conn = pymysql.connect(host, user, passwd, db)

	cur = conn.cursor()
	try:
		cur.execute("SELECT * FROM objects")
		rows = cur.fetchall()
		for row in rows:
			for i in range(columns):
				print(str(row[i]), end="\t")
			print()
	except Exception as e:
		print(e)
		raise
	else:
		pass
	finally:
		print("done")