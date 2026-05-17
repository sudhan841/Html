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

def menu():
    print("\n1.Add Contact")
    print("2.Remove Contact")