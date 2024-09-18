#Creating variable : to store the particular value in the memory
# a = 10
# b = 10.5
# print(a)
# print(type(a))
# print(type(str(a)))
# print(dir(a))

#Datatypes in python
# 1. Numeric Data Types in Python
    # 1. Integers
    # 2. Float
    # 3. Complex Numbers
 #Note: type() function is used to determine the type of Python data type. 
#Example:
#a = 5 # it is the integer
# print(type(a))

# b = 10.2  # it is the representing to floating point number like 10.5
# print(type(b))

# c = 2+3j  #A complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j
# print(type(c))

# 2. Sequence Data Types in Python
'''It is the is the ordered collection of similar or different Python data types.
    Sequences allow storing of multiple values in an organized and efficient fashion. There are several sequence data types of Python.'''
#   2.1 Python List

#       Lists are just like arrays, declared in other languages which is an ordered collection of data

#   2.2 Python Tuple

#       Just like a list, a tuple is also an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable i.e. tuples cannot be modified after it is created. It is represented by a tuple class.

#   2.3 Python String
#       Strings in Python are arrays of bytes representing Unicode characters.
#       A string is a collection of one or more characters put in a single quote, double-quote, or triple-quote.'''

#   2.1 List Functions():
#   Note: The dir() function returns all properties and methods of the specified object, without the values
#l = [1,2,3,4,5,6,7,8,9,10]
# print(l)
# print(type(l))
# print(dir(l))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# l.append(11)
# print(l)

# l2 = [1,2,3,4,5]
# l2.clear()
# print(l2)

# l3 = l.copy()
# print(l3)

# print(l.count(1))
# l2 = []

# l2.extend(l3)
# print(l2)
# print(l.index(10))
# print(l[::2])
# print(l[0:5])
# print(l[0:10:-1])
# print(l[10::-1])


# l4 = [1,2,3,4,5,6]
# l4.pop()
# print(l4)

# l4.remove(4)
# print(l4)
# l4.reverse()
# print(l4)
# l4.sort()
# print(l4)

#   2.2 Tuple Functions():
#t = (1,2,3,4,5,6,7)
# print(t)
# print(type(t))
# print(dir(t))
# 'count', 'index'
# t.count(1)
# print(t.index(7))
# print(t[::2])
# print(t[0:5])
# print(t[0:10:-1])
# print(t[10::-1])

#   2.3 String Functions():
s = "hello"
# print(s)
# print(type(s))
# print(dir(s))
# print(s.capitalize())
# print(s.casefold())
# print(s.center(10, '$'))
# print(s.count('l'))
# print(s.encode())
# print(s.endswith('lo'))
# print(s.startswith('he'))
# s1 = 'abc\t12345\tabc'
# print(s1.expandtabs())
# print(s.find('l'))
# print(s.rfind('l'))
# print('Hello {0}, you are very {1}'.format('python', 'famous'))
# print('hello {name}, your my {fav}'.format(name = "python", fav = "faviourate"))
# p = {'x': 5, 'y':7}
# print('{x} and {y}'.format_map(p))
# print('{x} and {y} and {z}'.format_map(p)) # Z is not defined in python

# s1 = "hello world"
# print(s1.index('h'))
# print(s1[::])
# print(s1[:5])
# print(s1[0::2])

# s2 = "hello1234"
# print(s2.isalnum())
# print(s.isalpha())

# s4 = 'hello1234$'
# print(s4.isascii())

# s3 = '123456'
# print(s1.isdecimal())
# print(s1.isdigit())
# print(s.isidentifier())

# print(s.islower())

# print(s3.isnumeric())
# print(s3.isprintable())

# s5 = " "
# print(s4.isspace())

# s6 = "Hello World!"
# print(s6.istitle())
# print(s6.isupper())

# s7 = ['I', "Love","India"]
# print(''.join(s7))
# print('@'.join(s7))

# s8 = "python"
# print(s8.ljust(12, '@'))
# print(s8.rjust(12, '@'))

# s9 = "    python    "
# #print(s9.strip())
# print(s9.lstrip())
# print(s9.rstrip())
# print(s9.strip())

# s10 = "@@@@@python@@@@@"
# print(s10.lstrip('@'))
# print(s10.rstrip('@'))
# print(s9.strip('@'))

# print(s.lower())

# dict = {'a': "123", "b":"456", "c":"789"}
# string = "abc"
# print(string.maketrans(dict))

# str = "python is fun"
# print(str.partition("ython"))
# print(str.rpartition("is "))

# t = "bat ball"
# res = t.replace('b','c')
# print(res)

# t = 'a,b,a,c,d,e,e,f,g'
# res = t.replace(',' ,'')
# print(res)
# str = "THIS SHOULD ALL BE lowercase"
# print(str.swapcase())
# str = "this should be a lowercase"
# print(str.title())

# a = ("john","charles", "mike")
# b = ("jenny", "christy","monica")
# x = zip(a, b)
# print(tuple(x))

# import sys
# a = [10,12.15,'python','averages', 100]
# b = (10,12.15,'python','averages', 100)
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))


# s = {1,1,2,3,4,5,6,8,7,9,7,4,10,11,22,15,16,14,14,15,16,1,61,25}
# s.add(66)
# print(s)  

# s1 = {1,1,2,3,4,5,6,8,7,9,7,4,10,11,22,15,16,14,14,15,16,1,61,25}
# s1.clear()
# print(s1)

# s2 = s.copy()
# print(s2)

# s2.update([65,76,86])
# print(s2)
# s3n = s2.pop()
# print(s3n)

# s3 = {1,1,1,22,2,2,2,3}
# s3.remove(1)
# print(s3)

# print(dir(s3))



# ss = s1.difference(s)
# print(s)
# print(s1)

# ss1 = s.difference_update(s1)
# print(s)
# print(f"this is the result of first difference : {s1}")

# print("hello")
# ss2 = s1.difference_update(s)
# print(s)
# print(f"this is the result of {s1}")
# print("end")


# ss3 = {10,11,12}
# ss3.discard(12)
# print(ss3)

# s = {1,2,3,4,5,6,6,5,4,3,2,5,6,6,6,11, 12}
# s1 = {1,2,3,4,5,6,6,5,4,3,2,5,6,6,6, 10, 13}
# print(s)
# print(s1)

# f = s.intersection(s1)
# f1 = s1.intersection(s)
# print(f)
# print(f1)

# dis = s.isdisjoint(s1)
# print(dis)

# s = {1,2,3,4}
# s1 = {1,2,3,4,5,6}
# print(s.issubset(s1))
# print(s.issuperset(s1))

print("jai srirama")


# d = {'name': "vissu", 'age': 18, "education": 'B-Tech'}
# print()
# print(d)


# d1 = {'name': "vissu", 'age': 18, "education": 'B-Tech'}
# d1.clear()
# print()
# print(d1)


# d2 = d.copy()
# print()
# print(d2)

# x = ('key1', 'key2', 'key3')
# y = 0
# th = dict.fromkeys(x, y)
# print(th)

# th1 = dict.fromkeys(x)
# print(th1)

# th2 = d2.get("name")
# print(th2)

# th3 = d2.get("qualification")
# print(th3)

# th4 = d2.items()
# print(th4)

# d = {'a': 1, 'b':2}
# e = {'c': 3, 'd': 4}

# c = d.update(e)
# print(d)
# print(d.items())
# print(d.keys())
# print(d.values())

# print(d.pop('a'))
# print(d.popitem())


# d5 = {'name': "vissu", 'age': 18, "education": 'B-Tech'}
# print(d5)

# d5.update({'name': "viswanth"})
# print(d5)

# required or mandatory arguments
# def addition(arg1, arg2):
#     a = arg1 + arg2
#     b = arg1 - arg2
#     return a, b

# aa = addition(5, 7)
# print(aa)


# #default arguments

# def addition_default(arg1 = 5, arg2 = 10):
#     ar = arg1 + arg2
#     return ar
# print(addition_default())

# #SyntaxError: non-default argument follows default argument
# # def addition_default1(arg = 35, arg2):
# #     ar = arg+ arg2
# #     return ar
# # print(addition_default1(10))

# def addition_default1(arg2, arg = 35):
#     ar = arg+ arg2
#     return ar
# print(addition_default1(10))
# print("this is the output from the function of addition_degault1")

# def substraction(arg1 = 10, arg2 = 20):
#     ar = arg1 - arg2
#     return ar
# print(substraction(arg2 = 25, arg1=5))

# #variable length keyword arguments
# def sumation(*c):
#     s = sum(c)
#     return s
# print(sumation(1,2,3,4,5,6,7,8,9,7,8,5,4,8,8))

# print("this is the output of the variable length keyword arguments ")

# def summation1(x, y = 2, *c, **d):
#     print(x)
#     print(y)
#     print(sum(c))
#     print(d)

# summation1(10, 20,  1,2,3,4,5,6,7,8,9,7,8,5,4,8,8, e = 15,f = 20,g = 25)

# def f1():
#     print("f1() This is the funcation1 output")
# f1()

# def f2():
#     print("f2() This is the funcation2 output")

# f2()


# def f1():
#     print("f1() This is the funcation1 output")


# def f2():
#     f1()
#     print("f2() This is the funcation2 output")

# f2()

# def f1(a):
#     def f2(b):
#         print("this is inside the nested function")
#         return b+ 5
        
#     return f2

# f = f1(5)
# print(f)
# ff = f(6)
# print(ff)


def summation(x, y, *c):
    print(x)
    print(y)
    print(sum(c))
    def summation_inner(b = 5):
        return b + 5
    return summation_inner
s = summation(5, 20, 3,4,5,6,7,8)
print(s)
s1 = s()
print(s1)


def summation(x, y, *c):
    print(x)
    print(y)
    print(c)
    print(x+y+sum(c))

    def summation_inner(b = 5):
        return b + 5
    return summation_inner
s = summation(5, 20, 3,4,5,6,7,8)
print(s)
s1 = s()
print(s1)


