def decor_division(func):
    def inner(a,b):
        try:
            if b==0:
                print("respected sir/madam plz go for maths tutions")
            else:
                return func(a,b)
        except ZeroDivisionError:
            print('')
    return inner
@decor_division
def division(a,b):
    return a/b
print(division(123,45))
print(division(23,5))
print(division(12,5))
print(division(123,0))
