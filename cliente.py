from conexao import conectar_ao_servidor, receber_mensagem
from menu import mostrar_menu, criar_mensagem
from imagem import processar_imagem


def main():
    cliente = conectar_ao_servidor()

    if cliente is None:
        print("Não foi possível conectar. Encerrando.")
        return

    try:
        while True:
            opcao = mostrar_menu()
            mensagem = criar_mensagem(opcao)

            if mensagem is None:
                continue

            cliente.sendall((mensagem + "\n").encode())

            if opcao == "0":
                break

            resposta = receber_mensagem(cliente)

            if opcao == "4":
                processar_imagem(resposta)
            else:
                print("Servidor:", resposta)

    finally:
        cliente.close()
        print("Conexão encerrada.")


if __name__ == "__main__":
    main()