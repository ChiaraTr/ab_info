n = 23
running = True

while running:
  guess = int(input('Enter an integer:'))
  if guess == n:
    print('You guessed!')
    break
  elif guess < n:
    print('Higher that that!')
  else:
    print('Lower than that!')

for i in range(n):
  if i <= n/2:
    print(' ',i/2)
else: 
  print('  Stop')
 
a=iter(list(range(10)))
for i in a:
  print(next(a))

b='Ciao'
for el in b: print('  ', el)
