# def verifica_maior_idade():
#     idade = int(input('Digite sua idade: '))

#     if idade <= 0: {
#         print('Digite um numero maior que Zero')

#     }
#     elif idade >= 18:
#         print(f'Você tem {idade} anos então e de maior')
#     else:
#         print(f'Você tem {idade} anos então e de menor')
              
    
# verifica_maior_idade()


# def par_impar():
#     numero = int(input('Digite um numero: '))

#     if numero % 2 == 0:
#         print('Numero par')
#     else:
#         print('Numero impar')


# par_impar()

def resultado_final():
    nota = int(input('Digite a sua nota: '))

    if nota < 0:
        print('Dgite um valor maior que 0')
    elif nota >= 7:
        print('Aluno aprovado')
    else:
        print('Aluno Reprovado')

resultado_final()