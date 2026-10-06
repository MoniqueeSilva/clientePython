import base64 
import subprocess 
import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Descobre a pasta raiz do projeto
CAMINHO_IMAGEM = os.path.join(BASE_DIR, "imagem_recebida.jpg") # Monta o caminho completo onde a imagem será salva

def processar_imagem(resposta):
    if not resposta.startswith("IMAGEM|"):
        print("Servidor:", resposta)
        return
    
    imagem_base64 = resposta[len("IMAGEM|"):] # Pega só o conteúdo Base64 e fatia a string 
    print("Imagem recebida em Base64.")
    print(f"Tamanho do Base64: {len(imagem_base64)} caracteres")

    try:
        imagem = base64.b64decode(imagem_base64) # Converte o texto de volta para bytes
        with open(CAMINHO_IMAGEM, "wb") as arquivo: # Abre/cria o arquivo em binário
            arquivo.write(imagem)

        caminho_absoluto = os.path.abspath(CAMINHO_IMAGEM)
        print(f"Imagem salva em: {caminho_absoluto}")

        # Abre o Chrome com o caminho da imagem
        subprocess.Popen(["google-chrome", caminho_absoluto],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

        print("Imagem aberta no Chrome.")

    except base64.binascii.Error:
        print("Erro: o conteúdo recebido não é um Base64 válido.")

    except OSError as erro:
        print(f"Erro ao salvar ou abrir a imagem: {erro}")