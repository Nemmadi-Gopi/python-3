# class Student:
#     name = ""
#     age = 0
# s1 = Student()
# s1.name = "srirama"
# s1.age = 10

# s2 = Student()
# s2.name = "woo"
# s2.age = 5
# print(f"{s1.name} and {s1.age}")
# print(f"{s2.name} and {s2.age}")

# class stu():
#     a = 5
#     b = 6
#     def add(self):
#         return self.a + self.b
#     def sub(self):
#         return self.b - self.a
# s1 = stu()
# s11 = s1.add()
# print(s11)
# s12 = s1.sub()
# print(s12)

# s2 = stu()
# s21 = stu.add(s2)
# s22 = stu.sub(s2)
# print(s21)
# print(s22)

# class stud():
#     name = ""
#     def __init__(self):
#         self.name = "sri rama"
#     def std(self):
#         print("this is my name : ", self.name)
# s1 = stud()
# s1.std()

# class Stud1():
#     cla_name = "A1"
#     no_of_sub = 6
#     def __init__(self, name, age, subj1, subj2):
#         self.name = name
#         self.age = age
#         self.s1 = subj1
#         self.s2 = subj2
#     def std_details(self):
#         print(f"hello this {self.cla_name} and {self.no_of_sub, self.name, self.age, self.s1, self.s2}")
# s5 = Stud1('Srirama', 12, 90, 60)
# s6 = Stud1('rama', 21, 92, 65)
# s5.std_details()
# s6.std_details()

# class Com:
#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print(self.__maxprice)

#     def setMaxPrice(self, price):
#         self.__maxprice = price
# c = Com()
# c.sell()

# c.__maxprice = 1000
# c.sell()

# c.setMaxPrice(1000)
# c.sell()

class student:
    def __init__(self):
        self.__maxmarks = 90
    def show_marks(self):
        print(self.__maxmarks)
    def setMaxPrice(self, score):
        self.__maxmarks == score
s = student()
s.show_marks()

s.__maxmarks = 95
s.show_marks()

s.setMaxPrice(95)
s.show_marks()

