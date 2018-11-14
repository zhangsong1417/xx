'''def printName(name):
    print(name+"棒棒哒，萌萌哒！")

printName("华华")'''

def sum(a,b):
    s = 0
    for i in range(a, b+1):
        s += i
    print(str(a)+"到"+str(b)+"的和是", s)

sum(1, 100)