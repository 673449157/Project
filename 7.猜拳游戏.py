# 1剪刀 2石头 3布
import random

player = int(input('请输入：'))

# 电脑产生一个随机数

computer = random.randint(1, 3)

if ((player == 1) and (computer == 3)) or ((player == 2) and (computer == 1)) or ((player == 3) and (computer == 2)):
    print('获胜，你真屌啊')
elif player == computer:
    print('平局，再来！')
else:
    print('失败，不要走，决战到天亮')

