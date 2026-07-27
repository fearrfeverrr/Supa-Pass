import random
import supa_dict
banner = '''
 ████ █   █ ████   ███  ████   ███   ████  ████   
█ ░░░░█░  █░█░░░█ █ ░░█ █░░░█ █ ░░█ █ ░░░░█ ░░░░  
 ███░░█░░ █░████░░█████░████░░█████░ ███░░░███░░░ 
  ░░█ █░░ █░█░░░░ █░░░█░█░░░░ █░░░█░░ ░░█   ░░█   
████░░ ███ ░█░░░░░█░░░█░█░░░░░█░░░█░████░░████░░  
 ░░░░ ░ ░░░ ░░░    ░░  ░░░░    ░░  ░░░░░░ ░░░░░ ░ 
  ░░░░   ░░░  ░     ░   ░ ░     ░   ░ ░░░░  ░░░░  
'''
print(banner)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the SupaPass Generator and Strength checker!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
word_guess = input("Would you like to add a random word? (yes/no):\n").lower()

if word_guess == "yes":
    print(supa_dict)
elif "no" in word_guess:
    print('Your Password will be harder to memorize.')
else:
    print("Your Password will be harder to guess! You can use the 'SupaPass Checker' to enure quality Level.")

password_list = []
for char in range(0, nr_letters):
      password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))



print(password_list)
random.shuffle(password_list)
print(supa_dict)

password = ""
for char in password_list:
    password += char

supa_dict = ""
for char in password:
    supa_dict += char
print(f"Your password is: {password}")
