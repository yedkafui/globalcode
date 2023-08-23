def get_age():
    Age = int(input("Enter Age: "))
    return Age

def get_name():
    name = input("Enter Name: ")
    return name

age = get_age()
name = get_name()

print(f"{'Your name is: '}{name}")
print(f"{'Your age is: '}{age}")

