import socket

# Cria o socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
cliente.connect(("192.168.68.107", 12345))

print("conectado")

while True:
    mensagem = input()

    # Envia a mensagem para o servidor
    cliente.sendall((mensagem + "\n").encode())

    # Recebe a resposta do servidor
    resposta = cliente.recv(1024).decode()

    print(resposta, end="")

# Fecha a conexão
cliente.close()