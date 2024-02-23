# programa para verificar si un numero es par o impar

# input
X = int(input("digite un numero: "))

# prosesing
R = (X % 2)

if R == 0:
    RTA = "Par"
else:
    RTA = "Impar"

# auput
print("el numero",X,"es",RTA)