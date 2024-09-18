# for i in range(1, 100):
#     if i>1:
#         for j in range(2, i):
#             if i%j == 0:
#                 break
#         else:
#             print(f"this is prime number: {i}")


# n = int(input("Enter the input : "))
# if n >1:
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"this is not a prime number : {n}")
#             break
#     else:
#         print(f"this is prime number: {n}")


# n = int(input("Enter the input : "))
# a = 0
# b = 1
# for i in range (0, n):
#     temp = a + b
#     a = b
#     b = temp
#     print(f"this is the temp value : {temp}")


# n = int(input("Enter the input : "))
# a = 0
# b = 1
# while (n>= a):
#     temp = a + b
#     a = b
#     b = temp
#     print(f"this is the temp value : {temp}")


# n = int(input("Enter the input : "))
# t = n
# reversedn = 0
# while(n != 0):
#     rem = n%10
#     reversedn = reversedn * 10 + rem
#     n //=10
# if(t == reversedn):
#     print(f"this is palandrome {reversedn}")
# else:
#     print(f"this is not a palandrome: {reversedn}")

# n1 = input("Enter the string : ")
# if n1 == n1[::-1]:
#     print(f"this is palandrome string {n1}")
# else:
#     print(f"this is not a palandrome string {n1}")



# n2 = int(input("Enter the Arm starong input : "))
# t = n2
# reve = 0

# while (t != 0):
#     rem = t % 10
#     reve += rem * rem * rem 
#     t = t//10
# if( n2 == reve):
#     print(f"this is ARM Strong number : {reve}")
# else:
#     print(f"this is not a Armstrong number : {reve}")


d = {'phy':82, 'maths': 68, 'eng':55, 'Science': 48}
min_key = d['phy']
max_val = ''
for key, val in d.items():
    if val < min_key:
        min_key = val
        max_val = key
print(max_val)