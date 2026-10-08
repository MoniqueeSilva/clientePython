import socket
import time

HOST = "10.10.136.139"
PORTA = 12346

MAX_TENTATIVAS = 30
INTERVALO_ESPERA = 2

# Função que recebe uma mensagem completa (até encontrar '\n')
def receber_mensagem(cliente):
    dados = b"" # Buffer

    while b"\n" not in dados:
        parte = cliente.recv(4096) # Lê bytes do socket

        if not parte:
            break

        dados += parte

    return dados.decode().strip() # Converte bytes em string, remove espaços e o '\n' do final

# Função que tenta conectar ao servidor
def conectar_ao_servidor():
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        
        # Capturar erros de conexão
        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP
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

        # Captura erros de conexão
        except (ConnectionRefusedError, OSError):
            print(
                f"[Tentativa {tentativa}/{MAX_TENTATIVAS}] "
                f"Servidor indisponível. Aguardando..."
            )
            time.sleep(INTERVALO_ESPERA)

    return None