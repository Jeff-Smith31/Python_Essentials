from faker import Faker

def faker_to_create_data():
    fake = Faker()

    name = fake.name()
    print(name)

    address = fake.address()
    print(address)

    text = fake.text()
    print(text)

def lambdas():


    # The lambda keyword creates an inline function that contains a single expression. The value of this expression is what the function returns when invoked.
    # Use it inside a function

    '''def transform(n):
        return lambda x: x + n


    f = transform(3)

    f(4)
    '''

    # simple lambda function
    print(lambda x: x ** 2 + 2 * x - 5)

    a = lambda x: x + 1

    print(a(1))


    # regular function

    def a(x): return x + 1

    print(a(1))


def filter_function():
    l1 = [10, 20, 30, 40, 50, 60, 70, 80]

    print([i for i in filter(lambda x: x > 30, l1)])

    '''    Output
    [40, 50, 60, 70, 80]'''

