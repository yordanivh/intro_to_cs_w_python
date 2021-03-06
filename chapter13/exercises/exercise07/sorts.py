def find_min(L: list, b: int) -> int:
    """Precondition: L[b:] is not empty.
    Return the index of the smallest value in L[b:].

    >>> find_min([3, -1, 7, 5], 0)
    1
    >>> find_min([3, -1, 7, 5], 1)
    1
    >>> find_min([3, -1, 7, 5], 2)
    3
    """
    smallest = b # The index of the smallest so far
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            # W e found a smaller item at L[i]
            smallest = i
        i = i + 1

    return smallest

def selection_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7,-1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        # Find the index of the smallest item in L[i:]
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i] 
        i = i + 1
    return L


