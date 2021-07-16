#无参数，无返回值
#此类函数，不能接收参数，也没有返回值，一般情况下，打印提示灯类似的功能，使用这类的函数
def printMeun():
    print('-'* 50)
    print('海底捞点餐系统')
    print('')
    print('1.毛肚')
    print('2.虾滑')
    print('3.牛肉')
    print('-'* 50)
print(printMeun())

#无参数，有返回值
#此类函数，不能接收参数，有返回值，一般情况下，像采集数据，用此类函数

#获取温度
def getTemperature():
    #这里是获取温度的一个过程
    #为了简单，先模拟返回一个数据
    return 24
temperature = getTemperature()
print('当前温度：%d' % temperature)

#有参数，无返回值
#此类函数，能接收参数，无返回值，一般情况下，对某些变量设置数据而不需要结果时，用此类函数，一般很少使用，需求不多

#有参数，有返回值的函数
#此类函数，不仅能接收参数，还可以返回某个数据，一般情况下，像数据处理并需要结果的应用，用此类函数

#计算1-num的累积和
def calculateNum(num):
    result = 0
    i = 1
    while i <= num:
        result += i
        i += 1
    return result
result = calculateNum(100)
print('1-100的累积和为：%d'% result)


