import pandas as pd

# Esta função vai organizar os dados recebidos em um dataframe do Pandas para melhor manipulação
def processData(data):
    columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"] # As colunas que vem chegar na função
    df = pd.DataFrame(data, columns=columns)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce') # Se não for uma data vai se tornar um 'NaT' (Not a Time)
    df['Volume'] = pd.to_numeric(df['Volume'].str.replace(',', ''), errors='coerce') # Se não for um numero vai retornar NaN (Not a Number)
    for col in ["Open", "High", "Low", "Close", "Adj Close"]:
        df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')
    return df.dropna() # Retorna o dataframe retirando valores indesejados (como NaN e NaT por exemplo)
