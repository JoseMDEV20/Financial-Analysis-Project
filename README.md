# Financial-Analysis-Project
Projeto que une as quatro principais ferramentas do mercado: Python, SQL, Excel e Power BI. Criado e desenvolvido por min.

Monitor de Investimentos End-to-End 📈
Python | SQL | Excel | Power BI

Este projeto demonstra a construção de um pipeline de dados completo, desde a extração automatizada de APIs financeiras até a visualização estratégica de indicadores de performance de ativos (Ações, ETFs e Criptomoedas).

🚀 O Projeto
O objetivo principal foi criar uma solução que centraliza dados de mercado dinâmicos com registros de transações pessoais, aplicando a filosofia de que "só se aprende fazendo".

🛠️ Tecnologias e Ferramentas
Python: Automação do processo de ETL utilizando as bibliotecas yfinance e Pandas. Realizou o tratamento de dados complexos (MultiIndex) e normalização de ativos.

SQLite: Utilizado como Data Warehouse local. Implementação de SQL Views com CTEs e Joins para processar regras de negócio (lucro/prejuízo e preço médio) diretamente no banco.

Excel: Atuou como interface de entrada (input) para o cadastro manual de ordens de compra e venda pelo usuário.

Power BI: Camada de visualização conectada via ODBC. Utilizou DAX avançado para criação de métricas de Base 100 (normalização de escala) e formatação condicional.

📂 Estrutura do Repositório
/scripts: Código Python para extração e carga de dados.

/sql: Queries de criação das tabelas e Views de performance.

/data: Modelo da planilha Excel para entrada de dados.

/dashboard: Arquivo .pbix com o layout final.

💡 Destaques Técnicos
Tratamento de Dados: Superação de desafios técnicos na API do Yahoo Finance para garantir a consistência dos dados de fechamento ajustado.

Performance via SQL: Deslocamento da lógica de cálculo do dashboard para o banco de dados, garantindo maior leveza ao relatório.

Análise Comparativa: Uso de lógica de Base 100 no Power BI para comparar ativos com disparidade de preço (ex: Bitcoin vs. Ações brasileiras).
