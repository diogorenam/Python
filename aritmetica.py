x = int(input())
s1 = input()
y = int(input())
s2 = input()
z = int(input())

ops = {
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y,
  '*': lambda x, y: x * y,
  '/': lambda x, y: x // y
}

try:
  res = None
  if s1 == '*' or s1 == '/':
    #x s1 y s2 z
    #4 * 8 - 4
    #ops[s1](x, y) #32
    res = ops[s2](ops[s1](x, y), z)
  else:
    #x s1 y s2 z
    # 4 + 8 / 4
    res = ops[s1](x, ops[s2](y, z))
    #ops[s1](x, 2)
  print(res, end="")
except:
  print ("erro", end="")