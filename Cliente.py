import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 12345))
# lê a mensagem de boas-vindas do servidor
mensagem_inicial = cliente.recv(1024).decode().strip()
if mensagem_inicial.startswith("ERRO"):
    print(mensagem_inicial)
    cliente.close()
    exit()
print("CONECTADO AO SERVIDOR")

executa = True

while executa:
    print("\nMENU: ")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Enviar Imagem")
    print("0 - Encerrar conexão")
    opcao = input("ESCOLHA UMA OPÇÃO: ")

    if opcao == "1":
        print("Somar selecionado.")
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        mensagem = f"1|{num1},{num2}"
    elif opcao == "2":
        print("Subtração selecionada.")
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        mensagem = f"2|{num1},{num2}"
    elif opcao == "3":
        print("Multiplicação selecionada.")
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        mensagem = f"3|{num1},{num2}"
    elif opcao == "4":
        print("Envio de imagem selecionado.")
        mensagem = "4|"
    elif opcao == "0":
        print("Encerrando conexão...")
        mensagem = "0|"
        executa = False
    else:
        print("Opção inválida. Tente novamente.")
        continue

    cliente.sendall((mensagem + "\n").encode())

    if opcao == "0":
        break

    resposta = cliente.recv(1024).decode()
    print("Servidor: " + resposta)

cliente.close()
print("Conexão encerrada.")