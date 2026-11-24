# 1
# def say_hello():
#     print("Привет, мир!")
# say_hello()

# 2
# def greet(name):
#     print(f"Привет, {name}!")
# greet('Анна')
# greet('Олег')

# 3
# def add(a,b):
#     return a+b
# res=add(3,5)
# print(res)

# 4
# def greet(name='Гость'):
#     print(f"Привет, {name}!")
# greet('Прохор')
# greet()

# 5
# def subtract(a, b):
#     print(a-b)
# subtract(5,3)
# subtract(b=5,a=3)

# 6
# def introduce(name,city='Москва'):
#     print(f'Меня зовут {name}, я из города {city}')
# introduce('Анна','Лондон')
# introduce('Анна')

# 7
# def multiply(*num):
#     sum=1
#     for i in num:
#         sum*=i
#     print(sum)
# multiply()
# multiply(2,3,4)

# 8
# def display_info(**num):
#     for key,value in num.items():
#         print(f"{key}-{value}")
# display_info(name='прохор',age=1)

# 9
# def order(name,amount=1,*pos):
#     print(f'Имя-{name}, количество: {amount}, доп позиции: {pos}')
# order('яблоко',8,'доширак','банан')

# 10
# def profile(name,age=18,**dop):
#     res=[name,age]
#     for key,value in dop.items():
#         res.append(f'{key}-{value}')
#     print(res)
# profile('Прохор',10,job='programmer')