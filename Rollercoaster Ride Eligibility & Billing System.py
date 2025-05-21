print("Welcome to our rollercoaster")
height=float(input("Enter your height in cm"))
bill=0

if height>=120:
	print("You can ride the rollercoaster")
	age=int(input("What is your age? "))
	if age <= 12:
		bill = 5
		print("Child tickets are $5.")
	elif age <= 18:
			bill = 7
			print("Youth tickets are $7.")
	elif age>25:
				bill = 12
				print("Adult tickets are $12.")
	photo=input("Do you want to have a photo take? Type y for Yes and n for No.")
	if photo == "y":
		bill+=3
		print(f"Your final bill is ${bill}")
else:
	print("Sorry you have to grow taller before you can ride.")