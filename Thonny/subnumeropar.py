T = int(input())

for i in range (T):
    PA, PB, G1, G2 = input().split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)

    ano = 0 
    while PA <= PB:
        PA = PA + PA * (G1 / 100)
        PB = PB + PB * (G2 / 100)
        ano += 1
if ano > 100:
    print("Mais de 1 século.")
else: 
    print(f"{ano} anos.")
