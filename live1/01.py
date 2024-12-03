nome_aluno = input('Digite o nome do aluno: ')

nota_caso = int(input('Digite a nota do estudo de caso: '))
nota_portfolio = int(input ('Digite a nota do portfolio: '))

media_aluno = (nota_caso + nota_portfolio) / 2

if media_aluno >= 5:
    situacao = 'Aprovada'
else:
    situacao = 'Reprovada'

print(f"A aluna {nome_aluno} tem a média {media_aluno} e está {situacao}")