"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
# Entrada dos dados
tamanho_arquivo = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_internet = float(input("Digite a velocidade da internet (em Mbps): "))

# Conversão: de MB para megabits
tamanho_em_megabits = tamanho_arquivo * 8

# Cálculo do tempo em segundos
tempo_segundos = tamanho_em_megabits / velocidade_internet

# Conversão para minutos
tempo_minutos = tempo_segundos / 60

# Saída
print(f"\nTempo aproximado de download: {tempo_minutos:.2f} minutos")
