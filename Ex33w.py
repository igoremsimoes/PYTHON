#Entrar via teclado com o sexo de determinado usuário, aceitar somente “F” ou “M” como respostas válidas.

s = input("Digite seu sexo (f) feminino e (m) masculino: ")


while ((s != "m") and (s != "f")):
    print("Sexo inválido!")
    s = input("Digite seu sexo (f) feminino e (m) masculino: ")