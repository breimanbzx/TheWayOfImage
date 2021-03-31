import json

# 列表
list_a = [1, 2, 3, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4]

list_a.insert(2, '10')

del list_a[1]  # 等于a.pop(1)
list_a.pop(-1)  # 默认删除最后一个元素
while 4 in list_a:
    list_a.remove(4)  # 删除所有4

print(list_a)

# 字典
dict_a = {1: 2, 3: 4}
# 同时遍历键值
for k, v in dict_a.items():
    print(k, v)

del dict_a[1]
print(dict_a)


# 函数
def test(a, b, *args, **kwargs):
    c = a+b
    for i in args:
        print(i)
    for kk, vv in kwargs.items():
        print(kk, vv)
    return c


test(1, 2, 5, 6, 8, 5, 8, 4, qq=20, rr=30)

# 万能文件打开方式：只读r  写入w  附加a  读写r+
with open('txt.txt','w') as file:
    file.write('Talib matplotlib grids aux axhline')

with open('txt.txt','a') as file1:
    file1.write('123456789')

#
with open('124.json') as file:
    num = json.load(file)












