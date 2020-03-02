#Code to change path entension of a file 
import os
print ("Do You want to Hack the file")
ques = int(input("If Yes press 1 If No press 2:"))
#answer in 1 & 2  
if (ques == 1):
     virus_file = 'virus.txt'
     base = os.path.splitext(virus_file)[0]
     print ("changing the base path of the  file.....")
     os.rename(virus_file,base + '.bin')

     print("Successfully Hacked the file....")
elif (gues == 2):
	print ("Program Abort.....")

else:
	print ("wrong output")
#change directory to current folder and execute this file like python virus.py
#now answer in 1 & 2 then press enter
#program run successfuly 