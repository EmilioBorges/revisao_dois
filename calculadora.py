def somar(numA, numB):
    soma = numA + numB
    print(f'A soma de {numA} + {numB} = {soma}')
    return soma

def subtrair(numA, numB):
    subtracao = numA - numB
    print(f'A subtração de {numA} - {numB} = {subtracao}')
    return subtracao

def multiplicar(numA, numB):
    multiplicacao = numA * numB
    print(f'A multiplicação de {numA} * {numB} = {multiplicacao}')
    return multiplicacao

def dividir(numA, numB):  
    divisao = numA / numB
    print(f'A divisão de {numA} / {numB} = {divisao:.2f}')
    return divisao


def calculadora():
    sair = False

    print('---------------------------------------')
    print('------------- CALCULADORA -------------')
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair")
    print('---------------------------------------')

    while sair == False:
        try:
            
            tipo_operador = input("Digite o numero da operação desejada: ")

            operadores_permitidos = '12340'

            if tipo_operador not in operadores_permitidos:
                print(f'Operador {tipo_operador} invalido')
                continue

            if len(tipo_operador) > 1:
                print('Digite apenas um operador..')
                continue

            if tipo_operador == '0':
                print('Calculadora Finalizada...')
                break

            number_one = float(input("Digite o primeiro numero: "))
            number_two = float(input("Digite o segundo numero: "))
            
        
            match tipo_operador:
                case '1':
                    somar(number_one, number_two)
                    print('---------------------------------------')
                case '2':
                    subtrair(number_one, number_two)
                    print('---------------------------------------')
                case '3':
                    multiplicar(number_one, number_two)
                    print('---------------------------------------')
                case '4':
                    if number_one == 0:
                        print("Nenhum número pode ser dividido por zero")
                    else:
                        dividir(number_one, number_two)
                    print('---------------------------------------')
                case '0':
                    sair = True
        except:
            print("Você não digitou um número: ")


calculadora()

