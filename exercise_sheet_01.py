# 1.Aufgabe

print("Hallo Tutron!")

# 2.Aufgabe

A = 3
B = 0.1
C = A * B
D = C == 0.3
print(D)
E = round(C, 1)
F = E == 0.3
print(F)
G = 9 / 5
print(type(G))
H = 9 // 5
print(type(H))
K = int(G)
print(type(K))
L = 9 % 5
print(L)

# 3.Aufgabe
M = type(A)
print(M)
N = B is int
print(N)
P = A is B
print(P)
P = id(A) == id(B)
print(P)

# 4.Aufgabe

Q = "Python sagt \"Hallo!\""
print(Q)
R = "Wie geht's?"
print(R)
S = Q[:-2] + ", " + R.lower() + "\""
print(S)

# 5.Aufgabe
T = "Eine Zeile \nUnd noch eine Zeile"
U = "Eigentlich erzeugt \\n einen Zeilenumbruch."
print(T)
print(U)

# 6.Aufgabe

# 5 - int('3e2'), invalid literal for int() with base 10: '3e2'
# ohne Hochkomma würde es funktionieren: 5 - (int(3e2))
# 'Hallo' - 'Ha',  unsupported operand type(s) for -: 'str' and 'str'
# 'Hallo'[2:] würde ich machen
# 3 + float('1,1'),  could not convert string to float: '1,1'
# Wir müssen float nicht durch ein Komma,
# sondern durch einen Punkt trennen: 3 + float('1.1')
