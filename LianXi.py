#-*- coding:utf-8 -*-
#1.存储10个值，存入列表
a = [4,2,5,7,3,9,1,10,6,8]
a.sort()
sum = 0
print a[0]+a[1]+a[2]
print a[3]+a[4]+a[5]
print a[6]+a[7]+a[8]
a.append(11)
print a


#下标1-3的值之和与最后一个值的差是多少
for i in a:
    if 0<i<4:
        sum+=a[i]
print '下标1-3的值之和:',sum
he = sum - a[-1]
print '与最后一个值的差是多少:',he


#求列表中的最大值
print max(a)



# for i in a:
#     if i<3:
#         sum += a[i]
#         print sum
#     if 3<=i<6:
#         sum += a[i]
#         print sum
#     if 7<=i<10:
#         sum += a[i]
#         print sum



#2.使用列表存储如下名字
b = ['zhangshan','lisi','wangwu','zhaoliu','zhangshan,','qianqi','wangba','zhangshan']
#(1)使用函数求张三的个数
print b.count('zhangshan')

#(2)求钱七所在的下标
print b.index('qianqi')

#(3)求下标3至下标7之间是否有王八
if(b.index('wangba',3,7)):
    print True
else:
    print False

#(4)按链表结构删除下标5的元素
del b[5]
print b

#(5)按链表结构删除最后一个元素
del b[-1]
print b

#(6) 输入五位同学的成绩,先按升序排列,然后按降序排列
score = [29,78,32,80,60]
score.sort()
print score

score.reverse()
print score

#(7)将成绩列表转换成元祖
a = tuple(score)
print a

#(8)将元祖转换成列表
b = list(a)
print b

#(9)新增一个成绩，判断是否有和当前成绩相同的成绩 ?
t= 90
b.append(t)
print t in b

# flag = True
# lie = []
# while True:
#     score = raw_input("请输入五位同学的成绩:")
#     if int(score) < 6:
#         flag = True
#         lie = [score]
#     else:
#         flag = False
#         break
# lie.sort()
# print lie


#3.完成两个列表的相关操作
list1 = ['life','is','short']
list2 = ['you','need','python']
#(1)输出python及其下标
print list1,list2
for i in range(len(list1)),range(len(list2)):
    print i,

print
#(2)在list2后追加 '!' , 在 'short' 后添加 ','
list2.extend('!')
print list2

list1.insert(3,',')
print list1

#(3)将两个字符串合并后，排序并输出其长度
he = list1+list2
print len(he)

# (4)'python' 改为 'python3'
list2[2] = 'python3'
print list2

#(5)移除之前添加的 '!' 和 ','
list2.remove('!')
print list2

list1.remove(',')
print list1

