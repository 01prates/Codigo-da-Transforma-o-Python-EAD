def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        else:
            print("Operação inválida!")
            return

        print(f"Resultado: {resultado}")

    except ZeroDivisionError:
        print("Erro: Não é possível dividir um número por zero!")
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

calculadora()