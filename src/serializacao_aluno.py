import javaobj.v3 as javaobj

from javaobj.constants import ClassDescFlags
from javaobj.v3.beans import (
    FieldType, #descreve um campo
    JavaClassDesc, #descreve uma classe
    JavaField, #informa o tipo do campo
    JavaInstance, #representa o obj
    JavaString, #representa valores do tipo texto no formato de serialização Java
)


def serializar_aluno(nome, matricula, curso):
    # Define os campos String da classe Java Aluno.
    campo_curso = JavaField(
        type=FieldType.OBJECT,
        name="curso",
        class_name="Ljava/lang/String;",
    )

    campo_matricula = JavaField(
        type=FieldType.OBJECT,
        name="matricula",
        class_name="Ljava/lang/String;",
    )

    campo_nome = JavaField(
        type=FieldType.OBJECT,
        name="nome",
        class_name="Ljava/lang/String;",
    )

    # Deve corresponder à classe Aluno do servidor Java.
    descricao_aluno = JavaClassDesc(
        handle=0,
        name="Aluno",
        serial_version_uid=1,
        desc_flags=ClassDescFlags.SC_SERIALIZABLE,
        fields=[campo_curso, campo_matricula, campo_nome],
    )

    aluno = JavaInstance(
        handle=0,
        classdesc=descricao_aluno,
        field_data={
            descricao_aluno: {
                campo_curso: JavaString(handle=0, value=curso),
                campo_matricula: JavaString(
                    handle=0, value=matricula
                ),
                campo_nome: JavaString(handle=0, value=nome),
            }
        },
    )

    return javaobj.dumps(aluno)


def enviar_aluno(cliente, mensagem):
    # Serializa os dados recebidos do menu.
    dados = serializar_aluno(
        nome=mensagem["nome"],
        matricula=mensagem["matricula"],
        curso=mensagem["curso"],
    )

    # Envia o código da operação e o tamanho do objeto.
    cabecalho = f"5|{len(dados)}\n".encode("utf-8")
    cliente.sendall(cabecalho)

    # Envia os bytes serializados.
    cliente.sendall(dados)

    print(f"Dados do aluno enviados ({len(dados)} bytes).")
