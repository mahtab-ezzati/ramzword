from random import choice, shuffle
import string

def passwordgen():
    small = string.ascii_lowercase
    capital = string.ascii_uppercase
    special = string.punctuation
    num = string.digits
   
    password = []
    password += [choice(small) for _ in range(4)]
    password += [choice(capital) for _ in range(4)]
    password += [choice(special) for _ in range(4)]
    password += [choice(num) for _ in range(4)]
   
    shuffle(password)
   
    return ''.join(password)