#列表嵌套
#一个学校3个办公室，现在有8位老师，随机分配8位老师到3个办公室
#定义一个列表用来保存3个办公室

import random

offices = [[],[],[]]

#定义一个列表用来存储8个老师的名字

names = ['欧艳楠','黄华','大斌','猛男','无敌','公子','少爷','带头大哥']

i = 0
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为：%d'%(i,len(tempNames)))
    i += 1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)












#嵌套练习

# list = [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9],
#         [12,12,13]
#        ]
# jieguo = 0
# for num in list:
#     for num01 in num:
#         jieguo += num01
# print(jieguo)