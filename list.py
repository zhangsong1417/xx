a = [1,2,3,"this is a list"]
b = [4,5,6,"这是第二个列表"]

a.append('思思')
a.insert(0,'华华')
print(a+b)
print(a*2)
print(len(a))
print(a[0])
print(a[1],a[2])
print(a[2:])
print(a[-1])
'''L = [
     ['Apple','Google','Microsoft'],
     ['Java','Python','Ruby','PHP'],
     ['Adam','Bart','Lisa']
    ]

print(L[0][0])
print(L[1][1])
print(L[2][2])

print(L[0][0]+'、'+L[1][1]+'、'+L[2][2])'''

str = "summer"
for j in str:  #遍历我们的字符串，一般用在字符串和列表
    print(j)

c = [1,2,3,4,5,6,7]
c.sort(c)
for i in c:
    print(i)