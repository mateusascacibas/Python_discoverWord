import random 
from more_itertools import locate


cont = 0
categories = ("sport", "artist", "animal", "color")
category = random.choice(categories)
if(category == "sport"):
    words = ("soccer", "basketball", "volleyball", "tennis", "skate", "swimming", "athletics")
elif(category == "artist"):
    words = ("rihanna", "eminem", "beyonce", "bruno Mars", "anitta", "michael jackson")
elif(category == "animal"):
    words = ("lion", "monkey", "snake", "cat", "dog", "elephant", "pig", "chicken")
else:
    words = ("black", "white", "blue", "yellow", "grey", "purple", "green", "orange")

word = random.choice(words)
num_letters = len(word)
print("----------")
print("Category: " + category)
print("----------")
print("Number of letters: " , num_letters)
print("----------")
array_Word = []
contAux = 0 
while(contAux < num_letters):
        array_Word.append("_")
        contAux += 1
print(array_Word)
print("----------")
while(cont < 5):
    
    option = input("Enter a letter: ")
    print("----------")
    i = num_letters
    while(i > 0):
        if("_" not in array_Word):
            print("Yeah, congratulations!! You are sure.")
            cont = 5
            break
        if(word.__contains__(option.lower())):
            counter = (list(locate(word, lambda x: x == option.lower())))
            j = len(counter)
            while(j > 0):
                array_Word[counter[j-1]] = option
                j -= 1
            response = "This letter has"
        else:
            response = "This letter does not have"
            
        i -= 1
    print("----------")
    print(response)
    print("----------")
    print(array_Word)
    print("----------")
    cont += 1

response = input("Now you must kick and see if you hit: ")
print("----------")

if(response.lower() == word):
    print("Yeah, congratulations!! You are sure.")
else:
    print("No you are wrong, the answer is" , word)
