def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
def sort(array):
    array = input('Enter the list of numbers: ').split(',')
    array = [int(x) for x in array]
    sort(array)
    print('List after sorting is : ', end='')
    print(array)