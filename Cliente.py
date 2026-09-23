import socket

# Cria o socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
cliente.connect(("192.168.68.107", 12345))

print("CONECTADO AO SERVIDOR")

executa = True

while executa:
    print("\n - MENU -")
    print("1- Somar")
    print("2- Subtrair")
    print("3- Multiplicar")
    print("4- Enviar imagem")
    print("0- Encerrar conexão")

    opcao = input("ECOLHA UMA OPÇÃO: ")

    match opcao:
        case "1":
            print("Somar selecionado.")

        case "2":
            print("Subtrair selecionado.")

        case "3":
            print("Multiplicar selecionado.")

        case "4":
            print("Envio de imagem selecionado .")

        case "0":
            print("Encerrando conexão...")
            executa = False

cliente.close()