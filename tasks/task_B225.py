b = """1000.00!=
125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10"""

b1sol = """Original Balance: 1000.00\r
125 Market 125.45 Balance 874.55\r
126 Hardware 34.95 Balance 839.60\r
127 Video 7.45 Balance 832.15\r
128 Book 14.32 Balance 817.83\r
129 Gasoline 16.10 Balance 801.73\r
Total expense  198.27\r
Average expense  39.65"""

a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

c=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

bsol="""Original Balance: """

value='' # 1000.00

minus='' # 125.45, 34,95, ...

raskhod=0 #весь расход

kr=0 #количество расходов

b+='\n'
b=b.replace('!','')
b=b.replace('?','')
b=b.replace('=','')
b=b.replace(';','')
b=b.replace(':','')
b=b.replace('{','')
b=b.replace('}','')
b=b.replace(' ','')
b=b.replace(',','')


'''
Теперь b=
1000.00\n                                                                                                          
125Market125.45\n                                                                                                    
126Hardware34.95\n                                                                                                   
127Video7.45\n                                                                                                       
128Book14.32\n                                                                                                       
129Gasoline16.10\n
'''

for i in range(len(b)):
    
    if(b[i]!='.'):
        bsol+=b[i]
        value+=b[i]
        
    else:
        bsol+=b[i]
        bsol+=b[i+1]
        bsol+=b[i+2]
        bsol+='\n'
        value+=b[i]
        value+=b[i+1]
        value+=b[i+2]
        break

value=float(value)

for i in range(len(b)):
    if(b[i]=='\n'):
        index=i+1
        break

for i in range(index, len(b)):
    
    if((b[i-1] in a) and (b[i] in c)):
        bsol+=' '
        bsol+=b[i]
        while(b[i]!='\n'):
            minus+=b[i]
            i+=1
            
        
    else:
        if((b[i-1] in c) and (b[i] in a)):
            bsol+=' '
        bsol+=b[i]
        if(b[i-1]=='.'):
            bsol+=" Balance "
            value=round((value-float(minus)),2)
            raskhod+=float(minus)
            kr+=1
            bsol+=str(value)
            minus=''
            
        
bsol+="Total expense "
raskhod=round(raskhod,2)
bsol+=str(raskhod)
bsol+='\n'
bsol+="Average expense "

sr=round(raskhod/kr,2)

bsol+=str(sr)

print(bsol)
