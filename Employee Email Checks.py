"""In this automation we want to create a function that will check an input email,
and see if it meets with company guidelines. For example lets say that all company 
emails follow the form of some alphanumeric characters then an @ and then some alphabetical
characters for the email version (gmail, yahoo, outlook, etc) and then there is a "." and 
finally some more alphabetical characters such as (com, ca, etc). This function will allow 
the user to access certain information so it is important the email is valid"""

#firstly import re to allow us to use useful functions later on
import re

#define the function that takes in an email
def validEmailCheck(userEmail):

  #Now this user email is a string so we will use the fullmatch method
  #we will put in the exact matching pattern that we are looking for and the email we are looking at
  #Then we will add it to the emailCheck variable

  emailCheck = re.fullmatch("\w+@[a-zA-Z]+\.[a-zA-Z]+", userEmail)

  #Now we will use a condition to check if the email is valid, and then print a command to the screen
  #we will check if the emailCheck is none, because if it is then the fullmatch was not successful

  if emailCheck is None:
    return print("Access Denied")

  else:
    return print("Access Allowed")
