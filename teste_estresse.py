import socket
import threading
import time

HOST = "localhost"
PORTA = 12345
QUANTIDADE_CLIENTES = 10

def executar_cliente(id_cliente):
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORTA))

        # Recebe a mensagem inicial do servidor
        mensagem_inicial = cliente.recv(1024).decode().strip()
        print(f"[Cliente {id_cliente}] {mensagem_inicial}")

        # Servidor cheio
        if mensagem_inicial.startswith("ERRO"):
            print(f"[Cliente {id_cliente}] conexão recusada.")
            cliente.close()
            return

        # SOMA
        cliente.sendall("1|10,5\n".encode())
        resposta = cliente.recv(1024).decode().strip()
        print(
            f"[Cliente {id_cliente}] "
            f"Soma: {resposta}"
        )

        # SUBTRAÇÃO
        cliente.sendall("2|20,5\n".encode())
        resposta = cliente.recv(1024).decode().strip()
        print(
            f"[Cliente {id_cliente}] "
            f"Subtração: {resposta}"
        )

        # MULTIPLICAÇÃO
        cliente.sendall("3|4,5\n".encode())
        resposta = cliente.recv(1024).decode().strip()
        print(
            f"[Cliente {id_cliente}] "
            f"Multiplicação: {resposta}"
        )

        # Mantém o cliente conectado durante o teste
        time.sleep(3)

        # ENCERRAMENTO
        cliente.sendall("0|\n".encode())
        print(f"[Cliente {id_cliente}] encerrado.")
        cliente.close()

    except ConnectionRefusedError:
        print(
            f"[Cliente {id_cliente}] "
            "servidor não está disponível."
        )

    except Exception as e:
        print(
            f"[Cliente {id_cliente}] "
            f"erro: {e}"
        )

def main():

    print("TESTE PYTHON")
    print(
        f"Quantidade de clientes: "
        f"{QUANTIDADE_CLIENTES}"
    )
    print()
    threads = []

    # Cria as threads dos clientes
    for i in range(QUANTIDADE_CLIENTES):
        id_cliente = i + 1
        thread = threading.Thread(
            target=executar_cliente,
            args=(id_cliente,)
        )
        threads.append(thread)

    # Inicia todos os clientes
    print("Iniciando clientes...\n")
    for thread in threads:
        thread.start()

    # Aguarda todos terminarem
    for thread in threads:
        thread.join()

    print()
    print("TESTE FINALIZADO")

if __name__ == "__main__":
    main()