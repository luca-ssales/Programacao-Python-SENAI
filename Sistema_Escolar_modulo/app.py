# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 

# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA 
# E A MEDIA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO,
# ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES

import modulo as md

print('----- 💻 Sistema escolar -----')
nome = input('Insira seu nome: ')

dados = []

quantidade = int(input(f'{nome}, quantas notas voce deseja cadastrar? '))

for i in range(quantidade):
    nota = float(input('Digite a nota: '))
    dados.append(nota)
else:
    print('-----------------------------------------')
    print('Moda', md.mode_(dados))
    print('Media:', md.mean_(dados))
    print('Desvio Padão:', md.desvio_(dados))
    print('Menor nota:', md.menor_n(dados))
    print('Maior nota', md.maior_n(dados))

print('-----------------------------------------')













