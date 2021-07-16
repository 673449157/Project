#函数应用：打印图形和数学计算

#打印一条横线
#打印自定义行数的横线

def printOneLine():
    print('-' * 50)
def printNumLine(num):
    i = 1
    while i < num:
        printOneLine()
        i += 1
printNumLine(3)
print(printOneLine())

#求三个数的和
#求三个数的平均值

# 求3个数的和
def sum3Num(a,b,c):
    return a+b+c

# 求3个数的平均值
def average3Num(a,b,c):
    sum3NumResult = sum3Num(a,b,c)
    average3NumResult = sum3NumResult / 3
    return average3NumResult
result = average3Num(11,232,35)
print('平均值是：%d'% result)