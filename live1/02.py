# Uma empresa quer calcular o salário de seus 
# funcionários com base em sua carga horária 
# semanal e o valor da hora de trabalho. 
# Além disso, a empresa oferece um bônus 
# de 10% para aqueles funcionários que 
# trabalharem mais de 40 horas por semana, 
# 20% para quem trabalhar mais de 100 horas
# e 30% para quem trabalha mais de 200 horas


carga_horaria = int(input('Digite sua carga horária: '))
valor_hora = float(input('Digite seu valor hora: '))

salario = carga_horaria * valor_hora

if carga_horaria > 200:
    salario = salario * 1.30
elif carga_horaria > 100:
    salario = salario * 1.20
elif carga_horaria > 40:
    salario = salario * 1.10



print (f'Seu salário é: {salario}')