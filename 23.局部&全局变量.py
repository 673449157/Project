#局部变量

def test1():
    a = 100
    print('test1修改前a=%d'% a)
    a = 200
    print('test1修改后a=%d'% a)
def test2():
    a = 300
    print('test3a=%d'% a)
test1()
test2()

#全局变量

a = 100
def test1():
    print(a)
def test2():
    print(a)
test1()
test2()

#全局变量和局部变量名字相同问题

# 定义全局变量
a = 100
def test1():
    a = 100
    print('test1修改前a=%d' % a)
    a = 200
    print('test1修改后a=%d' % a)
def test2():
    print('test3a=%d'% a)
test1()
test2()

#修改全局变量
#定义全局变量
a = 100
def test1():
    global a
    print('test1修改前a=%d' % a)
    a = 200
    print('test1修改后a=%d' % a)
def test2():
    print('test3a=%d' % a)
test1()
test2()