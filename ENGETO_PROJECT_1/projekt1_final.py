"""
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author: Katerina Carbolova
email: carbolovak@hotmail.com
"""

# registered_users

separator = "-" * 50
registered_users = {
    "bob" : "123",
    "ann" : "pass1234",
    "mike" : "password123",
    "liz" : "pass123"
}

#  texts for analysis

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# login

username = input("username:")
password = input("password:")

print(separator)

if registered_users.get(username) == password:
    print(f"Welcome to the app, {username.capitalize()}.")
    print(f"We have {len(TEXTS)} texts to be analyzed.", separator, sep ="\n")

# select number

    try:
        selected_number = int(input("Enter a number between 1 and {len(TEXTS)} to select:"))
        if selected_number not in range(1,len(TEXTS) + 1):
            print(f"Selected number not in range, terminating the program...", separator, sep="\n")
            quit()
        else:
            print(f"Below is the analysis of your selected text.", separator, sep="\n")
    except ValueError:
        print(f"Selected value is not a number, terminating the program...", separator, sep="\n")
        quit()


# analysis

    words = []

    results = {
        "word_counts" : 0,
        "title_case" : 0,
        "upper_case" : 0,
        "lower_case" : 0,
        "numeric_string" : 0,
        "numbers_sum" : 0
    }

    for word in TEXTS[selected_number-1].split():
        stripped_word = word.strip(".,-")
        words.append(stripped_word)
        results["word_counts"] = len(words)
    
        if stripped_word.istitle():
            results["title_case"] += 1
        elif stripped_word.isupper():
            results["upper_case"] += 1
        elif stripped_word.islower():
            results["lower_case"] +=1
        elif stripped_word.isdigit():
            results["numeric_string"] += 1
            results["numbers_sum"] += int(stripped_word)
    
    print(f"There are {len(words)} words in the selected text.") 
    print(f"There are {results["title_case"]} titlecase words.")
    print(f"There are {results["upper_case"]} uppercase words.")
    print(f"There are {results["lower_case"]} lowercase words.")
    print(f"There are {results["numeric_string"]} numeric strings.")
    print(f"The sum of all the numbers is {results["numbers_sum"]}.")
    print(separator)

# chart

    print("LEN |  OCCURENCES  |NR.")
    print(separator)

    lengths = {}
    for stripped_word in words:
        length = len(stripped_word)
        lengths[length] = lengths.get(length, 0) + 1
       
    for length in sorted(lengths):
        print(f"{length:<4}| {"*"*lengths[length]} {lengths[length]}")
    
    print(separator)
    print(f"Thank you for using our app, {username.capitalize()}.")
    quit()

else:
  print("Unregistered user, terminating the program...")
  quit()