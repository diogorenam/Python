t=int(input())
Sum=[]
for i in range(t):
  lista = map(int,input().split(";"))
  Sum.append(sum(lista)) 
for i in range(t):
  if(i == t-1):
    print(Sum[i],end="") 
  else:
    print(Sum[i])