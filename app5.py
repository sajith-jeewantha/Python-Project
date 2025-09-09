income = False
credit = True

if income and credit:
    print("Eligible")
else:
    print("Not Eligible")

if income or credit:
    print("Eligible")
else:
    print("Not Eligible")

###

student = True
if not student:
    print("Student is eligible")
else:
    print("Student is not eligible")

###


if income and credit and not student:
    print("Student credit is Eligible")
else:
    print("Student credit is Not Eligible")

if income or credit or not student:
    print("Student credit is Eligible")
else:
    print("Student credit is Not Eligible")

age = 22
if age >= 18 and age <= 65:
    print("Age is Eligible")

if 18 <= age <= 65:
    print("Age is Eligible")

###

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
