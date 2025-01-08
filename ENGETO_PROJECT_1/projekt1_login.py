# registered_users

separator = "-" * 50
registered_users = {
    "bob" : "123",
    "ann" : "pass1234",
    "mike" : "password123",
    "liz" : "pass123"
}

# login

username = input("username:")
password = input("password:")

print(separator)

if registered_users.get(username) == password:
  print(f"Welcome to the app, {username.capitalize()}.")
  print(f"We have 3 texts to be analyzed.", separator, sep="\n")

else:
  print("Unregistered user, terminating the program...")