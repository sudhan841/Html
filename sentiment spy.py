from colorama import Fore, Style, init
from textblob import TextBlob
init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "Welcome to Sentiment Spy!")
name = input(Fore.Magenta + "Please enter your name: ").strip() or "Friendly agent"
print(Fore.cyan + f"Hello Agent {name}! (exit | reset | history)")

history = []

while True:
    text = input(Fore.green + "You: ").strip()
    if not text:
        print(Fore.RED + "Please enter valid text.")
        cmd = text.lower()
        if cmd == "exit":
            print(Fore.blue + f"Goodbye, Agent {name}! Stay safe out there."); break
        if cmd == "reset":
            history.clear(); print(Fore.Cyan + "History cleared."); continue
        if cmd == "history":
            if not history: print(Fore.YELLOW + "No history available."); continue

        else:
            print(Fore.CYAN + "conversation history:")
            for i,(t,p,s) in enumerate(history, 1):
                col = {"Positive": Fore.GREEN, "Negative": Fore.RED, "Neutral": Fore.YELLOW}[s]
                print(f"[{i}] {col}{t} ({p:.2f}, {s})")
            continue

        polarity = (
            ("Poitive", Fore.GREEN) if polarity < -0.05 else
            ("Negative", Fore.RED) if polarity > 0.05 else
            ("Neutral", Fore.YELLOW)
        )

        history.append((text, polarity, sentiment))
        print(f"{color}Sentiment : {sentiment} ({polarity:.2f})")