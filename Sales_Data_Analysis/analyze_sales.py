import pandas as pd
from pathlib import Path
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def quantidade_total_vendas(df):
    return len(df)


def faturamento_total(df):
    faturamento = (df["Quantidade"] * df["Preco_Unitario"]).sum()
    return faturamento


def ticket_medio(df):
    ticket_medio = faturamento_total(df) / quantidade_total_vendas(df)
    return ticket_medio


def produto_mais_vendido(df):
    produto_vendas = df.groupby("Produto")["Quantidade"].sum()
    produto_mais_vendido = produto_vendas.idxmax()
    return produto_mais_vendido


def produto_mais_faturou(df):
    df = df.copy()
    df["Faturamento"] = df["Quantidade"] * df["Preco_Unitario"]
    faturamento_por_produto = df.groupby("Produto")["Faturamento"].sum()
    produto = faturamento_por_produto.idxmax()
    valor = faturamento_por_produto.max()
    return produto, valor


def categotia_mais_vendeu(df):
    mais_vendeu = df.groupby("Categoria")["Quantidade"].sum().idxmax()
    return mais_vendeu


def cliente_mais_comprou(df):
    df = df.copy()
    df["Valor"] = df["Quantidade"] * df["Preco_Unitario"]

    compras_cliente = df.groupby("Cliente")["Valor"].sum()

    cliente = compras_cliente.idxmax()
    valor_total = compras_cliente.max()

    return cliente, valor_total


def faturaento_mes(df):
    df = df.copy()
    df["Data"] = pd.to_datetime(df["Data"])
    df["Valor Final"] = df["Quantidade"] *df["Preco_Unitario"]
    faturamento_mes = df.groupby(df["Data"].dt.to_period("M"))["Valor Final"].sum()
    return faturamento_mes


def grafico(faturamento_mes):
    faturamento_mes.plot (kind="line", figsize=(10, 5), marker="o")

    plt.title("Faturamento por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Faturamento (R$)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

arquivo_vendas = Path(__file__).resolve().parent / "sales.csv"
df = pd.read_csv(arquivo_vendas)

quantidade_vendas = quantidade_total_vendas(df)
faturamento = faturamento_total(df)
ticket_medio_vendas = ticket_medio(df)
produtos_mais_vendidos = produto_mais_vendido(df)
produto, valor = produto_mais_faturou(df)
categoria_mais_vendeu = categotia_mais_vendeu(df)
clientes_mais_compraram, valor_total = cliente_mais_comprou(df)
faturamento_mes = faturaento_mes(df)




print("\n---------- Analise de Dados ----------")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Faturamento total: R$ {faturamento:.2f}")
print(f"Ticket médio: R$ {ticket_medio_vendas:.2f}")
print(f"Produtos mais vendidos são: {produtos_mais_vendidos}")
print(f"Produto que mais faturou: {produto} com faturamento de R$ {valor:.2f}")
print(f"Categoria que mais vendeu: {categoria_mais_vendeu}")
print(f"Cliente que mais comprou: {clientes_mais_compraram} com valor total de R$ {valor_total:.2f}")
print(f"Faturamento por mês: \n{faturamento_mes}")
grafico(faturamento_mes)
print("--------------------------------------\n")
