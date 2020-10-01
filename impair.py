#usr/bin/env python3
def impair(array):

	arr_1 = [] 
	count = 0
	for  i in array:
		count = 0
		
		for j in i:
			if '1' in j:
				count = count + 1
		if (count % 2 > 0):
			arr_1.append("0"+i)
		else:
			arr_1.append("1"+i)
	return arr_1
	
numb = int(input("Entrez un chiffre: ")) 

new_numb = "{0:b}".format(numb)
print("Le binaire du chiffre est: ", new_numb)

array = [new_numb]
print("Le resultat apres la parite impair est: ", impair(array))
