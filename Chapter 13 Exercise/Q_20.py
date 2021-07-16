"""Write a function called merge that takes two already sorted lists of possibly different lengths,
and merges them into a single sorted list.
(a) Do this using the sort method.
(b) Do this without using the sort method."""


def merge_withsort(l1,l2):
    result = l1 + l2
    print((sorted(result)))
    
    
merge_withsort([1,3,4,6],[2,4,5,6,7])


def merge_withoutsort(l1,l2):
    l3 =l1+l2

    for i in range(len(l3)):
        for j in range(1+i,len(l3)):
            if l3[i] > l3[j]:
                l3[i], l3[j] = l3[j], l3[i]

    print(l3)

merge_withoutsort([2,5,4,6,1],[7,6,5,4,3,0])


    