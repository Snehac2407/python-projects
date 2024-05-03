# write a program to find the number of  occurences of each character
#s =  "ABCDABBCDABBBCCCCDDDEEEE"
#d = {}
#for x in s:
   # if x in d.keys():
        #d[x] = d[x] + 1
   # else:
        #d[x] = 1
#print(d)
#for k,v in d.items():
   #print("{}={} Times ".format(k,v))

str = "youuknowwwhatiknowhowtocode"
a = {}
for i in str:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
print(str,(a))

