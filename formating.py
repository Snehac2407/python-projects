'''#for integer
print("this is integer:{}".format(123))
print("this is integer:{:d}".format(123))
print("this is integer:{:5d}".format(123))# here space is there in frot
print("this is integer:{:05d}".format(123))# here  zero will be there in front
#for floats
print("this is integer:{}".format(123.4567))
print("this is integer:{:f}".format(123.4567))
print("this is integer:{:8.3f}".format(123.4567))
print("this is integer:{:08.5f}".format(123.4567))
'''

print("this is integer:{}".format(123))
print("this is integer:{0:b}".format(123))
print("this is integer:{0:o}".format(123))
print("this is integer:{0:x}".format(123))
print("this is integer:{:+d}".format(123))
print("this is integer:{:d}".format(-123))
print("this is integer:{:<05d}".format(123))
print("this is integer:{:>05d}".format(123))
print("this is integer:{:^05d}".format(123))
print("{:*^40}".format("pythons"))



d = {'birthday':15,'name':'iyanu '}
print("{p[name]}'s birthday is on : {p[birthday]}".format(p=d))

l =[10,20,30,40]
l[1] = 555
print(l)