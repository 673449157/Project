#修改元素
info = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
new_id = input('请输入新的学号:')
info['id'] = int(new_id)
print('您的新学号为：%d' % info['id'])
#添加元素
info = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
newAdd = input('请输入您要查询的位置：')
info['newAdd'] = newAdd
print('您的位置为：%s' % info['newAdd'])
#删除元素
#删除指定key
info = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
del info['name']
print(info)
# #删除整个字典
info = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
del info
print(info)
#清空整个字典
info = {'name':'王志','id':1,'xingbie':'男','address':'河北省沧州市'}
info.clear()
print(info)