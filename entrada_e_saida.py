# def chamar_usuario():
#     nome = input('Qual e o seu nome? ')
#     print(f'Olá, {nome}! Seja bem-vindo(a)!')

# chamar_usuario()

# def somar_numeros(num_a, num_b):
#     soma = num_a + num_b

#     print(f'A soma dos resultados é: {soma}')
#     return soma

# somar_numeros(5,6)

# def multiplicar_numeros(num_a, num_b):
#     multiplicacao = num_a * num_b

#     print(f'O produto dos numeros é: {multiplicacao}')
#     return multiplicacao

# multiplicar_numeros(5,6)

# def divisao_numeros(num_a, num_b):
#     divisao = num_a / num_b

#     print('f'A divisão dos numeros é: {divisao}')
#     return divisao

# divisao_numeros(30,6)

def  calcular_imc(altura, peso):
    imc = peso / (altura * altura)
    print(f'seu imc e: {imc}')
    return imc

calcular_imc(2,100)