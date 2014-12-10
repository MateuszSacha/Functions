# Task 2 funtions class exercises
print("Matt's bank registration:")
def details():
    first_name, second_name, title, house_number, street, town, postcode = get_details
    display_details(first_name, second_name, title, house_number, street, town, postcode)

def get_details():
    first_name = input("Enter your first name:")
    second_name = input("Enter your second name:")
    title = input("Enter your title:")
    house_number = int(input("Enter your house number:"))
    street = input("Enter the street you live on:")
    town = input("Enter the town you live in:")
    postcode = input("Enter your postcode:")
    return first_name, second_name, title, house_number, street, town, postcode

def display_details(first_name):
    print("Congratulations {0}{1}{2}.You have successfully registered to our bank.".format(title, first_name, second_name))

