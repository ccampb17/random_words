import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
words = response.content.splitlines()

words = [w.decode() for w in words]

with open('./words.txt', 'w') as f:
    for line in words:
        f.write(f"{line}\n")