num = int(input('Digite um numero: '))

if num % 2 == 0:
    print(f'O numero {num} é par')
else:
    print(f'O numero {num} é ímpar')

print('-' * 10)

idade = int(input('Digite sua idade: '))

if 0 <= idade <= 12:
    print('Criança')
elif 13 <= idade <= 18:
    print('Adolescente')
elif idade > 18:
    print('Adulto')
else:
    print('Idade inválida')

print('-' * 10)

USERNAME = 'teste'
PASSWORD = 'teste'

username = input('Username: ')
password = input('Password: ')

if USERNAME == username and PASSWORD == password:
    print('Credenciais corretas')
else:
    print('Credenciais incorretas')

print('-' * 10)

x = float(input('Coordenada X: '))
y = float(input('Coordenada Y: '))

if x > 0 and y > 0:
    print('Primeiro quadrante')
elif x < 0 and y > 0:
    print('Segundo quadrante')
elif x < 0 and y < 0:
    print('Terceiro quadrante')
elif x > 0 and y < 0:
    print('Quarto quadrante')
else:
    print('Origem')