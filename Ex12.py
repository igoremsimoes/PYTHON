#Entrar com dois valores quaisquer. Exibir o maior deles, se existir, caso contrário, enviar mensagem avisando que os números são idênticos.

v1 = float(input("Digite o primeiro numero: "))
v2 = float(input("Digite o segundo numero: "))

if v1 > v2:
    print(v1, "É maior que", v2)
elif v1 == v2:
    print("Os números são idênticos")
else: 
    print(v2, "É maior que", v1)