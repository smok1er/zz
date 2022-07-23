import requests,random
F = '\033[2;32m' #اخضر
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #خرياني
id = input(B+'ايدي عزيزي => ')
tok = input(B+'حط توكن  => ')
print(Z+'='*58)
xz ='AASSDDFFGGHHJJKKLLQQWWEERRTTYYUUIIOOPPMMNNBBVVCXXZZ'
H = '1234567890'
o ='_'
while True:
	v = str("".join(random.choice(xz)for i in range(1)))
	y = str("".join(random.choice(xz)for i in range(1)))	
	g = str("".join(random.choice(xz)for i in range(1)))
	i = str("".join(random.choice(H)for i in range(1)))
	Q = v+o+g+o+y
	B = v+o+y+o+g
	C = y+o+g+o+v
	U = g+o+y+o+v
	K =g+o+i+o+v
	a =y+o+i+o+v
	BAS = [Q,B,C,U,K,a]
	Us = str(random.choice(BAS))
	z = str("".join(random.choice(xz)for i in range(1)))
	L = str("".join(random.choice(xz)for i in range(1)))	
	J = str("".join(random.choice(xz)for i in range(1)))
	W = L+o+z+o+J
	E = J+o+z+o+L
	T = L+o+J+o+z
	N = z+o+L+o+J
	BASHA = [W,E,T,N]
	USER = str(random.choice(BASHA))
	A = [Us,USER]
	USERNAME = str(random.choice(A))
	
	url=f"https://t.me/{USERNAME}"
	req = requests.get(url).text
	if '"tgme_username_link"' in req:
		print(F+'متاح  | ' + USERNAME )
		tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text= تعال صدتلك يوزر
		{USERNAME}
		@R_H_U المطور + \n''')
		i = requests.post(tlg)		
		
	else:
		print(Z+'مستخدم  | '+USERNAME)
		
		
