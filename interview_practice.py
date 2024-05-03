# =======ARRAY'S===========
# How to range update the array using cumulative sumlist=[10,20,30,40,50]   
# list=[10,20,30,40,50]
# new_list=[] 
# j=0
# for i in range(0,len(list)):
#     j+=list[i]
#     new_list.append(j) 
     
# print(new_list)

# find the identical element in the given array :-
# def identical_element(element):
#     twin={}
#     for name in element:
#         if name in twin :
#             twin[name]+=1
#         else:
#             twin[name]=1
#     identical=[]
#     for name,count in twin.items():
#         if count>1:
#             identical.append(name)
#     return identical 
# element=[1,2,2,1,4,3,4,5,4,6,5]
# identical=identical_element(element)
# print(identical)

# wap to count even number of digit c
# def count_even_digits(nums):
#     count = 0
#     for num in nums:
#         if len(str(num)) % 2 == 0:
#             count += 1
#     return count

# # Example usage:
# numbers = [12, 3453, 67, 890, 1234]
# result = count_even_digits(numbers)
# print("Number of integers with even number of digits:", result)

# wap for insertion 
# def insertion_Sort(array):
#     for i in range(1,len(array)):
#         value=array[i]#here value at 1st index will be 
#         j=i-1#zero th inex value 
#         while j>=0 and value<array[j]:
#             array[j+1]=array[j]
#             j-=1
#         array[j+1]=value
#     return array
# array=[23,345,54,23,1,656,788,4566,34]
# result=insertion_Sort(array)
# print(result)

# merege two sorted array without using any extra space:-
# arr_1=[23,43,45,65,67,87,]
# arr_2=[34,54,60,63,89]
# def merge(n,m):
#     i=0
#     j=0
#     k=n-1
#     while(i<=k and j<m):
#         if (arr_1[i] < arr_2[j]):
#             i+=1
#         else:
#             temp=arr_2[j]
#             arr_2[j]=arr_1[k]
#             arr_1[k]=temp
#             j+=1
#             k-+1
#         arr_1.sort()
#         arr_2.sort()
# merge(len(arr_1),len(arr_2))
# print(','.join(str(x) for x in arr_1),end ="")
# print(','.join(str(x) for x in arr_2))

# wap for impementing a quick sort algorithm :-
# def quick_sort(array):
#     if len(array)<=1:
#         return array
#     else:
#         pivot =array[0]
#         left_hand=[x for x in array[1:] if x <= pivot]
#         right_hand=[x for x in array[1:] if x > pivot]
#         return quick_sort(left_hand)+[pivot]+quick_sort(right_hand)
# array=[12,32,32,1,2,3,45,65,41]
# sorted_array=quick_sort(array)
# print(sorted_array)

# wap for square of sorted array:-
# class solution:
#     def make_sq(self,array):
#         n=len(array)
#         highest_index=n-1
#         left=0
#         right=n-1
#         while left<=right:
#             left_square=array[left]*array[left]
#             right_square=array[right]*array[right]
#         if left_square>right_square:
#             square[highest_index]=left_square
#             left+=1
#         if right_square>right_square:
#             square[highest_index]=right_square
#             right-=1 
#             highest_index-=1
#         return square
# result=solution()
# print("sorted square",str(result.make_sq([-2,-4,0,4,3])))

# wap for checking  arithmetic progression:-
# def AP(array):
#     array.sort()
#     d=array[1]-array[0]
#     for i in range(len(array)):
#         if (array[i]-array[i-1] !=d):
#             return False
#     return True
# array=[2,5,7,9,11,13]
# ap=AP(array)
# print(ap)
#

# wapfor finding the second largest element in array without sorting:-
# def second_largest(array):
#     largest=0
#     second_largest=-1
#     for i in range(len(array)):
#         if array[i]>largest:
#             largest=array[i]
#     for i in range(len(array)):
#         if array[i]>second_largest and array[i] != largest:
#             second_largest=array[i]
#     return second_largest
# print(second_largest([20,30,40,24,12,4]))