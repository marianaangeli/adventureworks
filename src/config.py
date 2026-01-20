import os
from dotenv import load_dotenv

# O load_dotenv procura o arquivo .env e carrega o que está lá dentro
load_dotenv()

# Pegando as variáveis do .env e salvando em nomes fáceis no Python
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Configurações da API
API_URL = os.getenv("API_URL")
API_USER = os.getenv("API_USER")
API_PASSWORD = os.getenv("API_PASSWORD")

# Teste para ver se funcionou (ele vai imprimir no terminal)
if DB_HOST:
    print("✅ Sucesso: O arquivo .env foi lido corretamente!")
    print(f"📡 Host configurado: {DB_HOST}")
else:
    print("❌ Erro: Não consegui ler o arquivo .env. Verifique se o nome está correto.")