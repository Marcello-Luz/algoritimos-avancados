str(input("Diga seu nome: "))
ing = int(input("Diga sua nota de inglês: "))
port = int(input("Diga sua nota de portguês: "))
mat = int(input("Diga sua nota de matemática: "))
print()
media = (ing * 2 + port * 3 + mat * 5)/10
print(f"A sua média é {media}")
print()
if media >= 7:
    print("Aprovado! Parabéns!")
if media <= 7:
    print("Reprovado!")
