on = True;

# Programa Um: Imprime strings
def programaUm():
    print("\nEsse programa imprime uma string.")
    print("\nPrograma Um rodando…")
    print("\nAlunos - PLP Unifavip 2022.2")

# Programa Dois: Imprime a entrada
def programaDois():
    print("\nEsse programa recebe uma entrada e imprime-a.")
    print("\nPrograma Dois rodando…")
    # Loop para evitar que o programa crashe
    while True:
        try:
            entrada = input("\nInsira um número: ")
            numero = float(entrada)
            print("\nO número informado foi", numero)
            break
        except ValueError:
            print("Entrada inválida!")

# Programa Três: Soma duas entradas
def programaTres():
    print("\nEsse programa faz uma soma de dois números.")
    print("\nPrograma Três rodando…")

    # Loop para evitar que o programa crashe
    while True:
        try:
            entrada1 = input("\nInsira um número: ")
            num1 = float(entrada1)
            entrada2 = input("\nInsira outro número: ")
            num2 = float(entrada2)
            soma = num1 + num2
            print(f"\nA soma de {num1} + {num2} é", soma)
            break
        except ValueError:
            print("Entrada inválida!")

# Função exibida após o fim de cada programa
def fim():
    print("\nFim do programa.\n")

# Função caso o usuário insira uma opção inválida na entrada
def opcao_invalida():
    print("\nEntrada inválida! Insira apenas 1, 2, 3 ou 4.")

# Função para encerrar o programa
def sair():
    global on
    print("Até mais!")
    on = False    
    
# Função principal que executa os programas 
def executar():
    global on
    while on:
        opcao = input("\nDeseja rodar qual programa: 1, 2 ou 3?\nDigite 4 para encerrar.\n")
        programas = {
            "1": programaUm,
            "2": programaDois,
            "3": programaTres,
            "4": sair
        }
        programas.get(opcao, opcao_invalida)()
        fim()

print("Boas vindas!")

# Loop que executa a principal função do programa
while on:
    executar()