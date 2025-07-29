"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: • o produto do dobro do primeiro com metade do segundo .
 • a soma do triplo do primeiro com o terceiro. • o terceiro elevado ao cubo.
"""
inteiro1 = int(input('digite o primeiro numero:'))
inteiro2 = int(input('digite o segundo numero:'))
real = float(input('digite um numero real:'))

resultado1 = (2 * inteiro1) * (inteiro2 / 2)
resultado = (3 * inteiro1) + real 
resultado3 = real **3

print(f'o produto do dobro do primeiro com metade do segundo é: ')
print(f'a soma do triplo do primeiro com o terceiro é:  ')
print(f'o terceiro numeor elevado ao cubo é: {resultado3}')