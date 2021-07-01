#字符串遍历
a_str = 'hello world'
for b in a_str:
    print(b,end = '')

#列表遍历
a_list = [1,2,3,4,5]
for b in a_list:
    print(b,end = '')
#元祖遍历
a_turple = (1,2,3,4,5)
for b in a_turple:
    print(b,end = '')
#字典遍历

a_dict = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
for b in a_dict:
    print(b,end = '')

#遍历字典key
a_dict = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
for b in  a_dict.keys():
    print(b)

#遍历字典value
a_dict = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
for b in a_dict.values():
    print(b)

#遍历字典的元素
a_dict = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
for b in a_dict.items():
    print(b)

#遍历字典的key-value（键值）
a_dict = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
for key,value in a_dict.items():
    print('%s-%s' % (key,value))

#带下标索引的遍历
list = ['a','b','c','d','e']
i = 0
for a in list:
    print('%d %s' % (i,a))
    i += 1

#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
list = ['a','b','c','d','e']
for i,a in enumerate(list):
    print('%d %s' % (i,a))