import socket
import threading
import time

# CONFIGURAÇÕES
HOST = "localhost"
PORTA = 12345
QUANTIDADE_CLIENTES = 10
TEMPO_CONECTADO = 3

# COMUNICAÇÃO
def receber_mensagem(cliente):
    dados = b""
    while b"\n" not in dados:
        parte = cliente.recv(4096)
        if not parte:
            break

        dados += parte

    return dados.decode().strip()

def enviar_mensagem(cliente, mensagem):
    cliente.sendall((mensagem + "\n").encode())

# TESTES
def testar_operacoes(cliente, id_cliente):
    # SOMA
    enviar_mensagem(cliente, "1|10,5")
    resposta = receber_mensagem(cliente)
    print(f"[Cliente {id_cliente}] Soma: {resposta}")

    # SUBTRAÇÃO
    enviar_mensagem(cliente, "2|20,5")
    resposta = receber_mensagem(cliente)
    print(f"[Cliente {id_cliente}] Subtração: {resposta}")

    # MULTIPLICAÇÃO
    enviar_mensagem(cliente, "3|4,5")
    resposta = receber_mensagem(cliente)
    print(f"[Cliente {id_cliente}] Multiplicação: {resposta}")

# CLIENTE DE TESTE
def executar_cliente(id_cliente):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((HOST, PORTA))

        # Mensagem inicial
        mensagem_inicial = receber_mensagem(cliente)
        print(f"[Cliente {id_cliente}] " f"{mensagem_inicial}")

        # Servidor recusou a conexão
        if mensagem_inicial.startswith("ERRO"):
            print(f"[Cliente {id_cliente}]" "conexão recusada.")
            return

        # Testa operações
        testar_operacoes(cliente, id_cliente)

        # Mantém o cliente conectado
        time.sleep(TEMPO_CONECTADO)

        # Encerramento
        enviar_mensagem(cliente, "0|")
        print(f"[Cliente {id_cliente}] ""encerrado.")

    except ConnectionRefusedError:
        print(f"[Cliente {id_cliente}] " "servidor não está disponível.")

    except OSError as erro:
        print(f"[Cliente {id_cliente}] " f"erro de conexão: {erro}")

    finally:
        cliente.close()

# EXECUÇÃO DO TESTE
def main():
    print("TESTE DE MÚLTIPLOS CLIENTES")
    print(f"Quantidade de clientes: " f"{QUANTIDADE_CLIENTES}")
    print()

    threads = []

    # Cria as threads
    for id_cliente in range(1, QUANTIDADE_CLIENTES + 1):
        thread = threading.Thread(target=executar_cliente, args=(id_cliente,))
        threads.append(thread)

    # Inicia os clientes
    print("Iniciando clientes...\n")
    for thread in threads:
        thread.start()

    # Aguarda todos os clientes
    for thread in threads:
        thread.join()

    print("TESTE FINALIZADO")

if __name__ == "__main__":
    main()
