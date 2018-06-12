mylist=[0,1,2,3,4,5]
for x in mylist:    #遍历
    print(x)

mylist.extend(["a","b"])  #在列表末尾一次性追加另一个序列中的多个值
print(mylist)

list2=list(range(5))        #创建0-4列表
mylist.extend(list2)
print(mylist)
print(mylist.index("a"))      #定位元素1的索引

mylist.insert(0,"牛逼")   #0索引处插入元素
print(mylist)

mylist.pop()        #删除最后一个元素
print(mylist)

mylist.remove(1)  #删除第一个找到的为1的元素
print(mylist)

mylist.reverse()    #反转
print(mylist)

list3=[12,46,13,31,46,13,4,846]
list3.sort()   #排序
print(list3)

list3.clear()   #清空
print(list3)

#list深浅拷贝
l1=[1,2,3,4,5]
l2=l1           #浅拷贝,数据是共用的     相当于两个变量指向同一地址
l3=l1.copy()    #深拷贝,数据各自独立     相当于两个变量指向不同地址
l2[3]=100
print(l1,l2,l3)