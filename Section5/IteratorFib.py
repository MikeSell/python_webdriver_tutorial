def fib(size):
   a, b = 0, 1
   count = 0
   while count < size:
      yield b
      a, b = b, a + b
      count += 1

f = fib(15)
print(type(f))
for i in f:
    print(i, end=' ')
print()