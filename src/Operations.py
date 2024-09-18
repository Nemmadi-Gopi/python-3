print("jai srirama")

# print('Good Morning!')
# print('It is rainy today')

# #print() with end Parameter
# print('Good Morning!', end = " ")
# print('It is rainy today')

# #print() with sep parameter
# print('New Year', 2023, 'See you soon!', sep= '. ')
# print("hello " + "world,"" this is python world")

# x = 1
# y = 2
# print("this is the output of x {} and y{}".format(x, y))


# print("{0} and {1}".format('Geeks', 'forgeeks'))
# print("{1} and {0}".format('Geeks', 'forgeeks'))

# for i in range(1, 10, 2):
#     if i == 5:
#         print(f"this is the output of the for loop: {i}")
#         break
#     else:
#         print(f"this is the output of the for loop in else condition: {i}")
# print("iam going out of this loop function in python")

#print a number whether it is prime number or not

n = int(input("please enter the input number: "))
if n>1:
    for i in range(2, n):
        print(i)
        if n%i == 0:
            print("It is not a prime number : ", n)
            break
    else:
        print("It is a prime number : ", n)

#print prime numbers in range
for i in range(1, 100):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print("It is a prime number : ", i)