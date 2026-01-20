# Data Engineering Pipeline: SQL Server & REST API Integration

## 📖 Descrição
Este projeto consiste no desenvolvimento de um pipeline de dados (ETL) robusto para a ingestão, processamento e armazenamento de dados provenientes de duas fontes distintas: um banco de dados relacional **SQL Server** e uma **API REST** de transações comerciais.

A solução foi projetada para garantir a escalabilidade e a rastreabilidade das informações. O pipeline realiza a extração dos dados brutos (camada Bronze/Raw), utilizando **Python** para automação e **Apache Spark (PySpark)** para o processamento distribuído. A arquitetura foca em boas práticas de engenharia, como o gerenciamento de variáveis de ambiente para segurança e um sistema centralizado de logs para monitoramento de falhas.

O projeto é compatível com ambientes de nuvem, como o **Databricks**, e utiliza conexões seguras via JDBC e autenticação básica para garantir a integridade da comunicação entre os sistemas.

## ⚙️ Setup do Projeto

### 1. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
