import time
import random
from sorts import selection_sort
from insertion_sort import insertion_sort
from exercise06 import bubble_sort_2

def built_in(L: list) -> None:

    """Call list sort --- we need our own function to do this so that we can 
    treat it as we treat our own sorts"""

    L.sort()

def print_times(L:list) -> None:
    """Print the number of milliseconds it takes for selection sortm insertion sort,
    and list.sort to run."""

    print(len(L), end='\t')
    for func in (bubble_sort_2 , selection_sort, insertion_sort, built_in):
        if func in (bubble_sort_2, selection_sort,insertion_sort) and len(L) > 10000:
            continue
        L_copy = L[:]
        t1 = time.perf_counter()
        func(L_copy)
        t2 = time.perf_counter()
        print("{0:7.1f}".format((t2-t1)*1000.), end='\t')

    print() # Print a newline.

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]:
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)