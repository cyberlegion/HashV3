import hashlib
import datetime
import os
#writing date in " saved_file.txt " FILE
tday= datetime.date.today()
txtfile="saved_file.txt"
with open(txtfile,"a") as file:
	file.write("\n=====>>>>  ")
	file.write(str(tday))
	file.write("  <<<<=====\n")
file.close()
#Running A loop for hashing the words into sha256 or md5 HASHES
while(1):
	#Inputting the string
	str=input("Enter string : ")
	#Exiting from the Program
	if(str=="exit" or str=="bye" or str=="end"):
		print("\n\n-------------------------------------------------------------------\nEXITING ..... .... ... .. .  ")
		break
	#Clearing the screen
	if(str=='(clear)' or str=='"clear"'):
		os.system('clear')
		continue
	#Choosing Options
	choice=int(input("1.SHA256            2.MD5\nEnter Option : "))
	if choice==1:
		hash=hashlib.sha256(str.encode()).hexdigest()
		print("SUCCESSFULLY CONVERTED INTO SHA256 HASH !!!")
		print("The Encrypted Code is : ",hash)
	elif choice==2:
		hash=hashlib.md5(str.encode()).hexdigest()
		print("SUCCESSFULLY CONVERTED INTO HASH FORMAT!!!")
		print("The Encrypted Code is : ",hash)
	else:
		print("Invalid Option Triggered . . . ")
	print("\n\n------------------------------------------------------------------------------------------------------------------------\n\n")
	#Saving Hashes to " Saved_file.txt " FILE 
	with open(txtfile, "a") as file:
	   file.write(str)
	   file.write("  ==>  ")
	   file.write(hash)
	   file.write('\n')
file.close()
#PROGRAM ENDED 
#Done By Program from Andhra Pradesh , India , Asia , Earth , Solar System , Star , MilkyWay Galaxy , Universe , Multiverse . . . . .