import copy
org = [[1,2,3],[4,5,6]]
sha_org = copy.copy(org)
sha_org[0][0] = 9
print(org)
print(sha_org)

import copy
org1 = [[1,2,3],[4,5,6]]
deep_org = copy.deepcopy(org1)
deep_org[0][0] = 9
print(org1)
print(deep_org)

l = lambda x, y: x+y
print(l(5,6))


m = map(lambda x: x**2, [1,2,3,4,5,6])
print(list(m))

f = filter((lambda l: l%2), [1,2,3,4,5,6,7])
print(list(f))


def my_gen(n):
    value = 0
    while value < n:
        yield value
        value += 1
for value in my_gen(3):
    print(value)

generator = my_gen(3)
print(next(generator))
print(next(generator))
print(next(generator))
#print(next(generator))

def main_welcome(msg):
    def sub_welcome():
        print("welcome to python")
        print(msg)
        print("end to the python world!")
    return sub_welcome()
m = main_welcome("Hello python guys..!")


print("-------------This is the decorator function-------------")

def Main_welcome(func):

    def Sub_welcome():
        print("welcome to python")
        func()
        print("end to the python world !")
    return Sub_welcome
@Main_welcome
def dec_func():
    print("this is the decorator function to implementation !")

dec_func()
