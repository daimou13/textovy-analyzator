TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("username: ")
password = input("password: ")

if username in users and users[username] == password:
    print(f"Welcome to the app, {username}")
else:
    print("Unregistered user, terminating the program.")
    quit()

print("-" * 40)
print(f"We have {len(TEXTS)} texts to be analyzed.")
print("-" * 40)

text_number = input(
    f"Enter a number btw. 1 and {len(TEXTS)} to select: "
)

if not text_number.isdigit():
    print("Invalid input, terminating the program.")
    quit()

text_number = int(text_number)

if text_number < 1 or text_number > len(TEXTS):
    print("Invalid text number, terminating the program.")
    quit()

selected_text = TEXTS[text_number - 1]

words = selected_text.split()

clean_words = []

for word in words:
    clean_word = word.strip(".,")
    clean_words.append(clean_word)

titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
numbers_sum = 0

for word in clean_words:
    if word.istitle():
        titlecase_words += 1

    if word.isupper():
        uppercase_words += 1

    if word.islower():
        lowercase_words += 1

    if word.isnumeric():
        numeric_strings += 1
        numbers_sum += int(word)

print("-" * 40)
print(f"There are {len(clean_words)} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numeric_strings} numeric strings.")
print(f"The sum of all the numbers {numbers_sum}")