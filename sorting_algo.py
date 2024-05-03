#  wap for sorting algorithm :-
# def Selection_Sort(array):
#     length=len(array)
#     for i in range(0, length - 1):
#         smallest = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[smallest]:
#                 smallest = j
#         array[i], array[smallest] = array[smallest], array[i]
# array = input('Enter the list of numbers: ').split(',')
# array = [int(x) for x in array]
# Selection_Sort(array)
# print('List after sorting is : ', end='')
# print(array)

# wap for bubble sorting:-
# def bubble_sort(array):
#     for i in range(len(array)-1,0,-1):
#         for j in range(i):
#             if array[j]<array[j+1]:
#                 temp=array[j]
#                 array[j]=array[j+1]
#                 array[j+1]=temp
# array = input('Enter the list of numbers: ').split(',')
# array = [int(x) for x in array]
# bubble_sort(array)
# print('List after sorting is : ', end='')
# print(array)

# wap for merge sort:-
# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         sub_array1 = arr[:mid]
#         sub_array2 = arr[mid:]
#         mergeSort(sub_array1)
#         mergeSort(sub_array2)
#         i = j = k = 0
#         while i < len(sub_array1) and j < len(sub_array2):
#             if sub_array1[i] < sub_array2[j]:
#                 arr[k] = sub_array1[i]
#                 i += 1
#             else:
#                 arr[k] = sub_array2[j]
#                 j += 1
#             k += 1
#         while i < len(sub_array1):
#             arr[k] = sub_array1[i]
#             i += 1
#             k += 1
#         while j < len(sub_array2):
#             arr[k] = sub_array2[j]
#             j += 1
#             k += 1
# num = int(input("how many eelemnt do you need in your list"))
# arr=[int(input()) for x in range(num)]
# mergeSort(arr)
# print(arr)

# wap forqick sort:-
def quick_sort(A,low,high):
    if low < high:
        pivot = partition(A,low,high)
        quick_sort(A,low,pivot-1)
        quick_sort(A,pivot+1,high)
def partition(A,low,high):#low = 0,high= len(A)-1
    pivot  = low
    swap(A,pivot,high)
    for i in range(low,high):
        if A[i] <= A[high]:
            print(A)
            swap(A,i,low)
            low = low+1
    swap(A,low,high)
    return low
def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
A = [100,399,245,89,678,565,200]
print(A)
quick_sort(A,0,len(A)-1)
print("afte applying qick sort\n",A)