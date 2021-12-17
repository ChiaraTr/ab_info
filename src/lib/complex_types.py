import time

m=['Lista','di',4,'elementi']
print(m[0],m[3])
print(m)

L=['spam','Spam','SPAM!']
print(L[2])
print(L[-1])
print(L[2:])

print('------------------------------------')

a=list(range(10))
print(a)
b=list(range(1,10,2))
print(b)
c=[el*2 for el in a]
print(c)

l1=[1,2]
l2=['a','b']
l3=[4,5]
f=[(e1,e2,e3) for e1 in l1 for e2 in l2 for e3 in l3]
print(f)

print('------------------------------------')

l=list(range(1000000))
v=list(range(1000000))
t1=time.perf_counter()
s=l+v
t2=time.perf_counter()
print('Execution time:',t2-t1,'s')

t3=time.perf_counter()
l.extend(v)
t4=time.perf_counter()
print('Extended execution time:',t4-t3,'s')

print('------------------------------------')

stack=[1,2,3,4]
print('Initial stack:', stack)
for i in list(range(5,7)):
  stack.append(i)
print('Append:',stack)
stack.pop()
print('Pop:',stack)

queue=['a','b','c','d']
print('Initial queue:',queue)
queue.append('e')
queue.append('f')
print('Append:',queue)
queue.pop(0)
print('Pop:',queue)

print('------------------------------------')

my_dict={'name':'Jack','age':26}
print(my_dict['name'])
print(my_dict.get('age'))
my_dict['age']=27
print(my_dict)
my_dict['adress']='Downtown'
print(my_dict)

squares={1:1,2:4,3:9,4:16,5:25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)
del squares[1]
print(squares)
squares.clear()
print(squares)
del squares
#print(squares) #dà errore

marks ={}.fromkeys(['Maths','English','Science'],0)
print(marks)
for item in marks.items():
  print(item)
print(list(sorted(marks.keys())))

