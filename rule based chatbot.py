import random 
from colorama import Fore, init
init(autoreset=True)

places = {
    "beaches": ["bali", "maldives", "phuket"],
    "mountains": ["Alps", "Himalayas", "Rockies"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = ["Why do programmers hate nature? Because it has too many bugs!",
         "Why was the computer sick? It caught a virus!",]

def chat():
    name = input("Name: ")
    print(f"Hello {name}! Try: recommend, packing, joke, or exit")

    while True:
        while True:
            cmd = input(f"{name}: ").lower()

            if "recommend" in cmd:
                p = input("Beaches, Mountains, or Cities? ").lower()
                if p in places:
                   print("Try: " + random.choice(places[p]))
                else:
                    print("Invalid Choice!")

            elif "packing" in cmd:
                print("Pack clothes, chargers, and check the weather.")

            elif "joke" in cmd:
                print(random.choice(jokes))

            elif cmd in["exit", "bye"]:
                print("Safe travels!")
                break

            else:
                print("Try again!")
chat()