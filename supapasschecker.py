import math
import string
import getpass

banner = '''
 ████ █   █ ████   ███  ████   ███   ████  ████     ███  █   █ █████  ███  █   █ █████ ████    
█ ░░░░█░  █░█░░░█ █ ░░█ █░░░█ █ ░░█ █ ░░░░█ ░░░░   █ ░░░ █░  █░█░░░░░█ ░░░ █░ █ ░█░░░░░█░░░█   
 ███░░█░░ █░████░░█████░████░░█████░ ███░░░███░░░  █░ ░░░█████░████░░█░ ░░░███ ░ ████░░████░░  
  ░░█ █░░ █░█░░░░ █░░░█░█░░░░ █░░░█░░ ░░█   ░░█    █░░   █░░░█░█░░░░ █░░   █░░█ ░█░░░░ █░░█░ ░ 
████░░ ███ ░█░░░░░█░░░█░█░░░░░█░░░█░████░░████░░    ███  █░░░█░█████░ ███  █░░░█ █████░█░░░█░  
 ░░░░ ░ ░░░ ░░░    ░░  ░░░░    ░░  ░░░░░░ ░░░░░ ░    ░░░  ░░  ░░░░░░░  ░░░  ░░  ░ ░░░░░ ░░  ░  
  ░░░░   ░░░  ░     ░   ░ ░     ░   ░ ░░░░  ░░░░      ░░░  ░   ░ ░░░░░  ░░░  ░   ░ ░░░░░ ░   ░ 
'''
print(banner)


min_length = 7
max_length = 30

def calculate_entropy(password):
    """Calculates entropy based on character diversity and length."""

    charset_size = 0
    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26
    if any(c in string.digits for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)
    if any(c.isspace() for c in password):
        charset_size += 1

    return len(password) * math.log2(charset_size) if charset_size else 0

def check_password_strength(remarks=None):
    """Evaluates password strength based on entropy and diversity."""
    password = getpass.getpass('Enter your desired password: ')

    if len(password) < min_length or len(password) > max_length:
        print(f"Your password must be between {min_length} and {max_length}")
        return

    lower_count = sum(1 for c in password if c in string.ascii_lowercase)
    upper_count = sum(1 for c in password if c in string.ascii_uppercase)
    num_count = sum(1 for c in password if c in string.digits)
    special_count = sum(1 for c in password if c in string.punctuation)
    wspace_count = sum(1 for c in password if c.isspace())

    entropy = calculate_entropy(password)

    if entropy < 28:
        remarks = "🥸Weaaaaak: This password can be easily guessed, Change it to something stronger!"
    elif entropy < 36:
        remarks = "😅Basically 123: Could be cracked quickly. Try something stronger!"
    elif entropy < 60:
        remarks = "🙂‍↕️Mid: Decent, this will work could be improved but don't double use!"
    elif entropy < 80:
        remarks = "😎Buffed: Harder to guess, consider making it longer could be brute forced."
    else:
        remarks = "🤩SupaPass: This is the best Password you could choose! Highly secure and harder to brute force!"


    print("\n Password Analysis:")
    print(f" {lower_count} lowercase letter")
    print(f"{upper_count} uppercase letter")
    print(f"{num_count} number")
    print(f"{special_count} special character")
    print(f"{wspace_count} whitespace characters")
    print(f"Entropy Score: {entropy: .2f} bits")
    print(f"Remarks: {remarks}\n")
    return None

def check_another_password():
    """Asks the user if they want to check another password."""
    while True:
        choice = input("🔄 Do you want to check your desired password? (yes/no): ").strip().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            print("👋 Exiting... Stay secure!")
            return False
        else:
            print("⚠️ Invalid input. Please enter 'yes' or 'no'.")

if __name__ == '__main__':
    print("===== 🔑 Welcome to SupaPass the Password Strength Checker 🔑 =====")
    while check_another_password():
        check_password_strength()
