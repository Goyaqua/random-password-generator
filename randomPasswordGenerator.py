import random
from string import ascii_letters, ascii_lowercase, digits, punctuation

def generate_random_pwd(secLevel): 
    psw = ""
    if secLevel == "1":
        for i in range(6):
            psw += random.choice(digits)
    elif secLevel == "2":
        for i in range(8):
            psw += random.choice(ascii_lowercase+digits)
    elif secLevel == "3":
        chars = ascii_letters + digits + punctuation
        for i in range(16):
            psw += random.choice(chars)
    print("Random Level {} Password: {}".format(secLevel, psw))
    return psw

def main():
    run = True
    while run:
        choice = input("Pick a security level: 1/2/3 , 0 to exit: ")
        if choice == "0": run = False
        elif choice in "123" and len(choice) == 1: generate_random_pwd(choice)
        else: print("Invalid choice, please try again.")
        
main()