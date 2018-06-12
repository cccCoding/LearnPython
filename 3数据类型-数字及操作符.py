length=18       #整数,十进制
length=0b11     #二进制
length=0o17     #八进制
length=0x12     #十六进制
print(length)

tall=1.66       #实数
tall=166e-2     #指数
print(tall)
width=1+2j       #虚数
print(width)

print(int(tall))    #类型转换

del tall        #删除一个变量
#print(tall)     #报错,变量未定义

#常见数学函数
import math
print("常见数学函数-------------------------------")
print(abs(-5))          #求绝对值
print(math.fabs(-5))
print(max(1,2,3,4,5))   #最大值
print(min(1,2,3,4,5))   #最小值

import random
print(random.random())  #得到一个0-1之间的随机数
print(random.randint(0,100))    #0-100间随机int数

print(math.e,math.pi)       #一些数学常量
