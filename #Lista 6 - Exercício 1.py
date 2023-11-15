inteiros = [0]*10
qntneg = 0
qntpos = 0

for i in range(10):
    inteiros[i] = int(input(f'Informe o {i+1}º número inteiro: '))
    if inteiros[i] < 0:
        qntneg += 1
    elif inteiros[i] > 0:
        qntpos += 1

VETNEG = [0]*qntneg
VETPOS = [0]*qntpos

for i in range(10):
    if inteiros[i] < 0:
        for c in range(qntneg):
            if VETNEG[c] == 0:
                VETNEG[c] = inteiros[i]
                break
    elif inteiros[i] > 0:
        for c in range(qntpos):
            if VETPOS[c] == 0:
                VETPOS[c] = inteiros[i]
                break

print(f'Os números negativos informados são {VETNEG} e os positivos são {VETPOS}.')
