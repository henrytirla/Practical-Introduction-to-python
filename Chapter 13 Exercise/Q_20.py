"""Write a function called merge that takes two already sorted lists of possibly different lengths,
and merges them into a single sorted list.
(a) Do this using the sort method.
(b) Do this without using the sort method."""


def merge_withsort(l1,l2):
    result = l1 + l2
    print((sorted(result)))
    
    
merge_withsort([1,3,4,6],[2,4,5,6,7])


def merge_withoutsort():
    pass


    