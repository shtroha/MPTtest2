list=["a","b",True]
list.insert(0,"c")
list.extend([8,7,8])
list.remove(8)
# удаляет чисто первый найденный
print(list.index(8))
# также
print(list)

list2=[1,2,3.4,-1]
list2.sort()
print(list2)

list3=[1,2,3.4,-1]
list3.sort(reverse=True)
print(list3)

list4=[0,1,2,[3,4,5]]
print(list4[3][0])

list5=[10,20,30,40,50,60]
print(list5[::2])
# чётные индексы
print(list5[1::2])
# нечётные индексы

list6=[x**2 for x in range(5)]
print(list6)

list7=[0,1,2]
a,b,c=list7
print(a,b,c)

list8=[3,4,5,6,7,8]
d,*e,f=list8
print(d,e,f)
