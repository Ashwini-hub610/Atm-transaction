import mysql.connector
from mysql.connector import Error
try:
	con=mysql.connector.connect(host="localhost",
			            	    database='ashu',
							    port='3306',
                                user='root',
                                password='root@123'	)
	print(con)
	cursor = con.cursor()

	con.commit()
	def pinNo(user):
		cursor=con.cursor()
		No="select pinNo from ashu.account where name=%s"
		cursor.execute(No,(user,))
		pin=cursor.fetchone()

		return pin[0]
	def withdraw(pin,amt):
		cursor=con.cursor()
		bal="select balance from ashu.account where pinNo=%s"
		cursor.execute(bal,(pin,))
		balance=cursor.fetchone()
		total=balance[0]-amt
		print("Withdraw success")
		print("Now Your Total balance is:",total)
		query="update account set Balance=%s where pinNo=%s"
		cursor.execute(query,(total,pin))
		con.commit()
		return balance[0]
	def balance(pin):
		cursor=con.cursor()
		bal="select balance from ashu.account where pinNo=%s"
		cursor.execute(bal,(pin,))
		amt=cursor.fetchone()
		return amt[0]
	def deposit(pin,amt):
		cursor=con.cursor()
		bal="select balance from ashu.account where pinNo=%s"
		cursor.execute(bal,(pin,))
		balance=cursor.fetchone()
		total=balance[0]+amt
		print("Amount Deposit Successfully")
		print("Now Your Total balance is:",total)
		query = "update account set Balance=%s where pinNo=%s"
		cursor.execute(query, (total, pin))
		con.commit()
		return balance[0]


except Error as e:
	print("Error while connecting to mysql.",e)

