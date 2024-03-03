import os
import time
import random
from colorama import Fore, Style

def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    
    return result

def get_shift():
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    return shift

def display_welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    welcome_banner = '''
           
  / _ \_______________/`/\+-/\'\'\
\_\(_)/_/ OXPLOITED19 -+-    -+-+-
 _//o\\_              \'\/+-\/`/`/
  /   \                \/-+--\/`/ 

    '''
    print(Fore.YELLOW + welcome_banner + Style.RESET_ALL)
    time.sleep(1)
    print("\nWelcome to an Encryption & Decryption experience!")
    time.sleep(1)

def display_author_info():
    author_banner = '''

      __                      
   (  )                     
 \ _\/_,'    OXPLOITED19    
--("))))))= -.._.-'-.._.-'-.
     \\                     

    '''
    time.sleep(1)
    print(Fore.CYAN + author_banner + Style.RESET_ALL)
    time.sleep(1)

def encrypt_decrypt_option():
    print("\nChoose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    option = input("Enter the option number (1/2): ")
    return option

def colorful_output(message, color=Fore.BLUE):
    print(color + message + Style.RESET_ALL)

def random_shift_generator():
    return random.randint(1, 25)

def save_to_file(message, filename):
    try:
        with open(filename, 'w') as file:
            file.write(message)
        print(f"Result saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def spinner_loading_bar():
    spinner = "|/-\\"
    for _ in range(5):  # You can adjust the number of iterations for a longer or shorter bar
        print(f"\b{spinner[_ % len(spinner)]}", end="", flush=True)
        time.sleep(0.5)  # Adjust the sleep duration for a faster or slower bar
    print()  # Move to the next line after the loading bar

def hash_loading_bar():
    for _ in range(5):  # You can adjust the number of iterations for a longer or shorter bar
        print("#", end="", flush=True)
        time.sleep(0.5)  # Adjust the sleep duration for a faster or slower bar
    print()  # Move to the next line after the loading bar

def decrypt_banner():
    decrypt_banner_art = '''
    
     /////////// 
     ////////////
 /. `//\\
o__,_||||||||||||'
    
    '''
    print(Fore.RED + decrypt_banner_art + Style.RESET_ALL)
    hash_loading_bar()

def thank_you_message():
    thank_you_art = '''
    
 .------------------.
| PRODIGY INFOTECH |
'------------------'
                                                                    
                                                                    
                                                                    
    '''
    print(Fore.MAGENTA + thank_you_art + Style.RESET_ALL)
    print("\nThank you for using OXPLOITED19's Encryption & Decryption Script!")

def main():
    display_welcome()

    option = encrypt_decrypt_option()
    message = input("\nEnter the message: ")

    if option == '1':
        shift = get_shift()
        spinner_loading_bar()
        encrypted_message = caesar_cipher(message, shift)
        colorful_output(f"\nEncrypted message: {encrypted_message}")
        decrypt_option = input("\nDo you want to decrypt the recently encrypted message? (y/n): ").lower()
        if decrypt_option == 'y':
            decrypt_banner()
            decrypted_message = caesar_cipher(encrypted_message, -shift)
            colorful_output(f"\nDecrypted message: {decrypted_message}")

    elif option == '2':
        shift = -get_shift()
        decrypt_banner()

    encrypted_decrypted_message = caesar_cipher(message, shift)
    colorful_output(f"\n{'Decrypted' if option == '2' else 'Encrypted'} message: {encrypted_decrypted_message}")

    display_author_info()

    # Additional Features
    save_option = input("\nDo you want to save the result to a file? (y/n): ").lower()
    if save_option == 'y':
        filename = input("Enter the filename (including extension): ")
        save_to_file(encrypted_decrypted_message, filename)

    random_shift_option = input("\nDo you want to generate a random shift for next time? (y/n): ").lower()
    if random_shift_option == 'y':
        print(f"Random Shift Generated: {random_shift_generator()}")

    thank_you_message()

if __name__ == "__main__":
    main()
