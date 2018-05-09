#pozicije u nizu

niz = [1,2,1,2,1,4,1,5]
broj = 1
pozicije =[]

for i in range(len(niz)):

    if niz[i] == broj:
        pozicije.append(i)

print(pozicije)