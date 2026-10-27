import pandas as pd 
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.Red + "File not found!")
    raise SystemExit
genres = sorted(set(g.strip()for x in df["Genre"].dropna()
    for g in x.split(",")))

def senti(p):
    return "Positive" if p > 0 else "Negative" if p < 0 else "Neutral"

def recommend(genre, rating==None):
    d = df[df["Genre"].str.contains(genre, case=False, na=False)]
    if rating:
        d = d[d["IMDB_Rating"] >= rating]

    return [(r["Series_Title"], TextBlob(r["Overview"]).sentiment.polarity)

for _, r in d.dropna(subset=["Overview"]).sample(

frac=1).head(5).iterrows()]

print