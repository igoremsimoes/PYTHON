#Criar uma rotina de entrada que aceite somente um valor positivo.

num = float(input("Insira um número positivo: "))

while (num < 0):
    print("Valor negativo não aceito!")
    num = float(input("Insira um número positivo: "))

print("Este número é positivo!")