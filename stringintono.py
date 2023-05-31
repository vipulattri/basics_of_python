a = input('enter a number')
print(a)
print(a.isdecimal)
print(a.isnumeric)
if a.isdecimal():
 num=int(a)
print(num)