"""Here we want to develop an algorithm that will help us scan a log file with reports, and print out suspicious activity statements. 
For example some suspicious statements could be: Login failed, Unauthorised access. 
We want to then create a list of these statements and see what is going on in the log"""

#log file is log_file.txt

logFile = "log_file.txt"

#log file for suspicious logs is

suspiciouslogsFile = "suspicious_log_file.txt"

#Open this log file for readability and use the read() function

with open(logFile, "r") as file:
	logActivity = file.read();

#Create a empty list that will be used to store suspicious activity

suspiciousLogs = []

#Now we have to turn logActivity from a string to a list

logActivity = logActivity.split()

#Now we must check all items in the logActivity list and if they match our condition
#We will then have to put them into the suspiciousLogs List using append()
#This function will allow us to add the string to the end of the list


for i in logActivity:
if i == "Login failed" or i == "Unauthorised access":
	suspiciousLogs.append(i)

	#Now we have a list called suspiciousLogs that hold the possible suspicious strings
	#We can print this information to the screen

	print(suspiciousLogs)

	#Or we can make it back into a string and then into a file, and append is using “a”

	suspiciousLogs = "\n".join(suspiciousLogs)

	with open(suspiciouslogsFile, "a") as file:
		file.write(suspiciousLogs)
