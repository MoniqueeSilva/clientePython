def mostrar_menu():
    print("\nMENU:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Enviar Imagem")
    print("5 - Enviar informações do aluno")
    print("0 - Encerrar conexão")
    return input("ESCOLHA UMA OPÇÃO: ")

def criar_mensagem(opcao):
    if opcao in ("1", "2", "3"):
        operacoes = {
            "1": "Somar",
            "2": "Subtração",
            "3": "Multiplicação"
        }

        print(f"{operacoes[opcao]} selecionada.")
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        return f"{opcao}|{num1},{num2}"

    if opcao == "4":
        print("Envio de imagem selecionado.")
        return "4|"

    if opcao == "5":
        nome = input("Nome do aluno: ")
        matricula = input("Matricula: ")
        curso = input("Curso")
        return {
            "nome": nome,
            "matricula": matricula,
            "curso": curso
        }

    if opcao == "0":
        print("Encerrando conexão...")
        return "0|"

    print("Opção inválida. Tente novamente.")
    return None