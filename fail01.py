##01 F
import copy


def func(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    print(args)
    print(*args)


func(1, 2, 3, 4, 5, 6, 7)


##02 F
class A:
    x = 1


class B(A):
    pass


class C(A):
    pass


B.x = 2
A.x = 5
print(A.x, B.x, C.x)

##03 F
a = list("123456")
b = a[0], a[-1], a[2:3]
print("{0},{1},{2}".format(*b))


##04
def func():
    yield (x for x in range(3))


for x in func():
    print(tuple(x))

##05

import re

paran = "back"
item = 0
if re.match(paran, "back"):
    item += 1
## False
if re.match(paran, "out.back"):
    item += 2
if re.search(paran, "backup"):
    item += 4
if re.search(paran, "out.back"):
    item += 8

print(item)


##06
class test1:
    pass


class test2(test1):
    pass


print(type(test2()) == "tes1")
print(type(test2()))
print(isinstance(test2(), test1) == True)
print(isinstance(test1(), test1) == True)

## 07
numbers = [1, 2, 3]
print(list(filter(lambda x: 2, numbers)))
print(list(filter(lambda x: (x + 1) * 3 / 3 % 3 == 0, numbers)))
print(list(filter(lambda x: x > 1, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))

## 08
a = [1,2,[2,2]]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(1)
print(a)
print(b)
print(c)
print(d)
##09 单例
##元类，基类 new 模块

## 10
