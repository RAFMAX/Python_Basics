for I in range(1,21):
    print(I)

T = []
for I in range(1,1000001) :
    T.append(I)

V = [I for I in range(1,10001)]
for i in range(0,10000):
    print(V[i])
print(min(V))
print(max(V))
print(sum(V))

L = [j for j in range(3,31,3)]
print(len(L))
for j in range(0,10):
    print(L[j])

L = []
for A in range(1,11):
    print(A**3)
    L.append(A**3)

print(L[-2:])
if 1 in L :
    print("Exists") 
if 1 == L[0] :
    print("Equals")