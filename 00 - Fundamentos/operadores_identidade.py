#comparam se os dois objetos testadam ocupam a mesma posição na memória
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 1000

curso is nome_curso #True
curso is not nome_curso #False
saldo is limite #True
saldo is not limite #False

print(saldo is limite)
print(saldo is not limite)
print(curso is not nome_curso)
print(curso is nome_curso)
