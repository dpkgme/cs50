# Ask user for their name
name = input("what's your name? ").strip().title()

# split user's name into first name and last name
first, last = name.split(" ")

# Say hallo to user
print(f"hello, {last}")

