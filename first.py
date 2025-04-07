# print("Hello, World!")
# MYNAME=input()
# myaddrees=input()
# myage=input()
# print("My name is",MYNAME)
# print("My address is",myaddrees)
# print("My age is",myage)
# a=10
# b=20
# if b%a ==0:
#  print(a+b)
# else:
#  print("ntg")
# print("syed","saad","syed",sep="-",end="!")

# s="Saad Syed"
# print(s)
# print(s[-3])
# print(s[1])
# print(type(s))


# b=["saad","syed",2,3,4,33,'s']

# print(b)
# print(b[-3])
# print(b[-10])

# t1=(2,3,4,5)
# t2=()
# t2=tuple(1)

# boolean
# print(type(True))
# print(type(true))

# SET
# a=set("helloworldprogram")
# b=set(["hello","worldprogram","hello"])

# a.add("newadd")
# b.add("newadd")
# print (a)
# print(b)
# frozen set

# c=frozenset("helloworldprogram")
# d=frozenset(["hello","worldprogram","hello"])

# print (c)
# print(d)
# c.add("newadd")
# d.add("newadd")


# slicing
# a="           _______revaTuRe is located in chennai______________________       "
# print(a)
# print(a[1:4].upper())
# print(a.title())
# print(a.capitalize())
# print(a.swapcase())
# print(a.isalpha())
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
# print(a.lstrip("_"))# Removes leading underscores
# print(a.strip(" _"))# Removes leading & trailing underscores


# dictionary
# a={"name":"saad","age":23,"salary":"1L"}
# print(a)
# print(a["age"])


# BINARY
# a=[65,66,67]
# print(a)

# c=bytes([65,66,67])
# print(c)

# Nonetype
# x=None
# print(type(y))
# print(type(x))
# y
# print(y)
# print(type(y))


# a=int(input())
# if(a>=90):
#  print("A")
# elif(a>=70 and a<90):
#  print("B")
# elif(a>=60 and a<70):
#  print("c")
# else:
#  print("fail")

# reverse a string
# s="daad"
# rs=""
# for i in range(len(s)):
#     rs=s[i]+rs

# print(rs)
# if(rs==s):
#     print("palindrome")
# else:
#     print("not a palindrome")

# eo=int(input())
# if eo%2 ==0:
#    print("even")
# else:
#    print("odd")


# import math
# e=int(input())
# b=False
# if e<2:
#  b=True
# else:
#  for i in range(2,int(math.sqrt(e))+1):
#     if(e%i==0):
#         b=True
#         break
# if(b):
#      print("not prime")
    
# else:
#    print("prime")


# fibonacci series
# a,b=0,1
# print(a)
# print(b)
# c=0
# for i in range (1,10):
#     c=a+b
#     print(c)
#     a=b
#     b=c

# def fun(**details):
#     for key,val in details.items():
#         print(key+"-"+str(val))
# fun(name="saad",age=23,passout="2024")
# import array
# fruit =array.array('i',[1,2,3,4])
# print(len(fruit))
# print(fruit[2])
# for f in fruit:
#     print(f)


# inbuit sorted
# import array
# a=array.array('i',[1,10,-3,4])
# b=sorted(a)
# print(a)
# print(b)

# list methods
# list =["apple","mango","banana","mango","papaya","aaa"]
# list.append("pineapple")
# list.insert(0,"watermelon")
# print(list)

# list.remove("papaya")
# list.pop()
# print(list)

# list.sort()
# print(list)
# list.reverse()
# print(list)

# list2=list.copy()
# print(list2)
# list2.clear()
# print(list2)

# print(list)
# print(list.index("mango"))
# print(list.count("mango"))

# lamba

# sqr=lambda x: "positive" if(x>0) else "Negative" if (x<0) else "zero" 
# print(sqr(10))
# print(sqr(0))
# print(sqr(-1))

# list =[lambda arg= i :arg * 10 for i in range(1,5) ]
# for i in list:
#     print(i())

# a=[1,2,3,4]
# b=map(lambda x:x*2,a)
# print(list(b))

# a=[1,2,3,4]
# b=filter(lambda x:x%2==0,a)
# print(list(b))

# from functools import reduce
# a=[1,2,3,4]
# b=reduce(lambda x,y:x+y,a) #x=1+y=2------x=3+y=3----------x=6+4
# print(b)
# REPLACE MAP WITH FILTER REDUCE SEE OUTPUT


# print("My name is {0} and iam from {1} age is {2}".format("saad","kurnool",23))

# name="saad"
# place="kurnool"
# age=23
# #An f-string is a concise and readable way to embed expressions inside string literals using {}.
# print(f"My name is {name} and iam from {place} age is {age}")


#inner functions
# def fun1(revature):
#     def fun2():
#         print(revature)
#     fun2()

# revature="revature"
# fun1(revature)
# def decorator(func) :
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper

# @decorator
# def greet():
#     print("greet")

# greet()

# import inspect
# inspect.signature(decorator)
# inspect.signature(greet)

# inner classes
# class Dog:
#     sound="bark"
#     def __init__(self,name,sal):
#         self.name=name
#         self.sal=sal
#     def __str__(self):
#         return f"name{self.name},salary{self.sal}"

# dog=Dog
# dog2=Dog("dog2","1000000")
# print(dog.sound)
# print(dog2.name)
# print(dog2.sal)
# print(dog2)
# dog2.name="dog3"
# print(dog2.name)

# class Outer:
#     def __init__(self):
#         print("outerinit")
#     def show():
#         print("outer show")
#     class inner:
#         def __init__():
#             print("inner init")
#         def display():
#             print("inner display ")
# o=Outer()
# o.__init__()

# class Par:
#     def show():
#         print("saad")
# class Child(Par):
#     super.show();

# c=Child()
# c.show()
# class Private:
#     def __init__(self):
#         self._salary=30000
#     def sal(self):
#         return self._salary
    
# ob=Private()
# print(ob.sal)


# a=[1,2,3,4,5]
# i=iter(a)
# print(next(i))
# print(next(i))
    


# def fun ():
#     x=3
#     print(x)

# fun()

# Enclosing scope
# def fun():
#     x=300
#     def infun():
#         print(x)
#     infun()
    
# fun()


# global scope
# x=300
# def fun():   
#     def infun():
#         print(x)
#     infun()
# fun()
# print(x)
    
