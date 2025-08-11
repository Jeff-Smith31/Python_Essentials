import timeit


def run_time_calculator():

    start = timeit.default_timer()

    # My code goes here

    total = 0
    for i in range(10):
      total += i

    print("Sum:" ,total)
    #--------------
    stop = timeit.default_timer()
    print('Time: ', stop - start)

def progress_bar():
    from tqdm import tqdm

    for i in tqdm(range(10000000)):
        pass