"""Este é o módulo principal do programa de geração de senhas.

Em específico, este módulo possui um menu interativo que permite ao usuário escolher parâmetros para a geração de senhas.
"""

# Importando a função de geração de senhas do módulo geracao_senhas
from geracao_senhas import gerar_senha


def menu():
    print("==== GERAÇÃO DE SENHAS ====")
    print()
    comprimento_senha = input("Defina o comprimento da senha: ")
    senha_possui_simbolos = input("A senha deve conter símbolos? (s/n): ")

    if senha_possui_simbolos == "s":
        senha_possui_simbolos = True
    else:
        senha_possui_simbolos = False

    senha_gerada = gerar_senha(
        comprimento=int(comprimento_senha),
        possui_simbolos=senha_possui_simbolos,
    )
    print(f"Senha gerada: {senha_gerada}")


# Executando o menu interativo
menu()
