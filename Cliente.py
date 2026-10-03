import socket
import time
import base64
import subprocess
import os

# Configurações de reconexão
MAX_TENTATIVAS = 30
INTERVALO_ESPERA = 2


def receber_mensagem(cliente):
    dados = b""
    while b"\n" not in dados:
        parte = cliente.recv(4096)
        if not parte:
            break
        dados += parte
    return dados.decode().strip()


def conectar_ao_servidor():
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.connect(("localhost", 12345))
            mensagem_inicial = receber_mensagem(cliente)
            if mensagem_inicial.startswith("OK"):
                print("CONECTADO AO SERVIDOR")
                return cliente

            # Servidor cheio
            print(
                f"[Tentativa {tentativa}/{MAX_TENTATIVAS}] "
                f"Servidor cheio. Aguardando {INTERVALO_ESPERA}s..."
            )

            cliente.close()
            time.sleep(INTERVALO_ESPERA)

        except (ConnectionRefusedError, OSError):
            print(
                f"[Tentativa {tentativa}/{MAX_TENTATIVAS}] "
                f"Servidor indisponível. Aguardando..."
            )

            time.sleep(INTERVALO_ESPERA)

    return None

# CONEXÃO COM O SERVIDOR
cliente = conectar_ao_servidor()
if cliente is None:
    print("Não foi possível conectar após várias tentativas. Encerrando.")
    exit()

# MENU PRINCIPAL
executa = True
while executa:
    print("\nMENU:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Enviar Imagem")
    print("0 - Encerrar conexão")
    opcao = input("ESCOLHA UMA OPÇÃO: ")

    # SOMA
    if opcao == "1":
        print("Somar selecionado.")
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        mensagem = f"1|{num1},{num2}"

    # SUBTRAÇÃO
    elif opcao == "2":
        print("Subtração selecionada.")
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        mensagem = f"2|{num1},{num2}"

    # MULTIPLICAÇÃO
    elif opcao == "3":
        print("Multiplicação selecionada.")
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        mensagem = f"3|{num1},{num2}"

    # IMAGEM
    elif opcao == "4":
        print("Envio de imagem selecionado.")
        mensagem = "4|"

    # ENCERRAR
    elif opcao == "0":
        print("Encerrando conexão...")
        mensagem = "0|"
        executa = False

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Tente novamente.")
        continue

    # ENVIA MENSAGEM
    cliente.sendall((mensagem + "\n").encode())

    # Se for 0, não espera resposta
    if opcao == "0":
        break

    # RECEBE RESPOSTA
    resposta = receber_mensagem(cliente)

    # PROCESSAMENTO DA IMAGEM
    if opcao == "4" and resposta.startswith("IMAGEM|"):
        imagem_base64 = resposta[len("IMAGEM|"):]
        print("Imagem recebida em Base64.")
        print(f"Tamanho do Base64: {len(imagem_base64)} caracteres")
        try:
            imagem = base64.b64decode(imagem_base64)
            caminho_imagem = "imagem_recebida.jpg"
            with open(caminho_imagem, "wb") as arquivo:
                arquivo.write(imagem)
            caminho_absoluto = os.path.abspath(caminho_imagem)
            print(f"Imagem salva em: {caminho_absoluto}")
            subprocess.Popen(
                ["google-chrome", caminho_absoluto],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print("Imagem aberta no Google Chrome.")

        except base64.binascii.Error:
            print("Erro: o conteúdo recebido não é um Base64 válido.")

        except OSError as erro:
            print(f"Erro ao salvar ou abrir a imagem: {erro}")

    # OUTRAS RESPOSTAS
    else:
        print("Servidor: " + resposta)

# FECHAMENTO
cliente.close()
print("Conexão encerrada.")