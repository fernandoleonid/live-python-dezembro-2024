# Um vendedor recebe uma comissão por suas vendas. 
# Dependendo do valor da venda, a comissão varia. 
# A comissão é calculada da seguinte forma:
# - 5% para vendas de até R$1.000,00
# - 7.5% para vendas entre R$1.000,01 e R$5.000,00
# - 10% para vendas entre R$5.000,01 e R$10.000,00
# - 15% para vendas acima de R$10.000,00
# Escreva um programa em Python que calcule a 
# comissão do vendedor, dado o valor da venda e o 
# nome do vendedor.

nomevendedor = input('Olá, vendedor. digite seu nome: ')
valorVenda = float(input((f'Olá, {nomevendedor}. Para calcular o valor de sua comissão, digite aqui o valor do produto: ')))

if valorVenda <= 1000.00:
    comissao = valorVenda * 0.05
elif valorVenda <= 5000.00:
    comissao = valorVenda * 0.075
elif valorVenda <= 10000.00:
    comissao = valorVenda * 0.10
else:
    comissao = valorVenda * 0.15


print (f"{nomevendedor}, sua venda no valor de R${valorVenda} terá uma comissão de R${comissao}")