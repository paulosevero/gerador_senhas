"""Este é o módulo de geração de senhas.

Ele encapsula a lógica de geração de senhas, permitindo que o usuário gere senhas com base em parâmetros fornecidos.
"""

# Importando o módulo string para coletar os caracteres permitidos nas senhas
import string

# Importando o módulo random para selecionar caracteres aleatórios
import random


def gerar_senha(comprimento: int, possui_simbolos: bool) -> str:
    """Função que gera uma senha com base em dois parâmetros:
    1. Comprimento da senha
    2. Se a senha deve conter símbolos especiais

    Args:
        comprimento (int): Comprimento da senha a ser gerada.
        possui_simbolos (bool): Indica se a senha deve conter símbolos especiais.

    Returns:
        senha_gerada (str): Senha gerada com base nos parâmetros fornecidos.
    """
    # Coletando a lista de caracteres permitidos
    caracteres_permitidos = string.ascii_letters
    if possui_simbolos:
        caracteres_permitidos += string.punctuation

    # Definindo a senha gerada inicialmente como uma string vazia
    senha_gerada = ""

    # Criando a senha gerada aleatoriamente
    for posicao in range(comprimento):
        posicao_aleatoria = random.randint(0, len(caracteres_permitidos) - 1)
        caractere_aleatorio = caracteres_permitidos[posicao_aleatoria]
        senha_gerada += caractere_aleatorio

    return senha_gerada
