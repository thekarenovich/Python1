'''s="Было закуплено 12 единиц техники по 410.37 рублей"
digit=''
digits=['1','2','3','4','5','6','7','8','9','0']


for i in range(len(s)):

	if(s[i] in digits):
			digit+=s[i]
			if(s[i+1] not in digits):
				digit=int(digit)
				digit=digit**3
				print(digit, end='')
				digit=''

	else:
		print(s[i], end='')'''


'''import re
s="Было закуплено 12 единиц техники по 410.37 рублей"
number=''
digits=['1','2','3','4','5','6','7','8','9','0']


for i in range(len(s)):

	if(s[i] in digits):
			number+=s[i]
			if(s[i+1] not in digits):
			    s = re.sub(r number, str(int(number)**3), s)
			    print(s)
			    number=''
			    
'''


import re 

string='Было закуплено 12 единиц техники по 410.37 рублей.'

result_f=re.findall('\d{1,6}', string)

for i in result_f:
    
    string=re.sub(i, str(int(i)**3), string)
    
print(string)

