from collections import defaultdict
from operator import itemgetter

def merge_lists_into_dictionary():
    keys_list = ['A', 'B', 'C']
    values_list = ['blue', 'red', 'bold']

    #There are 3 ways to convert these two lists into a dictionary

    #1- Using Python's zip, dict functionz
    dict_method_1 = dict(zip(keys_list, values_list))


    #2- Using the zip function with dictionary comprehensions
    dict_method_2 = {key:value for key, value in zip(keys_list, values_list)}


    #3- Using the zip function with a loop
    items_tuples = zip(keys_list, values_list)

    dict_method_3 = {}

    for key, value in items_tuples:

        if key in dict_method_3:

            pass # To avoid repeating keys.

        else:

            dict_method_3[key] = value

def sort_dictionary():

    dicts_lists = [
        {
            "Name": "James",
            "Age": 20,
        },
        {
            "Name": "May",
            "Age": 14,
        },
        {
            "Name": "Katy",
            "Age": 23,
        }
    ]

    # 1- Using the sort/ sorted function based on the age
    dicts_lists.sort(key=lambda item: item.get("Age"))

    # 2- Using itemgetter module based on name
    f = itemgetter('Name')
    dicts_lists.sort(key=f)

def map_list_to_dictionary():

    mylist = ['blue', 'orange', 'green']

    # Map the list into a dict using the map, zip and dict functions

    mapped_dict = dict(zip(itr, map(fn, itr)))

def merge_two_dicts():

    # merge two or more dicts using the collections module

    def merge_dicts(*dicts):
        mdict = defaultdict(list)

        for d in dicts:
            for key in d:
                mdict[key].append(d[key])

        return dict(mdict)

