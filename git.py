# from statistics import median
# n= [1,1,2,2,3,3,4,5,5,6,100,112]
# # mode(n)
# print(median(n))
#
# from collections import defaultdict
# def get_counts2(sequence):
#  counts = defaultdict(int) # values will initialize to 0
#  for x in sequence:
#       counts[x] += 1
#  return counts

# limit values greater than 15, memorizing of lost values.
lst = [11,18,9,12,23,4,17]
lost = []
for idx in range(len(lst)):
 val = lst[idx]
 if val > 15:
     lost.append(val)
 lst[idx] = 15
print("modif:",lst,"-lost:",lost)
