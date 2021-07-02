#函数嵌套调用
def testB():
    print('---- testB start ----')
    print('这里是testB函数执行的代码')
    print('---- testB end   ----')
def testA():
    print('---- testA start ----')
    testB()
    print('---- testA end   ----')
print(testA())
