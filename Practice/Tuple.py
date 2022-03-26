#Tuple: ordered, immutable and allows duplicate elements

#List vs Tuple which one better
import sys
import timeit
mylist = [1,2,"hello", True]
myTuple = (1,3,"hello", True)
print(sys.getsizeof(mylist), "bytes") #88 byte
print(sys.getsizeof(myTuple), "bytes") #72 byte
#so tuple require less memory spaces

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=10000000)) #0.7277..
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=10000000)) #o.0806..
# So Tuple is faster than list

# for list [] and tuple () | tuple immutable but list is mutable
notTuple = ("Max")
myTuple = ("Max",)
print(type(notTuple))
print(type(myTuple))

myTuple = tuple(["Max", 9])
print(type(myTuple))

#count function can be used for both
mylist = ["new", "q", "q", "q"]
print(mylist.count('new'))
myTuple = ("Max", "q", "q", "q")
print(myTuple.count('q'))
print(myTuple.index('q'))

#convert tuple to list and vise versa
myList = list(myTuple)
myTuple = tuple(myList)

#slicing typle
# : for range :: for jump/step

a = (1,2,4,5,6,7,8,9,10,11,12)
b = a[1:6]
c = a[2::2]
print(b)
print(c)
