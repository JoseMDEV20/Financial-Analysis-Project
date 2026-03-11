import yfinance as yf
import sqlite3
import pandas as pd

# 1. Defini os ativos
ativos = ['PETR4.SA', 'ITUB4.SA', 'IVVB11.SA', 'BTC-USD']

print("Buscando dados no Yahoo Finance...")

# MODIFICAÇÃO AQUI: Baixa os dados e deixa o yfinance tratar o fechamento
# auto_adjust=True garante que o 'Close' já seja o valor ajustado
data = yf.download(ativos, period='6mo', auto_adjust=True)

# 2. Seleciona apenas a coluna de fechamento ('Close')
# Como está baixando vários ativos, o pandas cria um MultiIndex
df_precos = data['Close'].reset_index()

# 3. Transforma o formato (de colunas para linhas)
df_melted = df_precos.melt(id_vars='Date', var_name='Ticker', value_name='Preco')

# 4. Conecta ao SQLite
conn = sqlite3.connect('investimentos.db')

# 5. Salva os dados
df_melted.to_sql('historico_precos', conn, if_exists='replace', index=False)

print("Sucesso! O arquivo 'investimentos.db' foi criado no diretório:")
import os
print(os.getcwd())

# 6. Conecta ao banco de dados criado
conn = sqlite3.connect('investimentos.db')

# 7. Colsulta SQL para coletar as primeiras 5 linhas
df_verificacao = pd.read_sql_query("SELECT * FROM historico_precos LIMIT 5", conn)

print("\nPrimeiras linhas do banco de dados.")
print(df_verificacao)

# 8. Lê a planilha do Excel
df_excel = pd.read_excel('meus_investimentos.xlsx')

# 9. Conexta ao banco de dados
conn = sqlite3.connect('investimentos.db')

# 10. Salvar como uma nova tabela (Transacoes)
# Usamos 'replace' para simplificar, mas em projetos reais usaríamos 'append'
df_excel.to_sql('transacoes', conn, if_exists='replace', index=False)

print("Dados do Excel salvos na tabela 'transacoes' do banco.")

print("\nEstas não as primeiras linhas do arquivo .xlsx")
# Deixei os parenteses fazios, pois na planilha não há mais que 5 linhas
print(df_excel.head())

conn = sqlite3.connect('investimentos.db')

# Agora, criamos a View que une as duas tabelas
# Ela pega o último preço disponível para cada ativo e compara com suas compras
query_view = """
CREATE VIEW IF NOT EXISTS v_performance_carteira AS
WITH UltimoPreco AS (
    SELECT Ticker, Preco as Preco_Atual, MAX(Date)
    FROM historico_precos
    GROUP BY Ticker
)
SELECT 
    t.Ticker,
    t.Quantidade,
    t.Preco_Pago,
    up.Preco_Atual,
    (t.Quantidade * t.Preco_Pago) AS Total_Investido,
    (t.Quantidade * up.Preco_Atual) AS Valor_Atual,
    ((up.Preco_Atual / t.Preco_Pago) - 1) * 100 AS Lucro_Percentual
FROM transacoes t
JOIN UltimoPreco up ON t.Ticker = up.Ticker;
"""

cursor = conn.cursor()
cursor.execute("DROP VIEW IF EXISTS v_performance_carteira") # Limpa se já existir
cursor.execute(query_view)
conn.commit()

print("\nView 'v_performance_carteira' criada com sucesso!")
conn.close()

conn.close()