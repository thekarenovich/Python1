with open("text.txt", "w") as file_1:

	file_1.write("Soviet postage stamp dedicated to the cartoon(1988) is a Soviet animated film made by Yuri Norstein in 1975 at the Soyuzmultfilm studio. The work is based on the fairy tale story of the same name by Sergei Kozlov, which was significantly revised during the writing of the script. The film tells the story of a Hedgehog who, on his way to visit a Bear Cub, gets lost in the fog and finds himself in a mysterious world where an Owl, a Snail, a Bat and a white Horse live. Among the technical means used by Norstein and the operator of the tape Alexander Zhukovsky — is the use of tiered scenery, thanks to which the was realized. The main character, as well as the entire film, was drawn by the animator Francesca Yarbusova. The musical background was created by the composer Mikhail Meerovich. Actors Maria Vinogradova, Vyacheslav Nevinny, Alexey Batalov were involved in the voice-over.The researchers note that the style of the film was influenced by the cultural traditions of different countries and peoples (including theater and painting of the East, works by Paul Klee, Andrey Rublev, Yuri Vasnetsov). In 1979, the creators of the film Norstein, Zhukovsky and Yarbusova became laureates of the USSR State Prize in Literature, art and architecture The Fox and the Hare (1974),(1975) Laputa""Hedgehog in the Fog")

	file_1.close()

def point_3() :

	#3.1
	with open("text.txt", "r") as file_1:
		print(file_1.read())
		file_1.close()


	#3.2 и 3.3
	with open("text.txt", "r") as file_1:
	    
	    m=[]
	    
	    dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	    for line in file_1:
	        for j in line:
	            for i in range(len(dictionary)):
	                if(j==dictionary[i] or j==' ' or j==dictionary[i].upper()):
	                    m.append(j)
	                    break
	    
	file_1.close()

	print()
	print()
	print()

	
	#3.4
	s=("".join(m)) # строка 
	print('3.4')
	print(s)

	#3.5
	d={}

	word=''
	
	kmax=0
	
	kol=[]

	for i in s:
		if(i!=' '):
			word+=i
		else:
		    k=s.count(word)
		    d[word]=k
		    word='' 
		    
	d.pop('')
		        
	print()
	print()
	print(d)
	print()
	print()
	
	#3.6 и 3.7
	
	dm=[]
	
	for i in range(10):
	    Keymax = max(d, key=d.get)
	    print(Keymax, d[Keymax])
	    d.pop(Keymax)
	
	print()
	 
	for i in range(10):
	    Keymin = min(d, key=d.get)
	    print(Keymin, d[Keymin])
	    dm.append(d[Keymin])
	    d.pop(Keymin)
	
	for i in range(10):
	    d["PYTHON"]=dm[i]
	    
	print()
	print()
	print(d)
	print()
	print()
	
	#3.8 и 3.9
	
	quantity=0
	
	word=''
	
	with open("text2.txt", 'w') as fuckfile:
	    
	    for i in range(len(s)):
	        
	        if(s[i]!=' '):
	            
	            word=word+s[i]
	        else:
	            if(quantity+len(word)+1<100):
	                quantity+=len(word)
	                quantity+=1
	                fuckfile.write(word)
	                fuckfile.write(' ')
	            else:
	                fuckfile.write("\n")
	                fuckfile.write(word)
	                quantity=len(word)
	            word=''
                

point_3()
