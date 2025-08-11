from datetime import date, datetime
from math import ceil



def datetime_manipulation():

    start_date = date(2022, 1, 10)
    end_date = date(2022, 11, 10)
    print((end_date - start_date).days)


    #Find the difference between two dates in months.
    start_date = date(2022, 1, 10)
    end_date = date(2022, 11, 10)
    no_of_months = ceil((end_date - start_date).days / 30)

    print(no_of_months)

    #Ouput
    '''11'''

    #check if the given date is a weekday or weekend from datetime import datetime

    week_date = date(2022, 3, 3)
    week_date.weekday() <= 4

    '''True'''


    week_date = date(2022, 3, 6)
    week_date.weekday() > 4

    '''True'''


    date_string = "2022-03-10 10:10:10"

    print(datetime.fromisoformat(date_string))

    '''2022 - 03 - 10
        10: 10:10'''


