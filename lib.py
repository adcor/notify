import sys 
import getpass
from time import sleep
from collections import defaultdict


v = "sup"
info = []
present = []

names = []
birthday = []


def createList():
	while raw_input("Are you done\n") != "done":	
		if raw_input("Would you like to enter a present ") == "yes":
			gift = raw_input("Enter a gift \n")
			present.append(gift)
			
def enterPerson():
	temp = {
	raw_input("Enter a name\n"): raw_input("Enter a birthday"); 'dog'}
	createList()
	info.append(temp)
	print info
	
enterPerson()
print info




def addList():
	createList()
	info[raw_input("Enter Key\n")] = str(present)
	

	
def addPList():
	print info
	gift = raw_input("Enter a gift idea\n")
	presents.append(gift)
	
	info.append(key)
	print info
	
	
	
	
def Choice():
	choice = str(raw_input("Would you like to add a name? Yes or no? \n"))
	if choice == "yes":
		enterPerson()
	else:
		printInfo()
		
def printInfo():
	print info
	
	
def choosePassword():
	""" Defines the password variable"""
	w = "Please choose a password \n"
	global password
	for char in w:
		sleep(0.1)
		sys.stdout.write(char)
		sys.stdout.flush()
	password = getpass.getpass()
	Verify()


def Verify():
	"""Sets up verification mechanism for 
	   user to enter different parts of the game"""
	x = raw_input("Enter Password ")
	while x != password:
		print "That's not appropriate"
		x = getpass.getpass()
	else:
		print v
	quit()
		
def Welcome():
	"""This welcomes the user"""