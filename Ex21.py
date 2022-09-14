a = float(input("Insira o primeiro valor: "))
b = float(input("insira o segundo valor: "))
c = int(input("Escolha uma operacao\n1 – Multiplicação \n2 – Adição \n3 – Divisão \n4 – Subtração \n5 - Fim do programa\n  "))

if c == 1:
   m = b*a 
   print("Resultado: ",m) 
elif c == 2:
    ad = b+a
    print("Resultado: ",ad)
elif c == 3:
    if b == 0:
        print("Valor invalido para divisao")
    else: 
        d = b*a
        print("Resultado: ",d)
elif c == 4:
    s = a-b
    print("Resultado: ",s)
elif c ==5:
    print("Fim do programa, obrigado por utilizar")
else: 
    print("Escolha invalida")