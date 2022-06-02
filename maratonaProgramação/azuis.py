
def mfi(entrada):
    for mfi in ['AUGUUCAUA', 'AUGUUCAUC', 'AUGUUCAUU', 'AUGUUUAUA', 'AUGUUUAUC', 'AUGUUUAUU']:
        if mfi in entrada:
            return True
    return False
for repeticao in range(int(input())):
    if mfi(input()): print('S')
    else: print('N') 


