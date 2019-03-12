print('hello python,hello world') #你好蟒蛇，世界 我来啦！
print(bool())
print(bool( ))
print(bool(''))
print(bool(' '))
print(bool(0))
print(bool(None)) #所有数据类型都自带布尔值，数据只有在0，None和空的时候为False

if True and False or False:
    print('yes')
else:
    print('no') #运算优先级由高到低：not>and>or，下同
    
if not True and False or False:
    print('yes')
else:
    print('no')