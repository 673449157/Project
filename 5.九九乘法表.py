# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d*%d=%d'%(j,i,i*j), end=' ')
        j = j + 1
    print()
    i = i + 1