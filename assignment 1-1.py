print("Registration Form")
print("please fill out the details below")
print("===========================================================")
print()
First_Name = input("your first name here:     ")
Last_Name = input("your last name here:       ")
Birth_Year = input("the year you were born      ")
temporary_password = First_Name + ("*") + Birth_Year

print()
print(f"Welcome\t{First_Name} {Last_Name}!")
print("Your registration is complete.")
print(f"your temporary password is:\t{temporary_password}")
