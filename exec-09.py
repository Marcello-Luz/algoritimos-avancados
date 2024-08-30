str(input("Seu Nome: "))
salario=int(input("Salário Atual: "))
reajuste=int(input("Diga o percentual de reajuste: "))
print(f"O percentual de ajuste é de {reajuste}%")
novo_salario=((reajuste/100)*salario)+salario
print(f"O novo salário é de R${novo_salario:.0f}")
