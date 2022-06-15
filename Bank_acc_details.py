# inheritance concepts --> single inheritance and multiple inheritance
# POLYMORPHISM and MTD OVERRIDDING
# Abstract method

from atm import accessing
from abc import ABC, abstractmethod

class Atm(ABC):

	@abstractmethod
	def atm_process(self):
		pass

class show_details(Atm):
	# overriding abstract method
	def atm_process(self):
		accessing()

processing = show_details()


# Base class User which holds the name of the Applicant
class User:
	def __init__(self,name):
		self.name = name		

# This is a child class which is inherited the User class
class currentaccount(User):
	def __init__(self,name,account_name="Current_accont",balance=100):
		super().__init__(name)
		self.account_name = account_name
		self.balance = balance
# __init__ method which is used to holds the acoount_name and balance 
# super() is a inbuilt function which is used to access te mtds of the parent/base class

	def welcome(self):
		print('Welcome to your Current Account : {} '.format(self.name))

	def deposit(self,value):
		self.balance = self.balance + value
		print("Net Amount :",self.balance)
# deposit is used to mainatain the deposition amt with the currenr balance amt

	def withdraw(self,value):
		if value >= 1000:
		 	print("you will have to phone the bank manager\n")
		else:
			self.balance = self.balance - value
			print("Available Balance : ",self.balance)
# withdrawal is used to withdraw the amt from the current_account
# if the amt is greater/equal to 1000rs it will return the error msg else if the amt is less 1000rs gives the available balance 
# with the minus amt of withdrawn

class savingsaccount(User):
	def __init__(self,name,account_name="Savings_account",balance=100):
		super().__init__(name)
		self.account_name = account_name
		self.balance = balance
	 	
	def welcome(self):
		print('Welcome to your Savings Account : {} '.format(self.name))

	def deposit(self,value):
		self.balance = self.balance + value
		print("Net Amount :",self.balance)

	def withdraw(self,value):
		self.balance = self.balance - value
		print("Available Balance:",self.balance)

# Savingsaccount class is same as the currentaccount class

currentobject = currentaccount("Sreeni")
# currentobject is the obj of currentaccount class

savingsobject = savingsaccount("Sreeni")
# savingsobject is the obj of savingsaccount class


while True:
	print("")
	print("1.current account")
	print("2.saving account")
	print("3.ATM Processing")
	menu_option = int(input())
	
	if menu_option == 1:
		currentobject.welcome()
		print("")
		#sub_options for currentaccount to find the deposit and withdraw amount
		print("1.deposit funds")
		print("2.withdraw funds")
		submenu_option=int(input())

		if submenu_option == 1:
			# when the input is 1 this calls the deposit method from the currentaccount class to deposit the amount 
			value=int(input("how much would you like to deposit :"))
			currentobject.deposit(value)

		elif submenu_option == 2:
			# when the input is 2 this calls the withdraw method from the currentaccount class to withdraw the amount 
			value=int(input("how much would you like to withdraw :"))
			currentobject.withdraw(value)

		else:
			print("wrong menu choice")

	elif menu_option == 2:
		currentobject.welcome()
		print("")
		#sub_options for savingsaccount to find the deposit and withdraw amount
		print("1.deposit funds")
		print("2.withdraw funds")
		submenu_option=int(input())

		if submenu_option == 1:
			# when the input is 1 this calls the deposit method from the savingsaccount class to deposit the amount 
			value=int(input("how much would you like to deposit :"))
			savingsobject.deposit(value)

		elif submenu_option == 2:
			# when the input is 2 this calls the withdraw method from the savingsaccount class to withdraw the amount 
			value=int(input("how much would you like to withdraw :"))
			savingsobject.withdraw(value)
		else:
			print("wrong menu choice")

	else:
		# when the option is selected as 3 this calls the function of abstract method
		processing.atm_process()