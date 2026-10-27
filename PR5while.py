import random
# # 1
# i=1
# while i<11:
#     print(i)
#     i+=1


# # 2
# n=int(input())
# sum=n
# while n!=0:
#     n=int(input())
#     sum+=n
# print(sum)

# # 3
# n=1234
# c=0
# while n!=0:
#     c+=1
#     n//=10
# print(c)

# # 4
# n=1234
# c=0
# while n!=0:
#     c+=n%10
#     n//=10
# print(c)

# # 5
# n=1234
# res=''
# while n!=0:
#     res+=str(n%10)
#     n//=10
# print(int(res))

# # 6
# n=17
# c=2
# while c<n:
#     print(c)
#     c**=2

# # 7
# n=input("Введите пароль: ")
# while n!="1234":
#     n=n=input("Введите пароль: ")
# print('Правильно')

# # 8
# a=12
# b=8
# while b!=0:
#     a,b=b,a%b
# print(a)

# # 9
# n=17
# a,b=0,1
# if a<=n:
#     print(a)
# while b<=n:
#     print(b)
#     a,b=b,a+b

# # 10
# n=random.randint(1,100)
# ans=int(input('введите число: '))
# c=1
# while ans!=n:
#     if ans<n:
#         print('больше')
#     else:
#         print('меньше')
#     ans=int(input('введите число: '))
#     c+=1
# print(f'правильно\nколичество попыток: {c}')