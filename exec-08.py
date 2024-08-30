eleitores=int(input("Diga o número de habitantes de seu município: "))
print(f"O número de habitantes é {eleitores}")
print("Ok, agora diga o número de votos brancos, nulos e válidos")
votos_brancos=int(input("Votos Brancos: "))
votos_nulos=int(input("Votos Nulos: "))
votos_validos=eleitores-(votos_brancos+votos_nulos)
print(f"Votos Válidos: {votos_validos}")
brancos_porcentagem=(votos_brancos/eleitores)*100
nulos_porcentagem=(votos_nulos/eleitores)*100
validos_porcentagem=(votos_validos/eleitores)*100
input(f"Porcentagem de Votos Brancos: {brancos_porcentagem:.1f}%")
input(f"Porcentagem de Votos Nulos: {nulos_porcentagem:.1f}%")
input(f"Porcentagem de Votos Válidos: {validos_porcentagem:.0f}%")
