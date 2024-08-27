"""Here we are going to check an input of passwords that are link to employees or customers, 
and use python to determine if they are strong, or weak passwords. Furthermore, we will only
allow strong passwords to be used and weak passwords will not be accepted"""

#First create requirments for strong password
#We will say the requirements are length of atleast 8 characters, atleast one uppercase letter, and one number

#we will also use import re to use some helpful functions

import re

userInputPassword = str(input("Enter your password here: "))

#Now the user will have chosen their password and it is our job to write a algorithm to check its strength
#Since it has to meet all requirements, we will go in order, and if it fails any condition, it will not be a valid password

#first we check the length of the password

if len(userInputPassword) < 8:
  print("This password is weak")

#then check that it contain atleast one uppercase
#The logic behind this is that we will see if the lower case version of the string is the same 
#as the normal version, if so then there are no uppercase letter present

elif userInputPassword.lower() == userInputPassword:
  print("This password is weak")

#Now we want to finally see if there is atleast one number
#We will use the findall function and use "\d" to search for digits in the string
#This will output a list of digits and if the length of the list is 0 then that means there were no digits in the password

elif len(re.findall("\d", userInputPassword)) == 0:
  print("This password is weak")

else:
  print("This password is valid")
  


