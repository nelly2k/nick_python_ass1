def create_key():
    print("I'm creating key")

print("Please select option")
print("1. Encrupt key")
print("2. decrypt key")
print("3. exit")
user_input = input()

while user_input!=3:
    print("user entered: " + user_input)
    if user_input == "1":
        create_key()
    else:
        print("incorrect input")
    break
        