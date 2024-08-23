import secrets
import string
import random
 
def  main():
    
    letters = string.ascii_letters
    
    digits = string.digits
    
    special_char = string.punctuation
    
    password_list = letters + digits + special_char
    
    password_len = 10
    
    password = " "
    
    for i in range(password_len):
        password += ''.join(secrets.choice(password_list))
        
    print(password)
    
    
if __name__ == "__main__":
    main()