
#元组 tuple
朱建涛的粉丝=("大傻子","二傻子","熊大","光头强","熊二")
朱建涛的面条=["牛皮","杏仁儿","高圆圆","大傻子"]

print(type(朱建涛的粉丝),朱建涛的粉丝)

朱建涛的面条[0]="糖葫芦"
print(朱建涛的面条)       #列表list可以被修改

#朱建涛的粉丝[0]="油条包麻子"
#print(朱建涛的粉丝)      #报错,元组元素不可被修改,相当于被锁住的列表,常量,不可变数组
#不支持append,说明也不可追加

