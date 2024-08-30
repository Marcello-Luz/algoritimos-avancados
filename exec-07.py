ano=int(input("Em que ano você nasceu? "))
mes=int(input("Qual o mês de seu nascimento? "))
dia=int(input("Qual o dia do seu nascimento? "))
nascimento=input("Você nasceu em {}/{}/{}".format(dia,mes,ano))
dia_atual=str(input("Qual a data de hoje? "))

dias_passados=dia_atual-dia
