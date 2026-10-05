import base64
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_IMAGEM = os.path.join(BASE_DIR, "imagem_recebida.jpg")

def processar_imagem(resposta):
    if not resposta.startswith("IMAGEM|"):
        print("Servidor:", resposta)
        return
    
    imagem_base64 = resposta[len("IMAGEM|"):]
    print("Imagem recebida em Base64.")
    print(f"Tamanho do Base64: {len(imagem_base64)} caracteres")

    try:
        imagem = base64.b64decode(imagem_base64)
        with open(CAMINHO_IMAGEM, "wb") as arquivo:
            arquivo.write(imagem)

        caminho_absoluto = os.path.abspath(CAMINHO_IMAGEM)
        print(f"Imagem salva em: {caminho_absoluto}")

        subprocess.Popen(["google-chrome", caminho_absoluto],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

        print("Imagem aberta no Chrome.")

    except base64.binascii.Error:
        print("Erro: o conteúdo recebido não é um Base64 válido.")

    except OSError as erro:
        print(f"Erro ao salvar ou abrir a imagem: {erro}")