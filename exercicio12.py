"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

altura = float(input('Digite sua altura em metros'))
Peso_ideal = (72.7 * altura) - 58
print(F'SEu peso ideal é: {Peso_ideal:.2f} kg')