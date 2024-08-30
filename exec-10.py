valor_carro = float(input("Diga o valor do carro que voçê deseja em R$: "))
print(f"O valor do carro é R${valor_carro:.0f}?")
resposta = input()
custo = (28/100) * valor_carro + (45/100) * valor_carro + valor_carro
print(f"O custo desse carro é de R${custo:.0f}")
