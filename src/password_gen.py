import string
from random import *


def password_generation():
    characters = string.ascii_letters + string.punctuation  + string.digits

    try:

      length = int(input("Enter an integer number: "))

      password = "".join(choice(characters) for x in range(length))

      print(password)

    except ValueError:

        print("Please input integer only") 