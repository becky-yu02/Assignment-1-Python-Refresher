import functools
from functools import lru_cache
import time
import matplotlib.pyplot as plt

execution_times = list()


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        execution_times.append((args[0], run_time))
        print(f"Finished in {run_time:.4f}s: f({args[0]}) -> {value}")
        return value

    return wrapper_timer


@lru_cache(maxsize=None)
@timer
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_plot():
    x = [i[0] for i in execution_times]
    y = [i[1] for i in execution_times]

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("fib(n)")
    plt.ylabel("Time (s)")
    plt.show()


if __name__ == "__main__":
    fib(100)
    fib_plot()
