numero = int(input("Digite um número: "))

while(numero <= 0):
    print("Opa, não pode números negativos, apenas positivos!")
    numero = int(input("Digite um número: "))

a = int(input("Digite o ínicio do intervalo: "))

b = int(input("Digite o fim do intervalo: "))

while(b <= a):
    print("opa, é necessario que o valor b seja maior que a")
    b = int(input("Digite o fim do intervalo: "))

for i in range(b, a-1, -1):
    t = numero * i
    print(numero, ' x', i, '=', t )



