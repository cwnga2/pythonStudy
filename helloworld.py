from __future__ import print_function

print('hello')
x = '90'
if x == '80' :
    print('test > 80')
else:
    print('aaa')

for i in range(1, 10):
    for j in range(1, 10):
        print(i*j,end = " ")
    print(end = "\n")

#list
print('==== list ====')
list = [1,2,3,4,5]
print(list)

for i in range(0, len(list)):
    print(list[i])

#dict
print('==== dict ====')
dict = {0:'zero', 1:'one'}
print(dict)

for i in dict:
    print(dict[i])

