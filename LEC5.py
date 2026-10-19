# t=(1,3,True)
# print(t)

# data=[1,2,3,4]
# print(tuple(data))

# t=(1,2,3)
# print(t[0])

# name,age,company,pos=('phil',34,"LCB","CEO")
# print(name,age,company,pos)

# s=('phil',34,"LCB","CEO")
# print(s[0:3])

# мн-во (set) - набор уникальный неупорядоченных элементов
# set1=() - пустой словарь
# set2=set()
# print(set2)

# set1={1,1,2,3,4,4}  словарь
# print(set1)

# set1={1,}
# print(set1)

# data=[1,2,3,3,True]
# print(set(data))

# fruits=set()
# fruits.add("apple")
# print(fruits)
# fruits.remove("apple")
# print(fruits)
# fruits.discard("apple")
# print(fruits)

# fruits=[1,2,3,4]
# print(fruits.clear())

# spisok={'eto','to'}
# res=spisok.copy()

# spisok={'eto','to'}
# res={'to samoe','to'}
# res2=spisok.union(res)
# print(res2)
# print(spisok | res)
#
# res3=spisok.intersection(res)
# print(res3)
# print(spisok & res)
#
# # разность мн-в
# print(res - res3)
#
# # симметрическая разность
# print(res.symmetric_difference(spisok))
# print(res^spisok)

# us1={'maga','bragin'}
# us2={'maga','shtroha','bragin'}
# # подмножество
# print(us1.issubset(us2))
# # надмножество - ничтожество
# print(us2.issuperset(us1))