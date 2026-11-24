#1
# def say_hi():
#     print("Привет!")
# other = say_hi
# other()

#2
# def cube(x):
#     return x ** 3
# first = cube
# second = cube
# print(first(2))
# print(second(3))

#3
# def get_five():
#     return 5
# print(type(get_five))
# print(type(get_five()))

# 4
# def hello():
#     print("дратути")
# def run(action):
#     action()
# run(hello)

# 5
# def double(n):
#     return n * 2
# def apply(action, number):
#     return action(number)
# print(apply(double, 6))

# 6
# def add_ten(n):
#     return n + 10
# def transform(values, action):
#     result = []
#     for v in values:
#         result.append(action(v))
#     return result
# print(transform([1, 2, 3], add_ten))

# 7
# def factory():
#     def worker():
#         print("Работает")
#     return worker
# f = factory()
# f()

# 8
# def make_adder(value):
#     def adder(n):
#         return n + value
#     return adder
# add5 = make_adder(5)
# add7 = make_adder(7)
# print(add5(10))
# print(add7(10))

# 9
# def make_counter():
#     count = [0]
#     def counter():
#         count[0] += 1
#         return count[0]
#     return counter
# c = make_counter()
# print(c())
# print(c())
# print(c())