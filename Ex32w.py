#Entrar com dois valores via teclado, onde o segundo deverá ser maior que o primeiro. Caso contrário solicitar novamente apenas o segundo valor.

num1 = float(input("Insira um valor: "))
num2 = float(input("Insira o segundo valor, maior que o primeiro: "))

while (num2 <= num1):
    print("Valor menor ou igual ao primeiro!")
    num2 = float(input("Insira o segundo valor, maior que o primeiro: "))

