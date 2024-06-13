from datetime import datetime

num_list = list(range(1, 11))
print(num_list)

print('-' * 50)

name_list = ['Rafael', 'Jun', 'Teramae', 'Dantas']
print(name_list)

print('-' * 50)

year_list = [2003, datetime.today().year]
print(year_list)

print('-' * 50)

print('Soma dos numeros impares de 1-10:')
soma = 0
for n in num_list:
    if n % 2 != 0:
        soma += n
print(f'Resultado: {soma}') 

print('-' * 50)

for i in range(len(num_list) - 1, -1, -1):
    print(num_list[i])

print('-' * 50)

num = int(input('Digite um numero: '))
print(f'Tabuada do numero {num}:')
for i in range(1, 11):
    print(f'{num} * {i} = {num * i}')

print('-' * 50)

soma = 0
num_list2 = num_list
try:
    for n in num_list2:
        soma += n
    print(f'Soma: {soma}')
except:
    print('N/A')

print('-' * 50)

soma = 0
num_list3 = num_list
try:
    for n in num_list3:
        soma += n
    media = soma / len(num_list3)
    print(f'Media: {media}')
except:
    print('Divisao por 0')