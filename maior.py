linha = input()
partes = linha.split()
n1 = int(partes[0])
n2 = int(partes[1])
n3 = int(partes[2])
maior = n1

if (n2 > maior):
        maior = n2
if (n3 > maior):
        maior = n3

print(maior, end="")