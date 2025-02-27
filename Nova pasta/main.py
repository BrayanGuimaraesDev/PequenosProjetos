while True:
    try:
        # Solicita os números e a operação
        PrimeiroNumero = int(input("Primeiro número (ou digite 0 para sair): "))
        if PrimeiroNumero == 0:
            print("Saindo...")
            break  # Sai do loop

        SegundoNumero = int(input("Segundo número: "))
        Operacao = input("Escolha o operador (+, -, *, /): ")

        # Verifica se o operador é válido
        if Operacao not in ["+", "-", "*", "/"]:
            print("Operador inválido! Tente novamente.")
            continue  # Volta ao início do loop

        # Realiza a operação
        if Operacao == "+":
            Resultado = PrimeiroNumero + SegundoNumero
        elif Operacao == "-":
            Resultado = PrimeiroNumero - SegundoNumero
        elif Operacao == "*":
            Resultado = PrimeiroNumero * SegundoNumero
        elif Operacao == "/":
            if SegundoNumero != 0:
                Resultado = PrimeiroNumero / SegundoNumero
            else:
                Resultado = "Erro: Divisão por zero!"

        # Exibe o resultado
        print("Resultado:", Resultado)

    except ValueError:
        print("Erro: Entrada inválida! Certifique-se de inserir números inteiros.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja fazer outra operação? (s/n): ").strip().lower()
    if continuar != "s":
        print("Saindo...")
        break
