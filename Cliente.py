import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 12345))
print("CONECTADO AO SERVIDOR")

executa = True

while executa:
    print("\n - MENU -")
    print("1- Somar")
    print("2- Subtrair")
    print("3- Multiplicar")
    print("4- Enviar imagem")
    print("0- Encerrar conexão")

    opcao = input("ESCOLHA UMA OPÇÃO: ")

    # Monta a mensagem no formato CODIGO|NUM1,NUM2
    if opcao in ("1", "2", "3"):
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        mensagem = f"{opcao}|{num1},{num2}"
    elif opcao == "4":
        mensagem = "4|"
    elif opcao == "0":
        mensagem = "0|"
        executa = False
    else:
        print("Opção inválida. Tente novamente.")
        continue  # volta para o início do while sem enviar nada

    # Envia a mensagem para o servidor
    cliente.sendall((mensagem + "\n").encode())

    # Se for encerrar, sai do loop sem esperar resposta
    if opcao == "0":
        print("Encerrando conexão...")
        break

    # Recebe a resposta do servidor
    resposta = cliente.recv(1024).decode()
    print(resposta, end="")

cliente.close()
print("Conexão encerrada.")