import sys
import math
import cmath

print(sys.maxsize)
#print(sys.float_info)

a=100.0/3
print(a,type(a))

b=100.0//3
print(b,type(b))

c=100.%3
print(c,type(c))

d=divmod(100.0,3)
print(d,type(d))

k=5
s=5+1j
print(s,k,s+k,type(s+k))

print(math.sin(5))
print(cmath.sin(s))

var1='Hello World!'
print(var1[4:])
print('var1[0]',var1[0])

name = 'Peter'
my_string = 'Hello %s, how are you? %s' % (name,'Ok')
print(my_string)

rstring = r'Hello /t World!' #funziona!
print(rstring)
print(var1.upper())