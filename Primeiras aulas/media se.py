a = int (input("Digite sua primeira nota: "))
b = int (input("Digite sua segunda nota: "))

media = (a+b)/2

if media >= 7:
    print("Sua nota é:", media, "APROVADO")
else:
    print("Sua nota é:", media, "REPROVADO")
    