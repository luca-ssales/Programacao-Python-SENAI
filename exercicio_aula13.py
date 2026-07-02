import random as rd

print('--Atividades--')

# 1 - Crie um número aleatório de 5,10
print('1️⃣ -Crie um número aleatório de 5,10')
opcoes = 5,6,7,8,9,10
numero = rd.choice(opcoes)
print(numero)
print()

#2 - Crie 3 números aleatórios
print('2️⃣ -Crie 3 numeros aleatorios')
op1 = 1,2,3,4,5,6,7,8,9,10
op2 = 1,2,3,4,5,6,7,8,9,10
op3 = 1,2,3,4,5,6,7,8,9,10

nu1 = rd.choice(op1)
nu2 = rd.choice(op2)
nu3 = rd.choice(op3)

print(nu1, nu2, nu3)
print()

#3 - Crie um número aleatório entre 10 a 30 utilize o range()
print('3️⃣ -Crie um número aleatório entre 10 a 30 utilize o range()')

nume = rd.choice(range(10, 31)) 
print(nume)
print()

#4 - Contagem regressiva simples 
print('4️⃣ -Contagem regressiva simples')
for i in range(10,0, -1):
        print(i)
print('FOGO!🔥🧨')
print()

#5 - Soma de numeros pares
print('5️⃣ -Soma de números pares')

n = int(input("Digite um número inteiro positivo: "))

soma = 0  

for i in range(2, n + 1): 
    if i % 2 == 0: 
        soma = soma + i 
print(f"A soma de todos os pares de 2 até {n} é: {soma}")
print()

#6- Tabuada de multiplicação
print('6️⃣ -Tabuada de Multiplicação')

num = int(input("Digite um número inteiro para ver a tabuada: "))

print(f"\n--- Tabuada do {num} ---")

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
print()

#7 -  Números ímpares reversos
print('7️⃣ -Contagem regressiva simples')
for i in range(99,0, -2):
        print(i)
