import os
from pathlib import Path
from datetime import datetime;


def f_Strings():

    #Formatting strings with f string.

    str_val = 'books'
    num_val = 15

    print(f'{num_val} {str_val}') # 15 books
    print(f'{num_val % 2 = }') # 1
    print(f'{str_val!r}') # books


    #Dealing with floats

    price_val = 5.18362
    print(f'{price_val:.2f}') # 5.18



def formatting_dates():

    date_val = datetime.utcnow()

    print(f'{date_val=:%Y-%m-%d}') # date_val=2021-09-24



def file_Existence():

    #Checking if a file exists in two ways

    #1- Using the OS module
    exists = os.path.isfile('/path/to/file')



    #2- Use the pathlib module for a better performance
    config = Path('/path/to/file')

    if config.is_file():

        pass
