import time


def speed_calc_decorator(function):  # decorator receives the function to wrap
    def wrapper():  # wrapper function
        start_time = time.time()      # 1. time before execution
        function()                    # 2. execute original function
        end_time = time.time()        # 3. time after execution
        duration = end_time - start_time  # 4. calculate difference
        print(f"{function.__name__} executed in: {duration}s")
    return wrapper  # return the wrapper


@speed_calc_decorator  # equivalent to: fast_function = speed_calc_decorator(fast_function)
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


# To test:
fast_function()
slow_function()
