import random

def password_generator(number, len):

    chars = ("qwertyuioplkjhgfdsazxcvbnm1234567890!@")

    for p in range(number):
        password = ("")
        for c in range(len):
            password += random.choice(chars)
        print(password)       

password_generator() #you need to enter two arguments 
