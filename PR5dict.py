# # 1
# d1={'Иванов':3,'Сидоров':4,'Крылов':5}
# print(d1['Крылов'])

# # 2
# d2={1:25,2:42,3:67}
# d2[4]=7
# d2[1]=52
# d2.pop(2)
# print(d2)

# # 3
# d3={1:'banana',2:'apple',3:'mango'}
# n=1
# if n in d3:
#     print('Есть')
# else:
#     print('Нет такого ключа')

# # 4
# d4={1:'kk',2:'tt',3:'zz'}
# print(d4.keys())
# print(d4.values())
# print(d4.items())

# # 5
# d5={'липтон':70,'доширак':30,'чипсы':55}
# for i in d5:
#     print(i,d5[i])

# # 6
# d6={'липтон':70,'доширак':30,'чипсы':55}
# s=0
# m=[]
# for i in d6:
#     s+=d6[i]
#     m.append(d6[i])
# print(s,max(m))

# # 7
# s7='eabcddeee'
# d7={}
# for i in s7:
#     d7.update({i:s7.count(i)})
# print(d7)

# 8
s8='ab ef ef cd ab ef'.split()
d8={}
for i in s8:
    d8.update({i:s8.count(i)})
d8=sorted(d8.items(),key=lambda x:x[1],reverse=True)
print(d8[0][0])


# # 9
# d9={1:49,2:57}
# d9c={}
# for a,b in d9.items():
#     d9c[b]=a
# print(d9c)

# # 10
# s1=['Russia','USA','UK']
# s2=['Moscow','Washington','London']
# d10={}
# for i in range(len(s1)):
#     d10.update({s1[i]:s2[i]})
# print(d10)