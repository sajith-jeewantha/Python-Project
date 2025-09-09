students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"

print(len(course_name))  # 18

print(course_name[0])  # p
print(course_name[-1])  # g
print(course_name[0:3])  # pyt
print(course_name[0:])  # Python Programming
print(course_name[:3])  # Pyt
print(course_name[:])  # Python Programming

description = "Python \"is a \'best \\practice \nprogramming language"
print(description)

first = "John"
last = "Smith"
full = f"{first} {last}"
print(full)  # John Smith

full2 = f"{len(first)} {2 + 2}"
print(full2)  # 4 4

print(course_name.upper())  # PYTHON PROGRAMMING
print(course_name.lower())  # python programming
print(course_name.title())  # python programming

rws = "      Remove whitespace  "
print(rws.strip())  # ....Remove whitespace....
print(rws.lstrip())  # ....Remove whitespace
print(rws.rstrip())  # Remove whitespace....

print(rws.find("move")) #8
print(rws.replace("white","blue")) #Remove bluespace
print("space" in rws) #True