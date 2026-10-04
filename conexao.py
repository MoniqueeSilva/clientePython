import socket
import time

HOST = "localhost"
PORTA = 12345

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
            cliente.connect((HOST, PORTA))
            mensagem = receber_mensagem(cliente)

            if mensagem.startswith("OK"):
                print("CONECTADO AO SERVIDOR")
                return cliente
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