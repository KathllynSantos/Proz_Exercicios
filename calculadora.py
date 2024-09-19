def calculadora():
    while True:
        # Exibe o menu de operações
        print("Escolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        # Solicita a escolha do usuário
        opcao = input("Digite o número da operação: ")
        
        if opcao == '0':
            print("Saindo...")
            break
        
        if opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existe")
            continue
        
        # Solicita os números para a operação
        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
            continue
        
        # Realiza a operação com base na escolha do usuário
        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado da soma: {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {resultado}")
        elif opcao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da divisão: {resultado}")
            else:
                print("Erro: Divisão por zero")
        
        # Mostra o menu novamente após cada operação
        print()

# Chama a função para iniciar o programa
calculadora()
