firstname = input("Enter your first name: ")
lastname = input(" Enter your last name: ")
year= int(input("What year were born "))
age = 2025 - year

print("Hello, " + str(lastname) + str(" ") + str( firstname) + " you are " + str(age)  ) 
if age < 18:
   print("Therefore you are not eligible to vote ")
else:   
   print("Therefore you are eligible to vote ")