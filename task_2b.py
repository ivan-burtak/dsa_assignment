import random
import time
from plots import plot_runtimes
from algorithms import merge_sort, insertion_sort, quick_sort, heap_sort
from decimal import Decimal, getcontext

getcontext().prec = 16  # increased precision for sum

# Task2_b

# sorted_arr = sort_function(arr.copy())
def generate_random_array(size):
    return [random.randint(1, 1000000) for _ in range(size)]

def measure_sort_time(sort_function, arr):
    start_time = time.perf_counter()
    sort_function(arr.copy())
    end_time = time.perf_counter()
    return Decimal(str(end_time)) - Decimal(str(start_time))

def test_runtimes(array_sizes):
    avg_runtimes = {name: [] for name in ["Merge", "Insertion", "Quick", "Heap"]}

    for size in array_sizes:
        print(f"Testing size: {size}")
        runtimes = {name: [] for name in ["Merge", "Insertion", "Quick", "Heap"]}

        for trial_num in range(3):
            print(f'Trial: {trial_num + 1}')
            arr = generate_random_array(size)

            runtimes["Merge"].append(measure_sort_time(merge_sort, arr.copy()))
            runtimes["Insertion"].append(measure_sort_time(insertion_sort, arr.copy()))
            runtimes["Quick"].append(measure_sort_time(quick_sort, arr.copy()))
            runtimes["Heap"].append(measure_sort_time(heap_sort, arr.copy()))

        for algorithm in runtimes:
            avg_runtime = sum(runtimes[algorithm], Decimal(0)) / len(runtimes[algorithm])
            avg_runtimes[algorithm].append(avg_runtime)

    return avg_runtimes


if __name__ == '__main__':
    array_sizes = [100, 1000, 5000, 10000, 25000, 45000, 60000]
    avg_runtimes = test_runtimes(array_sizes)
    plot_runtimes(array_sizes, avg_runtimes)
