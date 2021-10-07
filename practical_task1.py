import time
import random
import copy

def selection_sort(A):
    counter = 0
    for i in range(len(A)-1):
        min = i
        for j in range(i+1, len(A)-1):
            counter += 1
            if A[j] < A[min]:
                counter += 1
                min = j
        A[i], A[min] = A[min], A[i]
    return counter


counter = 0
def merge_sort(A):
    global counter
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            counter += 1
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
    return counter


def insertion_sort(A):
    counter = 0
    for j in range(2, len(A)):
        key = A[j]
        i = j - 1
        counter += 1
        while i > 0 and A[i] > key:
            counter += 1
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return counter


def shell_sort(A):
    counter = 0
    h = len(A) // 2
    while h > 0:
        counter += 1
        for i in range(h, len(A)):
            key = A[i]
            j = i
            counter += 1
            while j >= h and A[j - h] > key:
                counter += 1
                A[j] = A[j - h]
                j -= h
            A[j] = key
        h //= 2
    return counter


def comparison(A):
    B = copy.copy(A)
    C = copy.copy(A)
    D = copy.copy(A)
    start = time.time()
    s = selection_sort(A)
    end = time.time()
    print('\tSelection sort:')
    print('\t\tTime:',  end - start)
    print('\t\tNumber of comparisons:', s)

    start = time.time()
    m = merge_sort(B)
    end = time.time()
    print('\tMerge sort:')
    print('\t\tTime:', end - start)
    print('\t\tNumber of comparisons:', m)

    start = time.time()
    i = insertion_sort(C)
    end = time.time()
    print('\tInsertion sort:')
    print('\t\tTime:', end - start)
    print('\t\tNumber of comparisons:', i)

    start = time.time()
    sh = shell_sort(D)
    end = time.time()
    print('\tShell sort:')
    print('\t\tTime:', end - start)
    print('\t\tNumber of comparisons:', sh)


def result(lst):
    for i in range(7, 16):
        print('Array with random numbers, size:2^', i)
        A = (random.sample(range(2 ** 20), 2 ** i))
        comparison(A)
        print('\n')

    for i in range(7, 16):
        print('Array with sorted numbers, size: 2^', i)
        B = sorted(random.sample(range(2 ** 20), 2 ** i))
        comparison(B)
        print('\n')

    for i in range(7, 16):
        print('Array with sorted back numbers, size: 2^', i)
        C = sorted((random.sample(range(2 ** 20), 2 ** i)), reverse=True)
        comparison(C)
        print('\n')

    for i in range(7, 16):
        print('Array with numbers from set {1, 2, 3}, size: 2^', i)
        D = [random.randint(1, 3) for i in range(2 ** i)]
        comparison(D)

result([7, 8, 9, 10, 11, 12, 13, 14, 15])

