"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
 a quantidades de latas de tinta a serem compradas e o preço total.
"""
area = float(input('Digite o tamanha da area a ser pintada (em metros quadrados):'))
litros_necessarios = area / 3 
latas = int(litros_necessarios / 18)
if litros_necessarios % 18 !=0:
    latas += 1
preco_total = latas * 80

print(f'\nÀrea a ser pintada : {area:.2f} m²')
print(f'litros necessários : {litros_necessarios:.2f} L')
print(f'quantidade de latas : {latas}')
print(f'preço total  : R$ {preco_total:.2f}')
