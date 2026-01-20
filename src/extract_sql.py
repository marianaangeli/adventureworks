import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def get_config():
    """
    Retorna um dicionário com todas as configurações do projeto.
    Inclui validação de segurança para campos obrigatórios.
    """
    
    # Pegando as variáveis do ambiente
    db_password = os.getenv("DB_PASSWORD")
    api_password = os.getenv("API_PASSWORD")

    # VALIDAÇÃO: Se a senha do banco estiver vazia, levanta um erro (conforme pedido na tarefa)
    if not db_password or db_password.strip() == "":
        raise ValueError("❌ ERRO DE CONFIGURAÇÃO: A senha do banco de dados (DB_PASSWORD) não foi encontrada no .env!")

    config = {
        "db_host": os.getenv("DB_HOST"),
        "db_port": os.getenv("DB_PORT"),
        "db_name": os.getenv("DB_NAME"),
        "db_user": os.getenv("DB_USER"),
        "db_password": db_password,
        "api_url": os.getenv("API_URL"),
        "api_user": os.getenv("API_USER"),
        "api_password": api_password
    }

    return config

# Para facilitar o uso nos outros arquivos, também criamos variáveis globais
configs = get_config()

DB_HOST = configs["db_host"]
DB_PORT = configs["db_port"]
DB_NAME = configs["db_name"]
DB_USER = configs["db_user"]
DB_PASSWORD = configs["db_password"]
API_URL = configs["api_url"]
API_USER = configs["api_user"]
API_PASSWORD = configs["api_password"]

if __name__ == "__main__":
    # Teste rápido de validação
    try:
        c = get_config()
        print("✅ Tarefa 1.4 concluída: Configurações carregadas e validadas!")
        print(f"📡 Conectando ao Host: {c['db_host']}")
    except ValueError as e:
        print(e)