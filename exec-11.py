carros_vendidos = int(input("Diga o número de carros que você vendeu: "))
valor_vendas = 700 * carros_vendidos
print(f"O valor total de suas vendas foi de R${valor_vendas}")
print()
porcentagem = (5/100) * valor_vendas
salario_fixo = int(input("Diga o valor do seu salário fixo em R$: "))
print()
salario_final = salario_fixo + valor_vendas + (5/100 * valor_vendas)
print(f"O seu salário final será de {salario_final:.0f} reais")
