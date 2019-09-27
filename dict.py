import json
from difflib import get_close_matches

data = json.load(open("D:/Projects/Dictionary/data.json"))
word=''

def confirmation(ch, it=0):
    i= it 
    if ch == 'y':
        print (word)
        return data[get_close_matches(w, data.keys())[0]]
    elif ch == 'n':
        return  "The word doesn't exist, please check it"
    elif(i >=2):
        return "You think this is fun? Try entering the word again."
    else:
        try_again = input("I didn't understand your entry, please try again.(y/n)  ")
        return (confirmation(try_again, i+1))


def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "india" this will check for "Inida" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters acronyms like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        confirm = input("Did you mean %s? Enter y for yes, n for no.  " %
                        get_close_matches(word, data.keys())[0])
        x = confirmation(confirm)
        return x
    else:
        return "The word doesn't exist, please check it."


w = input("Enter a word:  ")
out = search(w)
if type(out) == list:
    for item in out:
        print("-->",item)
else:
    print("Error: ", out)