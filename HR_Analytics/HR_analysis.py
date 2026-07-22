from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def numero_funcionarios(df):
    return len(df)


def salario_medio(df):
    return df['Salario'].mean()


def salario_maximo(df):
    return df["Salario"].max()


def salario_minimo(df):
    return df["Salario"].min()


def idade_media(df):
    return df["Idade"].mean()


def tempo_medio_empresa(df):
    return df["Tempo_Empresa"].mean()


def departamento_mais_funcionarios(df):
    return df["Departamento"].value_counts().idxmax()


def departamento_mais_paga(df):
    return df.groupby("Departamento")["Salario"].max().idxmax()


def salario_medio_departamento(df):
    return df.groupby("Departamento")["Salario"].mean()


def quantidade_funcionario_departamento(df):
    return df.groupby("Departamento")["Nome"].count()


def cargo_maior_salario_medio(df):
    medias = df.groupby("Cargo")["Salario"].mean()
    return medias.idxmax()


def cargo_comum(df):
    return df["Cargo"].mode().iloc[0]


def numero_desenvolvedores(df):
    return len(df[df["Cargo"] == "Desenvolvedor"])


def maior_avaliacao(df):
    return df["Avaliacao"].max()


def media_avaliacao(df):
    return df["Avaliacao"].mean()


def funcionarios_avaliacao_maior_9(df):
    return df[df["Avaliacao"] > 9]


def funcionario_antigo(df):
    return df[df["Tempo_Empresa"] == df["Tempo_Empresa"].max()]


def funcionario_novo(df):
    return df[df["Tempo_Empresa"] == df["Tempo_Empresa"].min()]


def funcionario_bem_pago(df):
    return df.groupby("Nome")["Salario"].max().idxmax()


def graficos(df):
    fig, graficos = plt.subplots(2, 2, figsize=(14, 10))

    salario_medio = df.groupby("Departamento")["Salario"].mean()

    salario_medio.plot(kind="bar", ax=graficos[0, 0], color="skyblue")

    graficos[0, 0].set_title("Salário médio por departamento")
    graficos[0, 0].set_xlabel("Departamento")
    graficos[0, 0].set_ylabel("Salário médio (R$)")
    graficos[0, 0].tick_params(axis="x", rotation=45)

    # 2. Histograma dos salários
    graficos[0, 1].hist(
        df["Salario"],
        bins=8,
        color="seagreen",
        edgecolor="black"
    )

    graficos[0, 1].set_title("Distribuição dos salários")
    graficos[0, 1].set_xlabel("Salário (R$)")
    graficos[0, 1].set_ylabel("Quantidade")

    df["Departamento"].value_counts().plot(
        kind="pie",
        ax=graficos[1, 0],
        autopct="%1.1f%%",
        startangle=90
    )

    graficos[1, 0].set_title("Distribuição dos departamentos")
    graficos[1, 0].set_ylabel("")


    df["Cargo"].value_counts().plot(
        kind="bar",
        ax=graficos[1, 1],
        color="darkorange"
    )

    graficos[1, 1].set_title("Quantidade de funcionários por cargo")
    graficos[1, 1].set_xlabel("Cargo")
    graficos[1, 1].set_ylabel("Quantidade")
    graficos[1, 1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.show()


arquivo_funcionarios = Path(__file__).resolve().parent / "data" / "employees.csv"
df = pd.read_csv(arquivo_funcionarios)

numero_funcionario = numero_funcionarios(df)
salario_medio_funcionarios = salario_medio(df)
salario_maximo_funcionarios = salario_maximo(df)
salario_minimo_funcionarios = salario_minimo(df)
idade_media_funcionarios = idade_media(df)
tempo_medio_empresa_funcionarios = tempo_medio_empresa(df)
departamento_mais_paga_funcionarios = departamento_mais_paga(df)
salario_medio_departamento_funcionarios = salario_medio_departamento(df)
quantidade_funcionario_por_departamento = quantidade_funcionario_departamento(df)
cargo_maior_salario_medio_funcionario = cargo_maior_salario_medio(df)
cargo_mais_comum = cargo_comum(df)
numero_desenvolvedores_funcionarios = numero_desenvolvedores(df)
maior_avaliacao_funcionarios = maior_avaliacao(df)
media_avaliacao_funcionarios = media_avaliacao(df)
funcionario_avaliacao_maior_9 = funcionarios_avaliacao_maior_9(df)
funcionario_mais_antigo = funcionario_antigo(df)
funcionario_mais_novo = funcionario_novo(df)
funcionario_mais_bem_pago = funcionario_bem_pago(df)


print("\n---------- Dados do RH ----------")
print(f"O numero de funcionarios é: {numero_funcionario}")
print(f"O salario medio dos funcionarios é: {salario_medio_funcionarios}")
print(f"O salario maximo dos funcionarios é: {salario_maximo_funcionarios}")
print(f"O salario minimo dos funcionarios é: {salario_minimo_funcionarios}")
print(f"A idade media dos funcionarios é: {idade_media_funcionarios}")
print(f"O tempo medio na empresa dos funcionarios é: {tempo_medio_empresa_funcionarios}")
print(f"O departamento que mais paga é: {departamento_mais_paga_funcionarios}")
print(f"\nO salário médio por departamento é:\n" f"{salario_medio_departamento_funcionarios.to_string()}")
print(f"\nA quantidade de funcionários por departamento é:\n" f"{quantidade_funcionario_por_departamento.to_string()}")
print(f"O cargo com maior salario medio é: {cargo_maior_salario_medio_funcionario}")
print(f"O cargo mais comum é: {cargo_mais_comum}")
print(f"O numero de desenvolvedores é: {numero_desenvolvedores_funcionarios}")
print(f"A maior avaliação dos funcionários é: {maior_avaliacao_funcionarios}")
print(f"A média das avaliações dos funcionários é: {media_avaliacao_funcionarios}")
print(f"\nOs funcionários com avaliação maior que 9 são:\n" f"{funcionario_avaliacao_maior_9.to_string()}")
print(f"\nO funcionário mais antigo é:\n" f"{funcionario_mais_antigo.to_string()}")
print(f"\nO funcionario mais novo é: {funcionario_mais_novo}")
print(f"\nO funcionário mais bem pago é: {funcionario_mais_bem_pago}")
criar_graficos = graficos(df)