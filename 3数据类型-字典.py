#dict
#key不能重复,value可重复
#后面有相同的key,value更新到后面的value
mydict={110:"朱建涛",220:"朱建涛",110:"可爱多",330:"朱建涛"}
print(mydict)
print(mydict.keys(),mydict.values())
print(mydict[110])
mydict[110]="甜筒"    #存在就更新
mydict[440]="白痴"    #不存在就添加
print(mydict)
del mydict[110]         #删除元素
print(mydict)

mydict["ak47"]="一号"
mydict[1.33]="二号"
mydict[("你好",45.6)]="三号"    #可添加不同数据类型的key
#mydict[[12,12]]="四号"        #不能是列表
print(mydict)
print(str(mydict))  #转成字符串打印
print(mydict.get(550))  #存在返回value,不存在返回None
print(440 in mydict)    #判断是否存在该key
print(mydict.items())   #显示key,value元组的列表

mydict.setdefault(11111)    #key没有就添加,value为默认值None
print(mydict)

print("-------------迭代key--------------")
for a in mydict:
    print(a)
print("-------------迭代key--------------")
for a in mydict.keys():
    print(a)
print("-------------迭代value--------------")
for a in mydict.values():
    print(a)

#mydict.clear()      #清空
print("-------------一些方法--------------")
mytuple=(1,2,3,4,5)
myxyzdice=dict.fromkeys(mytuple)    #新造一个字典,value为None
print(myxyzdice)

mydict.update(myxyzdice)    #两个字典叠加
print(mydict)


