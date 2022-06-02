x, y = input().split(" ")
if int(x) == 0 and int(y) == 0:
    print('NO ALVO!', end="")
elif int(x) < 0 and int(y) < 0:
    print('R3', end="")
elif int(x) > 0 and int(y) > 0:
    print('R1', end="")
elif int(x) > 0 and int(y) < 0:
    print('R4', end="")
elif int(x) < 0 and int(y) > 0:
    print('R2', end="")
else:
    print(end="")