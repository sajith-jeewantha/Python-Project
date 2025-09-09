def greet(first_name, last_name):
    print(f"Welcome {first_name} {last_name}")


greet("John", "Smith")


###

def get_greeting(name):
    return f"Hello {name}"


message = get_greeting("john")
print(message)

file = open("content.txt", "w")
file.write(message)
file.close()


###

def increment(number, by=1):
    return number + by


print(increment(2))

print(increment(2, 5))


###
print("\n")

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5, ))
