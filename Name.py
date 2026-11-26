first_name = input("Please enter your name:")
last_name = input("Please enter your last name:")
full_name = first_name + " " + last_name
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))

print("Full Name:",full_name)
print("Age:",age)
print("Height:",height,"ft")
print(f"My full name is {full_name}, my age is {age} years old, and I am {height:.2f}ft.")
