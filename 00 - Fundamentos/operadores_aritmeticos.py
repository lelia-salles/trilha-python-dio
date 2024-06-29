'''
pecedência dos operadores: parêntesis, expoentes,multiplicação e divisão, 
, somas e subtrações (esq. para dir.).
Caso se queira que uma operação com precedência menor seja realizada
primeiro, basta colocar a expressão entre parêntesis
'''

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4
y = (10 / 2) + 25 * ((2 - 2) ** 2)
print(x)
print(y)
