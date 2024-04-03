def verifica_maior_idade():
    idade = int(input('Digite sua idade: '))

    if idade <= 0: {
        print('Digite um numero maior que Zero')

    }
    elif idade >= 18:
        print(f'Você tem {idade} anos então e de maior')
    else:
        print(f'Você tem {idade} anos então e de menor')
              
    
verifica_maior_idade()