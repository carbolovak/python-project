# registered_users

separator = "-" * 50
registered_users = {
    "bob" : "123",
    "ann" : "pass1234",
    "mike" : "password123",
    "liz" : "pass123"
}

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
garpike and stingray are also present.''',
"""blabla""",
"ghjghgj"
]

# login
""""
username = input("username:")
password = input("password:")

print(separator)

if registered_users.get(username) == password:
  print(f"Welcome to the app, {username.capitalize()}.")
  print(f"We have {len(TEXTS)} texts to be analyzed.", separator, sep="\n")

else:
  print("Unregistered user, terminating the program...")
  quit()
  """""

#selected_number = int(input("Enter a number between 1 and {len(TEXTS)} to select:"))


try:
    selected_number = int(input(f"Enter a number between 1 and {len(TEXTS)} to select:"))
    if selected_number not in range(1,len(TEXTS) + 1):
       print(f"Selected number not in range, terminating the program...", separator, sep="\n")
    else:
         print(f"Selected text {selected_number}")
except ValueError:
    print(f"Selected value is not a number, terminating the program...,", separator, sep="\n")