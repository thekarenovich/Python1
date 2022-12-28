# quit, exit - как break в цикле, только они останавливают всю программу

for i in range(10):
	if i == 5:
		print(quit)
		quit()
	print(i)


for i in range(10):
	if i == 5:
		print(exit)
		exit()
	print(i)
