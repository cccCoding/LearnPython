
#元组不可修改
mytuple=(1,2,3,4,5)
print(mytuple[:3])      #截取
print(mytuple+(8,9,10))     #元组加法
print(mytuple*5)        #元组乘法

for x in mytuple:
    print(x)

print(list(mytuple),mytuple)    #类型转换

