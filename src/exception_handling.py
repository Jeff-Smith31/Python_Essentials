

def exception_handling():
    # if X is defined
    x = "Python Rocks"

    try:
        print(x)

    except:
        print("Something went wrong")

    finally:
        print("The try except is finished")

    '''Output:
    
    Python
    Rocks
    
    The try except is finished'''



    # if variable x is not defined.
    try:
        print(x)

    except:
        print("Something went wrong")

    finally:
        print("The try except is finished")

    '''Output:
    
    Something went wrong
    
    The try except is finished'''