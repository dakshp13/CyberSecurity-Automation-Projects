"""Developing an algorithm to help us automate a cybersecurity task. There is a file called the allow list which contains ip addresses, 
for private medical records. The ip addresses are linked to the employees. The allow list file shows who can access these records. 
There is also a list that is pre made and is not a file, called remove list which shows who should not be able to access these records.
We want to develop and algorithm to check all ip addresses, in the allow list file, and if they are also present in the remove list, 
we must take them out of the allow list as those IP addresses should not have access to the medical records"""

#file for allow list is “allow_list.txt"

#firstly create a variable for the file

allowListFile = "allow_list.txt"

#Use a with statement to read the file as give it a name ipAddresses.
#Also use the .read() function to convert it into a string

with open(allowListFile, "r") as file:
	ipAddresses = file.read()

#Use .split() function to convert it into a list

ipAddresses = ipAddresses.split()

#Now use a variable i to iterate through through the premade remove_list
#check if that variable is also in the ipAddresses List that we creates
#If it is, then remove that element from the ipAddresses List

for i in remove_list:
	if i in ipAddresses:
		ipAddresses.remove(i)

#Once the new list is created, use the join() function to make it into a string

ipAddresses = "\n".join(ipAddresses)

#Finally use the with statement again to overwrite all contents of the allowListFile
#This will ensure that only valid IP addresses will have access to the records

with open(allowListFile, "w") as file:
	file.write(ipAddresses)
