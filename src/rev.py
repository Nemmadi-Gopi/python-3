# print("jai srirama")

# # s = lambda x, y: x + y
# # print(s(5,6))

# # ma = map(lambda s: str(s).upper(), "abc")
# # print(list(ma))

# # m1 = map(lambda i: i**i, [1,2,3,4,5,6,7])
# # print(list(m1))

# # c = filter(lambda l: l%2, [1,2,3,4,5,6,7,8,9])
# # print(list(c))

# # c1 = filter(None, [1,2,3,4,5,6,7,8,9])
# # print(list(c1))

# # l1 = [1,2,3,4,5]
# # l2 = l1
# # print(id(l1))
# # print(id(l2))
# # l2[1] = 1000
# # print(l2, l1)

# # l11 = [1,2,3,4,5]
# # l22 = l11.copy()
# # l22[1] = 1000
# # print(l22, l11)

# # l111 = [[1,2,3,4,5,6],[7,8,9,10,11,12]]
# # l222 = l111.copy()
# # l222[1][1] = 1000
# # print(l222, l111)

# # import copy
# # l1 = [[1,2,3,4,5,6],[7,8,9,10,11,12]]
# # l2 = copy.deepcopy(l1)
# # l2[1][1]= 1000
# # print(l2, l1)

# # def generator_a():
# #     yield "a"
# # g = generator_a()
# # for i in g:
# #     print(i)

# # a = [4,5,6]
# # def myfun(b):
# #     for x in b:
# #         print("before yield")
# #         yield x
# #         print("after yield")
# # c = myfun(a)
# # print("Generator function: ", c)
# # print(next(c))
# # print()
# # print(next(c))
# # print()
# # print(next(c))
# # print()
# # print(next(c))
# # print()

# # f = open(r'C:\Users\nemma\Desktop\demo.py', 'w')
# # f.write("hello")
# # f.close()

# # def main_welcome():
# #     msg = "hello Everyone"
# #     def sub_welcome():
# #         print("welcome to python")
# #         print(msg)
# #     return sub_welcome()
# # m = main_welcome()


# # def main_welcome(func):
# #     def sub_welcome():
# #         print("welcome to python")
# #         func()
# #         print("please read the python")
# #     return sub_welcome()
# # @main_welcome
# # def second_welcome():
# #     print("this is from the second function")
# # main_welcome(second_welcome)

# # def main_welcome(func):
    
# #     def Sub_welcome():
# #         print("welcome to python")
# #         func()
# #         print("please read the python")
# #     return Sub_welcome
# # @main_welcome
# # def second_welcome():
# #     print("This is from second function")
# # second_welcome()


# # def make_pretty(func):

# #     def inner():
# #         print("I got decorated")
# #         func()
# #     return inner

# # @make_pretty
# # def ordinary():
# #     print("I am ordinary")

# # ordinary()

# # def main_welcome(func):

# #     def sub_welcome():
# #         print("welcome to python")
# #         func()
# #         print("Please read the python")

# #     return sub_welcome
# # @main_welcome
# # def second_welcome():
# #     print("this is from the second function")

# # second_welcome()

# # import itertools
# # print("jai srirama")


# # def power(x, n=2):
# #     return x**n
# # print(power(5))

# # x = [1,2,3,4,5]
# # y = [i**2 for i in x if i%2 == 0]
# # print(y)

# # x = [1,2,3]
# # result = itertools.combinations(x,2)
# # print(list(result))

# # def func(x):
# #     try:
# #         return int(x)
# #     except:
# #         return None
# # x = ["1", "2", "a", "4"]
# # result = list(map(func, x))
# # print(result)

# # class ABC():
# # 	def capital(self):
# # 		print("iam a first method in ABC class")
# # 	def language(self):
# # 		print("iam a second method in ABC class")
# # 	def type(self):
# # 		print("iam a third method in ABC class")
# # class DEF(ABC):
# # 	def capital(self):
# # 		print("iam a first method in DEF class")
# # 	def language(self):
# # 		print("iam a second method in ABC class")
# # 	def type(self):
# # 		print("iam a third method in ABC class")
# # a = ABC()
# # d = DEF()
# # d.capital()
# # class Deck():
# # 	def talk(self):
# # 		print("Quack... Quack")
# # class Dog():
# # 	def talk(self):
# # 		print("Bow... Bow")
# # class cat():
# # 	def talk(self):
# # 		print("Meow.. Meow")
# # class Goat():
# # 	def talk(self):
# # 		print("Myaah.. Myaah")
# # def f1(obj):
# #     obj.talk()
# # l = [Deck(), Dog(), cat(), Goat()]
# # for i in l:
# #     f1(i)

# def main_welcome(func):
#     def sub_welcome():
#         print("this is hello1")
#         func()
#         print("thanks3")
#     return sub_welcome
# @main_welcome
# def second_welcome():
#     print("hello2")
# second_welcome()

# class student():
#     def __init__(self, name):
#         self.name = name
#     def std(self):
#         print(self.name)
# s = student("HI")
# s.std()



def min_absolute_difference(arr):
    # Sort the array
    arr.sort()
    
    min_diff = float('inf')
    min_pairs = []

    # Iterate through the sorted array and find the minimum absolute difference
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff < min_diff:
            min_diff = diff
            min_pairs = [(arr[i], arr[i + 1])]
        elif diff == min_diff:
            min_pairs.append((arr[i], arr[i + 1]))

    # Sort the pairs based on the first element and then the second element
    min_pairs.sort(key=lambda x: (x[0], x[1]))

    return min_diff, min_pairs

# Example usage
arr = [4,2,1,3]
min_diff, min_pairs = min_absolute_difference(arr)

# Output the result in the required format
for pair in min_pairs:
    print(pair[0], pair[1], end=", ")
