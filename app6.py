for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

###
print("\n")

successful = True
for number in range(3):
    print("Attempt", number + 1)
    if successful:
        print("Success")
        break
else:
    print("Failed")

###
print("\n")
# Nested for loop

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

###
print("\n")

print(type(5))
print(type(range(5)))

# Iterable
for x in "Python":
    print(x)

print("\n")

for x in [1, 2, 3, 4]:
    print(x)

###
print("\n")

number = 100
while number > 0:
    print(number)
    number //= 2

###
print("\n")

command = ""
# while command.lower() != "exit":
    # command = input("Enter command: ")
    # print("ECHO", command)


###
print("\n")

# while True:
#     text = input("> ")
#     print("ECHO", text)
#     if text.lower() == "exit":
#         break

###
print("\n")

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers.")