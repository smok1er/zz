import random
import time, requests, webbrowser
from time import sleep
import os
import sys
import pyfiglet
from pyfiglet import figlet_format
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
logo1 = figlet_format('aljoker',font ='banner3')
print(H+logo1)
print(E+'- '*25)
token = input(H+'- Enter Token :  ')
ID = input(K+'- Enter ID :  ')
os.system('clear')
logo2 = figlet_format('Choice',font ='banner3')
print(logo2)
print(H+'∞'*30)
print("[1] UseR #_#_#\n\n[2] UseR ##_##\n\n[3] UseR ###BOT ")
print(H+'∞'*30)
Aljoker = input('What You Need :  ')
print(H+'∞'*30)
def sh3():
	os.system('clear')
	logo1 = figlet_format('UseRs #_#_#',font ='banner3-D')
	print(logo1)
	print(H+'_'*60)
	while True:
		oip1 ='QWERTYUIOPLKMNJHBVGFCXDSZA'
		all1 = 'QAZXSWEDCVFRTGBNHYUJMKIOLP1234567890'
		u1 = str(''.join(random.choice(oip1)for i in range(1)))
		u2 = str(''.join(random.choice(all1)for i in range(1)))
		u3 = str(''.join(random.choice(all1)for i in range(1)))
		tr = '_'
		user11 = u1+tr+u2+tr+u3
		url = f"https://t.me/{user11}"
		req = requests.get(url)
		if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0: 
			print(f" \033[1;32m - work >> [ {user11} ]")
			req = requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- Hi New Telegram User .\n. — — — — —  — — — — — .\n- User :  @{user11} \n by : @H_C_4 - @BBQBBBBB''')
		else:
			print(f"\033[1;31m - Not Work >> [ {user11} ]")
def sh4():
	os.system('clear')
	logo1 = figlet_format('UseRs ##_##',font ='banner3-D')
	print(logo1)
	print(H+'_'*60)
	while True:
		oip2 ='QWERTYUIOPLKMNJHBVGFCXDSZA'
		all2 = 'QAZXSWEDCVFRTGBNHYUJMKIOLP1234567890'
		u1 = str(''.join(random.choice(oip2)for i in range(1)))
		u2 = str(''.join(random.choice(all2)for i in range(1)))
		u3 = str(''.join(random.choice(all2)for i in range(1)))
		u4 = str(''.join(random.choice(all2)for i in range(1)))
		tr ='_'
		user22 = u1+u2+tr+u3+u4
		url = f"https://t.me/{user22}"
		req = requests.get(url)
		if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0: 
			print(f" \033[1;32m - work >> [ {user22} ]")
			req = requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- Hi New Telegram User .\n. — — — — —  — — — — — .\n- User :  @{user22} \n by : @H_C_4 - @BBQBBBBB''')
		else:
			  print(f"\033[1;31m - Not Work >> [ {user22} ]")
def bot3():
	os.system('clear')
	logo1 = figlet_format('USERS ###BOT',font ='banner3-D')
	print(logo1)
	print(H+'_'*60)
	while True:
		oip3='QWERTYUIOPLKMNJHBVGFCXDSZA'
		all3 = 'QAZXSWEDCVFRTGBNHYUJMKIOLP1234567890'
		u1 = str(''.join(random.choice(oip3)for i in range(1)))
		u2 = str(''.join(random.choice(all3)for i in range(1)))
		u3 = str(''.join(random.choice(all3)for i in range(1)))
		user33 = u1+u2+u3+'BOT'
		url = f"https://t.me/{user33}"
		req = requests.get(url)
		if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0: 
			print(f" \033[1;32m - work >> [ {user33} ]")
			req = requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- Hi New Telegram User .\n. — — — — —  — — — — — .\n- User :  @{user33} \n by : @H_P_K - @C_P_8''')
		else:
			  print(f"\033[1;31m - Not Work >> [ {user33} ]")
if Aljoker =='1':
	sh3()
if Aljoker =='2':
	sh4()
if Aljoker =='3':
	bot3()
