#if嵌套的使用
bus = int(input('上车请刷卡！'))
#如果余额超过2元可以上车，否则走着去
#如果车上有位置就可以坐下，否则站着
busweizhi = 0#
if bus > 2:
    print('买票上车')
    if busweizhi == 1:
        print('请坐下')
    else:
        print('请上车，位置让位孕妇')
else:
    print('没票了')


