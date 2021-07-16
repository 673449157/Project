#1.多个return
def create_nums():
    print('---1---')
    return 1 #函数中下面的代码不会被执行，因为return除了能将数据返回之外，还有一个隐藏的功能:结束函数
    print('---2---')
    return 2
    print('---3---')

#不同场景下执行不同的return
def create_nums(num):
    print('---1---')
    if num == 100:
        print('---2---')
        return num+1
    else:
        print('---3---')
        return num+2
        print('---4---')
result1 = create_nums(100)
print(result1)
result2 = create_nums(200)
print(result2)

#2.一个函数返回多个数据的方式
def calc_2_num(a,b):
    sum01 = a + b
    sub01 = a - b
    mult01 = a * b
    divide01 = a / b
    return sum01,sub01,mult01,divide01
result = calc_2_num(100,20)
print(result)
