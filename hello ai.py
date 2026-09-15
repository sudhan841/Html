print("Hello! I am AI bot. What is your name?")

name = input()

print(f"Nice to meet you, {name}!")

print("How are you feeling today? (good/bad) : ")
mood = input().lower()

if mood == "good":
    print("I am glad to hear that!")
elif mood == "bad":
    print("I am sorry to hear that.I hope things get better for you soon.")
else:
    print("I see. Sometimes it is hard to put feelings into words.")

    print(f"It was nice chatting with you, {name}. Have a great day!")