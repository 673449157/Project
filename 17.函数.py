#定义函数
def printInfo():
    print('-' * 20)
    print('人数苦短，我用python')
    print('-' * 20)
#调用函数
print(printInfo())

#函数的说明文档
def sum_2_num(a,b):
    """

    :param a:参数一
    :param b:参数二
    :return:返回result两个数的和
    """
    result = a + b
    return result
sum_2_num(2,3)

print(help(sum_2_num))
