import re

password = input("Enter your password: ")

if re.match(r"^(?=.*[a-zA-Z0-9!#$%@])[a-zA-Z0-9!#$%@]{8,}$",password):
    print("Valid..")
else:
    print("Invalid..")    

