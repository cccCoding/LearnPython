
# 列表list 类似java里的list
# 正索引0,1,2,3,4 负索引-1,-2,-3,-4,-5
朱建涛的粉丝=["大傻子","二傻子","熊大","光头强","熊二"]
print(type(朱建涛的粉丝),朱建涛的粉丝)
print(朱建涛的粉丝[0])    #第一个
print(朱建涛的粉丝[-1])   #倒数第一个
print(朱建涛的粉丝[-2])   #倒数第二个

print(朱建涛的粉丝*2)     #列表乘法

朱建涛的面条=["牛皮","杏仁儿","高圆圆","大傻子"]
print(朱建涛的粉丝+朱建涛的面条)    #列表相加

朱建涛的粉丝.append("coldplay")   #列表添加
朱建涛的粉丝.append("熊七")
print(朱建涛的粉丝)

#切片,包左不包右
朱建涛的粉丝=朱建涛的粉丝[1:-1]   #切片,去掉第一个和最后一个
print(朱建涛的粉丝)

朱建涛的粉丝=朱建涛的粉丝[1:2]
print(朱建涛的粉丝)

mylist=[1,1,1,2,"zzz"]      #列表可以重复,可以包含不同类型元素
print(mylist)