new_file = open('new_File12.txt', 'x')
new_file.close()

import os
print("Checking if my_file exists or not....")
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("The file does not exist")

my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Atharv and I am 10yr old.")

os.remove('Codingal.txt')