#迭代器
mylist=[1,2,3,4,5,6,7]
myiter=iter(mylist)
print(next(myiter)) #挨个迭代元素
print("")
for it in myiter:       #迭代器里应该是有一个指针的概念
    print(it)

print("----------------")
mylist2=[1,2,3,4,5,6,7]
myiter2=iter(mylist2)
while True:
    try:
        print(next(myiter2))
    except:
        break

print("--------生成器--------")
def go():
    print("11")
    yield 1
    print("12")
    yield 2
    print("13")
    yield 3

print(type(go)) #函数类型   <class 'function'>
T=go()
print(type(T))  #生成器类型   <class 'generator'>
print("return=",next(T))
print("return=",next(T))
print("return=",next(T))
