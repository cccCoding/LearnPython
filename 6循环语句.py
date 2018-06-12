#循环语句可精简代码
for i in range(10):
    print(i,end=",")

#死循环
#while True:
#    print("haha")

i=0
while i<20:
    i+=1
    print(i,end=",")
else:
    print("结束了")    #其他情况的处理

mylist=[1,2,3,4,5,6]
for i in mylist:
    print(str(i),end=",")
else:
    print("else",str(i))    #恰好跳出循环的那一次处理

for i in [1,2,3,4,5,6,7,8]:
    if i == 2:
        continue    #本次循环结束,开始下次循环
    if i == 6:
        break       #跳出循环
    print(i, end=",")

print("")

for i in range(50,100,2):
    print(i, end=",")

print("")
print(range(50,100,2))
print(list(range(50,100,2)))

for i in range(10):
    for j in range(10):
        print(i*10+j,end=" ")
    print("")

for i in range(10):
    if i%2==0:
        print(str(i),end="")
    else:
        pass    #占位符,不执行任何操作

