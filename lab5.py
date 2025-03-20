import random
import string

# 1
replacement_dict = {}

for _ in range(5):
    letter = input("Enter a lowercase character: ")

    while letter in replacement_dict or not letter.isalpha() or not letter.islower():
        print("This letter is already chosen or invalid. Try another one.")
        letter = input("Enter a lowercase character: ")

    replacements = set()

    while len(replacements) < 3:
        replacement = input(f"Enter a replacement for '{letter}': ")

        if len(replacement) == 1 and replacement not in replacements:
            replacements.add(replacement)
        else:
            print("Invalid or duplicate character! Try again.")

    replacement_dict[letter] = list(replacements)

print("\nReplacement Dictionary:", replacement_dict)

# 2
passwords = []
for _ in range(10):
    password = ''.join(random.choices(string.ascii_lowercase, k=12))
    passwords.append(password)

print("\nGenerated Passwords (Before Replacement):")
for pw in passwords:
    print(pw)


modified_passwords = []
for password in passwords:
    new_password = ""

    replaced_count = 0

    for char in password:
        if char in replacement_dict:
            new_char = random.choice(replacement_dict[char])
            new_password += new_char
            replaced_count += 1
        else:
            new_password += char

    modified_passwords.append((new_password, replaced_count))

# 3
categorized_passwords = {"strong": [], "weak": []}

for password, replaced_count in modified_passwords:
    if replaced_count > 4:
        categorized_passwords["strong"].append(password)
    else:
        categorized_passwords["weak"].append(password)

#4
print("\nSTRONG PASSWORDS:")
for pw in categorized_passwords["strong"]:
    print(pw)

print("\nWEAK PASSWORDS:")
for pw in categorized_passwords["weak"]:
    print(pw)
