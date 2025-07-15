# imc - indice de massa corpora 
# imc = peso / altura **2 
# imc = peso / (altura * altura) 

nome = 'lucas' 
altura = 1.71
peso = 80
# processamento 
imc = peso / altura **2 
print(nome, 'tem' ,altura, 'de altura\n' ,'peso',peso, ' seu imc é =' , imc)
# f -strings
print(f'{nome} tem {altura} de altura pesa {peso} e seu imc é = {imc:.2f}')
