
print(r"徐淑欢今年\n%d岁,身高%f" % (17, 1.58))      #前面加个r,字符串格式化,\n当做字符串
print("朱建涛今年\n%d岁,身高%f" % (19,1.61))        #不加r,\n当做换行符

#常用方法
str="aaa你1"
print(str.capitalize())     #首字母大写
print(str.center(20,"*"))  #返回一个指定的宽度width居中的字符串,fillchar为填充的字符,默认为空格
print(str.count("h"))       #h出现的次数
print(str.encode("utf-8"))  #编码为二进制b开头
print(str.encode("utf-8").decode("utf-8"))  #二进制转为字符串
print(str.endswith("zi"))   #判断是否以某个字符串结尾
print(str.find("你"))      #查找字符串位置,找到返回索引,找不到返回-1
print(str.rfind("你"))       #从右查找,返回索引或-1
print(str.isalnum())        #字符串至少一个字符并且所有字符都是字母或数字 汉字也算字母
print(str.isalpha())        #字符串至少一个字符并且所有字符都是字母或汉字
print(str.isdecimal())      #十进制数字
print(str.isnumeric())      #是否数字

mystr="  hello,Python  "
print(mystr.join("h"))  #将序列中元素以指定的字符连接生产一个新的字符串???
print(mystr.upper())    #大写
print(mystr.lower())    #小写
print(mystr.lstrip())    #去掉左边空格
print(mystr.rstrip())    #去掉右边空格
print(mystr.strip())     #去掉前后空格
print(max(mystr.strip()))       #取最大字符
print(min(mystr.strip()))       #取最小字符
print(mystr.replace("hello", "shabi"))  #替换字符
print(mystr.split(","))     #用逗号分隔字符串得到字符串列表
