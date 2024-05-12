"""
Suponha que você esteja trabalhando em um projeto para uma
empresa de análise de dados que precisa calcular a média da renda
familiar de um conjunto indefinido de famílias residentes na cidade de
Tangamandápio. Você foi designado para escrever um programa em
Python que leia a renda mensal de cada membro de uma família (o
número de indivíduos da família deve ser solicitado ao usuário) e em
seguida calcule e imprima a renda total da família, o número de
indivíduos e a renda familiar média. O número de famílias é indefinido,
logo, o seu programa deve solicitar se ainda há famílias para serem
calculadas pelo sistema e ao final da inserção dos dados de todas as
famílias, o seu programa deve imprimir a renda familiar média da
cidade, além do percentual de famílias que possuem renda familiar
média inferior a 1 salário mínimo e a quantidade de famílias com
renda familiar média superior a 10 salários mínimos.
Obs: Considere para o salário mínimo, o valor de R$ 1.212,00 e que a
renda familiar média da cidade é a soma de todas as rendas familiares
divididas pela quantidade de famílias da cidade.
"""

contador_familias = 0 
renda_cidade = []
contador_maior = 0 
contador_menor = 0 
while True: 
    contador_familias += 1 
    individuos_familia = int(input('Digite a quantidade de mebros que tem na família: '))
    renda_familia = []

    for individuo in range (individuos_familia): 
        renda_individuo = float(input(f'Digite aqui a renda do indivíduo {individuo+1}: '))
        renda_familia.append(renda_individuo)
        media_familia = sum(renda_familia) / individuos_familia
    renda_cidade.append(sum(renda_familia))

    print(f'A renda total da família {contador_familias} é: {sum(renda_familia)}')
    print(f'O número total de indivíduos da família {contador_familias} é: {individuos_familia}')
    print(f'A média da renda da família {contador_familias} é: {media_familia:.2f}')

    if media_familia < 1212:
        contador_menor += 1  
    elif media_familia > 1212: 
        contador_maior += 1 
    continuar = input('Deseja continuar?[s/n]: ')
    if continuar == 'n': 
        break

percentual = (contador_menor * 100) / contador_familias
print('=-'*30)
print(f'A renda média da cidade é: {sum(renda_cidade) / contador_familias:.2f}')
print(f'O percentual de famílias com renda média inferior a 1 salário mínimo é: {percentual:.2f} %')
print(f'A quantidade de famílias com renda superior à 10 salários mínimos é: {contador_maior}')
