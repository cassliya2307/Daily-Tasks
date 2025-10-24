def true_love(flower_1 , flower_2):

	if type(flower_1) and type(flower_2):
		if flower_1 % 2 == 0 and flower_2 % 2 != 0:
			return True

		elif flower_1 % 2 != 0 and flower_2 % 2 == 0:
			return True


		else:
    			return False
	else:
		raise TypeError("Invalid Input")


#flower_1 = int(input("Enter number of petals: "))

#flower_2 = int(input("Enter number of petals: "))

#print(true_love(flower_1 , flower_2))