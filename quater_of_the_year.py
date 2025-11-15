def get_the_months_quater_of_the_year(num):
	months = ["January" , "February", "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"]

	if num >=1 and num <= 3:
		print(f"{months[num]} is in the first quater of the year")

	elif num >= 4 and <= 6:
		print(f"{months[num]} is in the second quater of the year")


	elif num >= 7 and <= 9:
		print(f"{months[num]} is in the third quater of the year")

	elif num >= 10 and <= 12:
		print(f"{months[num]} is in the fourth quater of the year")	

	return ""