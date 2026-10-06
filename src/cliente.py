from conexao import conectar_ao_servidor, receber_mensagem
from menu import mostrar_menu, criar_mensagem
from imagem import processar_imagem


def main():
    cliente = conectar_ao_servidor() # Estabelece conexão com o servidor e guarda o socket retornado

    if cliente is None:
        print("Não foi possível conectar. Encerrando.")
        return

    try:
        while True:
            opcao = mostrar_menu() 
            mensagem = criar_mensagem(opcao) # Converte a opção escolhida em uma mensagem para enviar ao servidor

            if mensagem is None:
                continue

            cliente.sendall((mensagem + "\n").encode()) # Envia mensagem ao servidor codificada em bytes

            if opcao == "0":
                break

            resposta = receber_mensagem(cliente) # Aguarda e recebe a resposta enviada pelo servidor

            if opcao == "4":
                processar_imagem(resposta)
            else:
                print("Servidor:", resposta)

    finally:
        cliente.close()
        print("Conexão encerrada.")


if __name__ == "__main__":
    main()