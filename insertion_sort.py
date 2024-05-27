import random

def insertion_sort(arr):
    for i in range (1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr [j - 1]
            j -= 1
 
arr = [random.randint(1, 100) for _ in range(10)]
print ("pradinis atsitiktinai sugeneruotas masyvas:", arr)

insertion_sort(arr)
print ("isrusiuotas masyvas:",arr)
