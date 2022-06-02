
t = int(input())
lista = []
lista1 = []
c = 0
for i in range(t):
  n1, n2 = map(int, input().split())
  lista.append(n1)
  lista1.append(n2)
while t > 0:
  if t == 1:
    a = lista[c]
    b = lista1[c]
    print(a + b, end="")
  else:
    a = lista[c]
    b = lista1[c]
    print(a+b)
  c = c+1
  t = t-1




