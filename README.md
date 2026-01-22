# Data Engineering Pipeline: SQL Server & REST API Integration

## 📖 Descrição

Este projeto consiste no desenvolvimento de um pipeline de dados (ETL) robusto para a ingestão, processamento e armazenamento de dados provenientes de duas fontes distintas: um banco de dados relacional SQL Server e uma API REST de transações comerciais.

A solução foi projetada para garantir a escalabilidade e a rastreabilidade das informações. O pipeline realiza a extração dos dados brutos (camada Bronze/Raw), utilizando Python para automação e Apache Spark (PySpark) para o processamento distribuído. A arquitetura foca em boas práticas de engenharia, como o gerenciamento de variáveis de ambiente para segurança e um sistema centralizado de logs para monitoramento de falhas.

O projeto é compatível com ambientes de nuvem, como o Databricks, e utiliza conexões seguras via JDBC e autenticação básica para garantir a integridade da comunicação entre os sistemas.

## ⚙️ Setup do Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Configurar Variáveis de Ambiente

O projeto utiliza um arquivo `.env` para gerenciar credenciais de forma segura.

- Copie o arquivo de exemplo:
  ```bash
  cp .env.example .env
  ```
- Preencha o arquivo `.env` com as credenciais de acesso (Host, Usuário, Senha, Banco de Dados).

**Nota:** O arquivo `.env` está configurado no `.gitignore` para evitar a exposição de dados sensíveis.

### 3. Instalar Dependências

Certifique-se de ter o Python 3.x instalado. Recomenda-se o uso de um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 📁 Estrutura do Projeto

A organização segue padrões de modularização para facilitar a manutenção:

- **config/**: Centraliza o carregamento das variáveis de ambiente e configurações globais.
- **data/**: Diretórios locais destinados ao armazenamento temporário de dados (Raw/Processed).
- **logs/**: Armazena os registros de execução do pipeline (INFO, ERROR, DEBUG).
- **notebooks/**: Scripts de validação, testes de conectividade JDBC/API e análise exploratória.
- **src/**: Core do projeto, contendo os scripts de extração, classes de logging e utilitários.

## 📏 Convenções e Padrões

- **Estilo de Código:** Segue as diretrizes do Google Python Style Guide.
- **Tratamento de Exceções:** Blocos de captura de erro estruturados para lidar com falhas de conexão e timeout.
- **Logging Profissional:** Implementação de um logger customizado que registra eventos tanto no console quanto em arquivos físicos com timestamp.

## 🚀 Roadmap de Desenvolvimento

- [x] Configuração do ambiente e gerenciamento de dependências.
- [x] Validação de conectividade com Banco de Dados via JDBC/Spark.
- [x] Teste e integração com API REST (Basic Auth e tratamento de JSON).
- [ ] Implementação da rotina de extração completa das tabelas de negócio.
- [ ] Padronização e limpeza dos dados para a camada Silver.
- [ ] Orquestração do pipeline para execuções agendadas.
