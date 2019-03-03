import json
from difflib import get_close_matches as gcm

# Getting the location of the json and setting it to read and write mode
data = json.load(open("D:\Ram\Projects\Python\dictionary.json", "r+"))

# function that takes the input data and prints the result


def dictionary(w):
    # converts the word to lowercase
    w = w.lower()
    
    # Checks if the i/p data is present in the dictionary
    if w in data:
        return(data[w])
    
    # Checks if the word is similar to another word in the dictionary if the input is incorrect
    elif len(gcm(w, data.keys())) > 0:
        return("Did you mean %s ?" % gcm(w, data.keys(), cutoff=0.6)[0])
        '''
            gcm is a function that compares the i/p word to the keys of the dictionary 
            and how similar they are and gives a list of the similar keys as input
        '''
    else:
        return("word doesn't exist")


word = input("Search your word: ")

output = dictionary(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)