def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: divisão por zero"

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite sua escolha (1/2/3/4): ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print(numero1, "+", numero2, "=", adicao(numero1, numero2))
elif escolha == '2':
    print(numero1, "-", numero2, "=", subtracao(numero1, numero2))
elif escolha == '3':
    print(numero1, "*", numero2, "=", multiplicacao(numero1, numero2))
elif escolha == '4':
    print(numero1, "/", numero2, "=", divisao(numero1, numero2))
else:
    print("Escolha inválida")
