#prime number 1- 100:

for i in range(1, 100):
    if(i>1):
        for j in range(2, i):
            if(i%j== 0):
                break
        else:
            print(i, end = " ")
output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 

#Write a programme to check wether given number is prime number or not??

num = int(input("Enter the prime number range: "))
if(num>1):
	for i in range(2, num):
		if((num%i)==0):
			print("It is not a prime number: ", num)
			break
	else:
		print("It is prime number) 

#write a programme to print fibnocci series with using for loop: 
n = int(input("enter the number: "))
a = 0
b = 1
for i in range(0, n):
	print(a)
	temp = a + b
	a = b
	b = temp

#write a programme to print fibnocci series with using while loop:
n = int(input("enter the number: "))
a = 0
b = 1	
while(n >= a):
	
	temp = a + b
	a = b
	b = temp
	print(temp)

#Write a programme to print wether the user given is palandrome or not
n = int(input("enter the number: "))
t = n
reversedn = 0
while(n !=0):
	rem = n%10
	reversedn = reversedn *10 + rem
	n//=10
if(t == reversedn):
	print("it is a palandrome number: ", reversedn)
else:
	print("it is not a palandrome number: ", reversedn)
output:
C:\Users\ANIL\Desktop>python exception.py
enter the number: 151
it is a palandrome number:  151

C:\Users\ANIL\Desktop>python exception.py
enter the number: 1001
it is a palandrome number:  1001

C:\Users\ANIL\Desktop>python exception.py
enter the number: 121
it is a palandrome number:  121

#write a programme to print wether the user given string is palandrome or not
n = input("enter the number: ")
if(n == n[::-1]):
	print("it is a palndrome string")
else:
	print("it is not a palndrom string")
output:
C:\Users\ANIL\Desktop>python exception.py
enter the number: raju
it is not a palndrom string

C:\Users\ANIL\Desktop>python exception.py
enter the number: abba
it is a palndrome string

#ARMstrong number:
n = int(input("enter the number: "))
t = n
reversedn = 0
while(t != 0):
	rem = t % 10
	reversedn += rem*rem*rem
	t = t//10
if(n == reversedn ):
	print("it is a ARMstrong number: ", reversedn)
else:
	print("it is not a ARMstrong number: ", reversedn)
Output:
C:\Users\ANIL\Desktop>python exception.py
enter the number: 151
it is not a palandrome number:  127

C:\Users\ANIL\Desktop>python exception.py
enter the number: 153
it is a ARMstrong number:  153

Arm strong number n digits
n = int(input("enter the number: "))
t = n
res = 0
c = 0
rem = 0
while(t != 0):
	rem = t%10
	c = c+1
	print(c)
	t = t//10

t = n
while(t != 0):
	rem = t %10		#3,5
	res = res + pow(rem,c)	#27, 152, 153
	t = t // 10		#15,1,0
if(res == n):
	print("it is a arm strong number")
else:
	print("it is not a arm strong number")

Output:
enter the number: 153
1
2
3
it is a arm strong number

enter the number: 1634
1
2
3
4
it is a arm strong number


#-----------------------------------------------------------------
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
