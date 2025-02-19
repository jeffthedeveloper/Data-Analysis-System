## Estrutura de Diretórios


Sistema-Analise-Dados-Corporativos/ │── 📂 data/ # Diretório para arquivos de dados │ ├── sample_data.csv # Dados de exemplo para testes │ │── 📂 sql/ # Diretório contendo scripts SQL │ ├── schema.sql # Definições das tabelas e estrutura do banco de dados │ ├── 📂 migrations/ # Scripts de criação e atualização do banco de dados │ │ ├── 001_create_tables.sql │ ├── 01_analise_marketing.sql # Query de análise de marketing │ ├── 02_analise_reservas.sql # Query de análise de reservas de hotéis │ ├── 03_analise_vendas.sql # Query de análise de vendas de produtos │ ├── 04_analise_sinistros.sql # Query de análise de sinistros de seguros │ ├── 05_recomendacao_produtos.sql # Query de recomendação de produtos │ │── 📂 reports/ # Diretório de relatórios gerados │ ├── analysis_report.pdf # Relatório gerado da análise dos dados │ │── README.md # Documentação do projeto │── .gitignore # Arquivo para ignorar arquivos desnecessários no Git


# Sistema de Análise de Dados Corporativos Integrados

Este projeto tem como objetivo demonstrar a criação de um sistema de análise de dados SQL integrado, simulando a coleta, processamento e análise de dados de diferentes setores de uma empresa, como marketing, vendas, seguros, telecomunicações e e-commerce. O sistema foi projetado para fornecer insights valiosos para a tomada de decisões estratégicas.

## Estrutura do Projeto

Este repositório contém:

- **Diretório `data/`**: Contém os scripts de criação do banco de dados e dados de exemplo.
- **Diretório `sql/`**: Contém as queries SQL de análise e processamento de dados, divididas em arquivos distintos para cada área da empresa (marketing, vendas, reservas, seguros, etc.).
- **Diretório `reports/`**: Contém relatórios gerados a partir da análise dos dados.

## Funcionalidades Principais

- Análise de **funcionários** de marketing e vendas com orçamento superior a R$1800.
- **Junção de dados** de reservas de clientes com hotéis disponíveis.
- Cálculo da **idade média** dos clientes cadastrados após 2020.
- **Análise de vendas** de produtos por categoria e status.
- **Análise de sinistros de seguros**, com foco em sinistros de seguros automotivos.
- Recomendações personalizadas de **produtos** para clientes com base em seu histórico de compras.

## Como Executar o Projeto

1. Clone este repositório:
    ```bash
    git clone https://github.com/usuario/Sistema-Analise-Dados-Corporativos.git
    cd Sistema-Analise-Dados-Corporativos
    ```

2. Crie o banco de dados e as tabelas executando o script:
    ```bash
    mysql -u username -p < data/schema.sql
    ```

3. Execute os scripts SQL encontrados na pasta `sql/` para realizar as análises:
    ```bash
    mysql -u username -p database_name < sql/01_analise_marketing.sql
    ```

4. Os relatórios de análise serão gerados na pasta `reports/`.

## Dependências

- MySQL ou MariaDB
- Editor de texto para visualização de arquivos `.sql`
- Ferramenta para geração de relatórios (ex: MySQL Workbench, DBeaver)

## Autor

**Jefferson Firmino Mendes**

---

