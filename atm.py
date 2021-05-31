import backend
print("""** ** ** ** ** ** WELCOME ** ** ** ** **""")

user=input("Enter the Name:")
pwd=int(input("Enter your Pin: "))
pin= backend.pinNo(user)
#bal=backend.balance()
print("""
Welcome to ATM Machine
Choose Transaction
1)BALANCE
2)WITHDRAW
3)DEPOSIT
4)EXIT
""")

while True:
	#pwd = int(input("Enter your Pin: "))

	#pin = backend.pinNo()

	bal = backend.balance(pin)
	if pwd == pin:
		option=int(input("Enter Transaction : "))
		if(option==1):
			if pwd == pin:
				print("Your Balance is",bal)
				print("****Thanks***")
				anothertrans=input("Do you Want to make Another transaction YES/NO:")
				if(anothertrans=="YES"):
               				continue
				else:
					break

		elif(option==2):
			withdraw1=int(input("Enter amount to withdraw: "))


			if(bal>withdraw1):
				bal = backend.withdraw(pin, withdraw1)


			else:
				print("Insufficient Balance")

			anothertrans = input("Do you Want to make Another transaction YES/NO:")
			if (anothertrans == "YES"):
				continue
			else:
				break



		elif(option==3):

			deposit=float(input("Enter Amount to deposit: "))
			dep = backend.deposit(pin,deposit)


			anothertrans = input("Do you Want to make Another transaction YES/NO:")
			if (anothertrans == "YES"):
				continue
			else:
				break

		elif(option==4):
			print("closing the program")
		else:
			print("No selected transaction")
	else:
		print("****Incorrect Pin no****")
		break

