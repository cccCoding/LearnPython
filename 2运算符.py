#算数运算符
a=10
b=3
print(a/b)  #除法
print(a//b) #整除
print(a%b)  #求余
print(a**b) #求幂 a的b次方

#比较运算符
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)

#赋值运算符
a+=1
print(a)
a-=1
print(a)
a*=2
print(a)
a**=2   #平方
print(a)
a//=2   #整除
print(a)
a/=2    #除法
print(a)
a**=0.5
print(a)
a%=b
print(a)

#逻辑运算符 not and or
c=True
d=False
print(c)
print(not c)
print(not not c)
print(c and d)
print(c or d)

#关系运算符
print("关系运算符-------------------")
朱建涛的粉丝=set(["大傻子","二傻子","熊大","光头强","熊二"])
print("光头强" in 朱建涛的粉丝)      #判断在
print("光头强" not in 朱建涛的粉丝)  #判断不在
print("光头强的光头" in 朱建涛的粉丝)

#身份运算符
print("身份运算符-------------------")
e="大王"
f="大王"
print(e is f)   #判断是否引用同一个对象    #针对字符串变量,为了节省内存,指向同一个
print(e is not f)
print(id(e),id(f))

朱建涛的面条=["牛皮"]
朱建涛的烤面筋=["牛皮"]
print(朱建涛的面条 is 朱建涛的烤面筋)        #针对集合列表数据结构,不是同一个,类似java

#运算符优先级与结合性

