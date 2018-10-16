#-*- coding:utf-8 -*-
#-------列表篇----------[]
#1.序列的列表的长度可变,而数组不能
#存在负索引,从-1开始,从右往左依次递减

a = 'jin wan chi ji'
print a[0:5]
a = "今晚吃鸡" #一个中文字占据3个字节
print a[0:18]
# name = input()[0]
# print name


#切片:对一定范围内的元素进行访问 索引1<=索引2
#切片返回一个新的序列
a = [1,True,3,'hello','little boy',4,6,7,8]
print a[4:7]
print a[-5:-1]
print a[2:]
print a[0:-1:-8]


#序列相加 不同类型的序列不能相加
#序列相乘(用途) ：重复序列操作 None的初始化操作 空列表


#字符串是一个特殊的序列 可以进行成员检测


#len()获取变量的长度
#max() min() 获取变量中的最大最小值
print len(a)


#2.列表的更新
#修改的格式: 变量[索引] = 更新值
a = [1,3,4,5]
a [0] = 10
print a


#添加元素 append()
#append()方法对序列本身进行操作,没有返回值
print('=================')
a.append('Gold')
print a


#将元素插入到指定位置 insert(下标,更新值)
a.insert(1,'$')
print a


#删除元素  remove(obj)
a.remove('$')
print a


#根据下标删除元素   del(下标)
del a[0]


#list()方法:
b = list('hello') #将字符串转换成一个字符列表
print b


#count()统计一个元素在列表中出现的次数,返回值为整数
c = [1,3.4,1,'e','m',2,['2',7,1]]
print c.count(1) #统计1在列表中出现的次数
print c[len(c)-1] #获取c的最后一个yuans


d = ['bbc','cba','acb','def','fed']
d.reverse() #反转元素序列
print d


c.sort() #默认自然序列排序
print d


c.sort(reverse=True) #先排序,再反转 达到升序的效果
print d


c.pop(1) #先排序进栈,再出栈
print c


r = [5,6,7]
#extend()方法对序列本身进行操作,没有返回值
c.extend(r) #在原来的列表进行追加
print c


# #-----------元祖篇--------------()
# #声明元祖 元祖内容不能被修改,只能够连接组合
# a = 1,2,3
# print  a
#
# b = (1,2,3)
# print b
# print b[0]
# c = [(4,5,6)]
# print tuple(c)
# d = tuple("xiaoming") #将字符串转换成元祖
# print d[0:4] #元祖的元素访问和列表一致
#
# f = ["xiao","ming"]
# d = (1,2,3,f)
# print d
# print id(f)
# print id(d)
# f[0] = "Big"
# print id(f)
# print id(d[3])
#
# #同类型:int>float>complex
# #不同类型 比较大小:字典>列表>字符串>元祖
# a = ('abc',45,789,'hjk','jk',56)
# print len(a)
# print max(a)
# print min(a)
#
# a = [11,22,(33,44),55,66]
# a[2][1] = 0
# print a





