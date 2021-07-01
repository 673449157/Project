# #添加元素
# #append的使用
# list01 = [1,2]
# list02 = [3,4]
# list01.append(list02)
# print(list01)
# #extend的使用
# list01 = [1,2]
# list02 = [3,4]
# list01.extend(list02)
# print(list01)
# #insert的使用
# list01 = [0,1,2,3,4]
# list01.insert(3,'i')
# print(list01)
# #修改元素
# A = ['xiaoHu','xiaoMing','uzi']
# for name in A:
#     print(name)
# A[0] = 'wangZhi'
# for name in A:
#     print(name)
# #查找元素
#
# nameList = ['duFu','suShi','liBai']
# findName = input('请输入您要查找的名字：')
# if findName in nameList:
#     print('在')
# else:
#     print('不存在')
#
# #删除元素
# #del
# nameList = ['duFu','suShi','liBai']
# for name in nameList:
#     print(name)
# del nameList[2]
# for name in nameList:
#     print(name)

# #pop
#
# nameList = ['duFu','suShi','liBai']
# print('删除之前')
# for name in nameList:
#     print(name)
# nameList.pop()
# print('删除之后')
# for name in nameList:
#     print(name)
#
# #remove
#
# nameList = ['duFu','suShi','liBai']
# print('删除之前')
# for name in nameList:
#     print(name)
# nameList.remove('duFu')
# print('删除之后')
# for name in nameList:
#     print(name)

#排序
#sort
a = [1,3,5,7,9,2,4,6,8]
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.sort(reverse = True)
print(a)