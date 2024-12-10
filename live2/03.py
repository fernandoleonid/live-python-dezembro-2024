senha_correta = '123'
senha_digitada = ''

contador = 0
while senha_digitada != senha_correta:
    senha_digitada = input("Digite sua senha: ")
    if senha_digitada != senha_correta:
        contador += 1
        print (f"Tentativa {contador}, tente novamente!")
        

print ("Bem-vindo ao Sistema!")