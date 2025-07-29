"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas: • Para homens: (72.7h) - 58 • Para mulheres: (62.1h) - 44.7
"""
sexo = input('digite seu sexo (M para masculino, F para feminino): ').strip().upper()
altura =float(input('digite sua altura em metros'))

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 'esta palavra letra não é valida'
if peso_ideal is not None:
    print(f'seu peso ideal é:{peso_ideal:.2f} kg')
else:
    print('sexo invalido. use apenas "M" ou "F".')
    
          