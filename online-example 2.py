# imports

import time
import random
import os

# Variables def

umoney = 0
uname = ''
ucert = 'NO'
ujob = ''
uearning = 0
uexp = 0
# urep = 0
unet = 0
cname = ''
clevel = 0
cnet = 0
cearning = 0
cowner = 0

# Startup

print('-------------------------------------------------------')
print('|                Welcome to LineLife!                 |')
print('|   LineLife is a real life simulation game in which  |')
print('|   you can become what ever you want example :       |')
print('|       Programmer, Footballer, Photographer, ETC     |')
print('|                                                     |')
print('|    # Money earned :                                 |')
print('|           Programmer : $500 - $700                  |')
print('|           Footballer : $600 - $650                  |')
print('|           Doctor : $700 - $750                      |')
print('|           Photographer : $200 - $400                |')
print('|           Poet : $150 - $250                        |')
print('|     #NOTE : THESE ARE WITHOUT CERT!                 |')
print('|                                                     |')
print('|   If you have cert then you earn more by doing your |')
print('|   jobs.Cert is when you study about the job and get |')
print('|   certification                                     |')
print('|                                                     |')
print('|           LETS START WITH THE GAME THEN!            |')
print('|                                                     |')
print('|                     Credits:                        |')
print('|         Rivan Nirmal Juthani ( Game Owner )         |')
print('| _This box will stay for 0*0 seconds before it goes_ |')
print('-------------------------------------------------------')
time.sleep(5)

# Main Simulation

print('-------------------------------------------------------')
print('|            Select a job from the list               |')
print('|                                                     |') 
print('|           Programmer : 1                            |')
print('|           Footballer : 2                            |')
print('|           Photographer: 3                           |')
print('|           Poet : 4                                  |')
print('-------------------------------------------------------')
userinputtemp = input('Enter a number : > ')
if userinputtemp == '1':
	os.system('clear')
	
	# New Var def
	
	ujob = 'Programmer'
	
	# Main Header def
	
	def gameheader():
		print('--------------------------------------------------------')
		print('|   Player Name :',uname,'Player Job :',ujob)
		print('|   Player Money :',umoney,'Player Exp :',uexp)
		print('|   Player Cert :',ucert)
		print('----------------------------')
		return
	
	def gamebank():
		os.system('clear')
		print('--------------------------------------------------------')
		print('|              Welcome to LineBank(R)!                 |')
		print('| Here you can check your bank account deposited money |')
		print('| Here are your details :                              |')
		print('--------------------------------------------------------')
		print('|      Name :',uname,' Money :',umoney)
		print('----------------------')
		return
	
	def gameshop():
		os.system('clear')
		print('--------------------------------------------------------')
		print('|                  Welcome to shop!                    |')
		print('|')
	
	
	
	# Main Start ::
	
	print('--------------------------------------------------------')
	print('| (+) Welcome to LineLife!                             |')
	print('|                                                      |')
	print('|    You have selected to become a Programmer! Nice!   |')
	print('|    You will earn :                                   |')
	print('|    Programmer : $500 - $700 (Without Cert)           |')
	print('|    Programmer : $15,000 (With Cert)                  |')
	print('|                                                      |')
	print('--------------------------------------------------------')
	uname = input('Enter your in-gamename : ')
	os.system('clear')
	gameheader()
	userinputtemp = input('LineLife:> ')
	if userinputtemp == 'help':
		print('--------------------------------------------------------')
		print('|                 Welcome to help!                     |')
		print('|  Commands :                                          |')
		print('|      help : To show this help box                    |')
		print('|      bank : To see your bank account information     |')
		print('|      study : To study about you job to get a cert    |')
		print('|      shop : To see the items you can buy             |')
		print('|                                                      |')
		print('|        MORE COMING SOON GIVE SOME TO ME!             |')
		print('--------------------------------------------------------')
	if userinputtemp == 'bank':
		gamebank()
	if userinputtemp == 'shop':
		gameshop()
	
	# After 
	
	
	
	
	
	
	




if userinputtemp == '2':
	print('Hello World!')
if userinputtemp == '3':
	print('Hello World!')
if userinputtemp == '4':
	print('Hello World!')
	
