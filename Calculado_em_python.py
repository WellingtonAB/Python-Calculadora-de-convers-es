
print("############# Bem vindo a Calculadora ############################ ")


###### Funções #########
# Adição
ad = lambda x,y : x+y
# Subtração
su = lambda x,y : x-y
# Multiplicação
mu = lambda x,y : x*y
# Divisão
di = lambda x,y : x/y

#############################

valor1 = 0
valor2 = 0
escolha = 0
escolha2 = 0
resultado = 0

i = 0
aux = 0

while aux != "auxiliando":
    while escolha != "S":
        if(i == 0 or escolha2 == "cinco"):
            valor1 = int(input("Escolha um número: "))
            escolha2 = 0
        else:
            valor1 = resultado
        print("O que você deseja?")
        print("[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Apagar\n[6] Sair")
        escolha = int(input("Escolha a operação: "))

        if(escolha != 5 and escolha != 6):
            valor2 = int(input("Escolha outro número: "))


        if(escolha == 1):
            resultado = ad(valor1,valor2)
        if(escolha == 2):
            resultado = su(valor1,valor2)
        if(escolha == 3):
            resultado = mu(valor1,valor2)
        if(escolha == 4):
            resultado = di(valor1,valor2)
        if(escolha == 5):
            escolha2 = "cinco"
        if(escolha == 6):
            break


        escolha = str(input("Finalizou? \n[S] Sim\n[N] Não\n\n"))
        i += 1
        if(escolha == "N"):
            print("A parcial é %s." %resultado)

    print("O resultado gerado é %s." %resultado)



    ############### Parte 2 - Formato ###################

    print("Deseja mudar o formato do resultado?")
    mudar = str(input("[S] Sim\n[N] Não\n\n"))

    if(mudar == "S"):

        print("Qual o formato?\n[1] Binário\n[2] Deciamal\n[3] Octal\n[4] hexadecimal\n[5] Sair")
        formato = int(input("Escolha um formato: "))

        if(formato == 1):
            print("O resultado gerado é %s." %bin(resultado))
        if(formato == 2):
            print("O resultado é %s (mesmo da calculadora)." %resultado)
        if(formato == 3):
            print("O resultado gerado é %s." %oct(resultado))
        if(formato == 4):
            print("O resultado gerado é %s." %hex(resultado))
        if(formato == 5):
            print("Fim de processo.")
            aux = "auxiliando"

    else:

        print("Fim de processo.")
        aux = "auxiliando"