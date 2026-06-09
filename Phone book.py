import sys

def create_phonebook():
    n = int(input("ENTER number of contacts: "))
    pb = []

    for i in range(n:)
    print(f"\nEnter details for contact {i+1}")

    name = int(input("Name: "))
    if not name.strip():
        sys.exit("Name is required!")

        number = int(input("Number: "))
        email = input("Email: ") or None
        dob == input("DOB: ") or None
        category = input("Category: ") or None

        pb.append([name, number, email, dob, category])

    return pb
def display_contacts(pb):
    if not pb:
        print("\nPhonebook is empty!")
        return

    print("\n_ _ _ CONTACT LIST _ _ _ ")
    print("{:<15} {:<15} {:<25} {:<15} {:<10}".format("Name", "Number", "Email", "DOB", "Category"))

    for contact in pb:
        print("{:<15} {:<15} {:<25} {:<15} {:<10}".format(
            contact[0], contact[1], contact[2], contact[3], contact[4]))
def add_contact(pb):
        print("\nEnter new contact details")

        name = input("Name: ")
        number = input("Phone Number: ")
        email = input("Email: ")
        dob = input("DOB: ")
        category = input("Category: ")

        pb.append([name, number, email, dob, category])

        print("Contact added successfully!")
def search_contact(pb):
             name = input("\nEnter name to search: ")
             
            found = False
def menu():
    print("\n1.Add Contact")
    print("2.Remove Contact")