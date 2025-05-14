# Solicita ao usuário um número inteiro N
N = int(input("Digite um número inteiro: "))

# Inicializa o fatorial como 1 (porque o fatorial de 0 e 1 é 1)
fatorial = 1

# Calcula o fatorial de N
for i in range(1, N + 1):
    fatorial *= i  # Multiplica o fatorial pelo número atual

# Exibe o resultado
print(f"O fatorial de {N} é: {fatorial}")
