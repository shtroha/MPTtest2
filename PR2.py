a,b=int(input("Введите первое число: ")),int(input("Введите второе число: "))
print("ЛЕГЕНДА:\n+ Сложение\n- Вычитание\n* Умножение\n/ Деление\n// Целочисленное деление\n% Остаток от деления\n** Возведение в степень\n== Равно!= Не равно\n> Больше\n< Меньше\n>= Больше или равно\n<= Меньше или равно\nand Логическое И\nor Логическое ИЛИ\nnot Логическое НЕ\nin Принадлежность\nnot in Не принадлежность\nis Тождественно\nis not Не тождественно")
c=str(input("Введите действие: "))
if c=="+":
    print (f"{a} + {b} = {a+b}")
elif c=="-":
    print(f"{a} - {b} = {a-b}")
elif c=="*":
    print(f"{a} * {b} = {a*b}")
elif c=="/":
    print(f"{a} / {b} = {a/b}")
elif c=="//":
    print(f"{a} // {b} = {a//b}")
elif c=="%":
    print(f"{a} % {b} = {a%b}")
elif c=="**":
    print(f"{a} ** {b} = {a**b}")
elif c=="==":
    print(f"{a} == {b} = {a==b}")
elif c=="!=":
    print(f"{a} != {b} = {a!=b}")
elif c==">":
    print(f"{a} > {b} = {a>b}")
elif c=="<":
    print(f"{a} < {b} = {a<b}")
elif c==">=":
    print(f"{a} >= {b} = {a>=b}")
elif c=="<=":
    print(f"{a} <= {b} = {a<=b}")
elif c=="and":
    print(f"{a} and {b} = {a and b}")
elif c=="or":
    print(f"{a} or {b} = {a or b}")
elif c=="not":
    print(f"Not {a}, not {b} = {not a, not b}")
elif c=="in":
    a=str(a)
    b=str(b)
    print(f"{a} in {b} = {a in b}")
elif c=="not in":
    a=str(a)
    b=str(b)
    print(f"{a} not in {b} = {not(a in b)}")
elif c=="is":
    print(f"{a} is {b} = {a==b}")
elif c=="is not":
    print(f"{a} is not {b} = {a!=b}")
else:
    print("Введена неправильная операция")