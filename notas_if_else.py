nota1 = int(input("informe a nota do 1º bimestre (0-100): "))
nota2 = int(input(" informe a nota do 2º bimestre (0-100)"))
media = (nota1 + nota2) / 2
if media >= 60:
    print(f" Você foi aprovado com média {media}")
else:
    print(f" Você não foi aprovado, sua média é {media}") 