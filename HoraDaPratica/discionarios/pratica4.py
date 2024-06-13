pessoa = {'nome': 'Rafael', 'idade': 21, 'cidade': 'Sao Carlos'}
print(pessoa)

print('-' * 50)

pessoa.update({'idade': 30})
pessoa['profissao'] = 'estudante'
del pessoa['cidade']
print(pessoa)

print('-' * 50)

#num_quadrado_dict  = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
num_quadrado_dict = {n: n*n for n in range(1, 6)}
print(num_quadrado_dict)

print('-' * 50)

chave = 'nome'
dicionario = num_quadrado_dict
if chave in dicionario:
    print(f'A chave {chave} existe em {dicionario}')
else:
    print(f'A chave nao {chave} existe em {dicionario}')

print('-' * 50)

frase = 'Bom dia boa tarde boa noite'
letra_contador = {}
for letra in frase:
    if letra not in letra_contador:
        letra_contador[letra] = 1
    else:
        letra_contador[letra] += 1

print(f'''
Contagem de letras da frase: "{frase}"
{letra_contador}
''')

print('-' * 50)

palavras = frase.split()
palavra_contador = {}
for palavra in palavras:
    if palavra not in palavra_contador:
        palavra_contador[palavra] = 1
    else:
        palavra_contador[palavra] += 1

print(f'''
Contagem de palavra da frase: "{frase}"
{palavra_contador}
''')