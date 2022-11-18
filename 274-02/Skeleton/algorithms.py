"""Implementations of some sorting"""
import random


def merge(a0, a1, a):
    i0 = i1 = 0
    for i in range(len(a)):
        if i0 == len(a0):
            a[i] = a1[i1]
            i1 = i1 + 1
        elif i1 == len(a1):
            a[i] = a0[i0]
            i0 = i0 + 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 = i0 + 1
        else:
            a[i] = a1[i1]
            i1 = i1 + 1


def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    a0 = merge_sort(a[0:m])
    a1 = merge_sort(a[m:len(a)])
    merge(a0, a1, a)
    return a


def _quick_sort(a, i, n):
    if n <= 1:
        return
    x = a[i + random.randrange(0, n - 1)]
    p, j, q = i - 1, i, i + n
    while j < q:
        if a[j] < x:
            p = p + 1
            a[j], a[p] = a[p], a[j]
            j = j + 1
        elif a[j] > x:
            q = q - 1
            a[j], a[q] = a[q], a[j]
        else:
            j = j + 1
    _quick_sort(a, i, p - i + 1)
    _quick_sort(a, i, n - (q - i))


def quick_sort(a):
    _quick_sort(a, 0, len(a))
    return a


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
