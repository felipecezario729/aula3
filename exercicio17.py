"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
• comprar apenas latas de 18 litros; • comprar apenas galões de 3,6 litros; • misturar latas e galões, de forma que o preço seja o menor.
 Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

area = float(input('Digite o tamanha da Area a ser pintade (em m²):'))
area_com_folga = area * 1.1
litros = area_com_folga / 6
# colocar os valores de cada lata 

litros_lata = 18
preco_lata = 80
litros_galao = 3.6 
preco_galao = 25

# hora de chamar as entradas para latas e galões 
latas_apenas = int(litros / litros_lata)
if litros % litros_lata != 0:
    latas_apenas += 1
preco_lata_apenas = latas_apenas * preco_lata

galao_apenas = int(litros / litros_galao)
if litros % litros_galao != 0:
    galao_apenas += 1
preco_galao_apenas = galao_apenas * preco_galao    

#  misturar latas e galões, de forma que o preço seja o menor.
lata_mistas = int(litros / litros_lata)
resto_litros = litros - (lata_mistas * litros_lata)
galoes_mistos = int(resto_litros / litros_galao)
if resto_litros % litros_galao != 0:
    galoes_mistos += 1
preco_misto = (lata_mistas * preco_lata) + (galoes_mistos * preco_galao)    

# mostra o resultado 
print((f'\n comprar Lata ou Galão'))
print(f'1. apenas latas de 18L: {latas_apenas} lata(s) - R$ {preco_lata_apenas:.2f}')
print(f'2. apenas galões de 3,6L: {galao_apenas} galão(ÕES) - R$ {preco_galao_apenas:.2f}')
print(f'3. Mistura: {lata_mistas} lata(s) e {galoes_mistos} galão(ôes) - R$ {preco_misto:.2f}')
