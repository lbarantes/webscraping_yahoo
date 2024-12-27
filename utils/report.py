import pandas as pd
import matplotlib.pyplot as plot
from fpdf import FPDF

# Gerar excel usando pandas (+ openpyxl)
def generateExcel(dataframe):
    dataframe.to_excel(f"assets/relatorio.xlsx", index=False)

# Essa função vai gerar um gráfico de exemplo, somente para mostrar o uso do matplotlib
def generateGraph(dataframe):
    plot.figure(figsize=(10, 5))
    plot.plot(dataframe['Date'], dataframe['Close'], label='Close Price')
    plot.title(f"Histórico de Preços")
    plot.xlabel("Data")
    plot.ylabel("Preço")
    plot.legend()
    plot.grid(True)
    plot.savefig(f"assets/relatorio.png")

# Gerar pdf usando FPDF
def generatePdf(dataframe):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Relatório Financeiro", ln=True, align="C")

    pdf.ln(10)
    pdf.set_font("Arial", "B", size=10)
    columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
    col_width = pdf.w / (len(columns)+1)
    row_height = 10

    for col in columns:
        pdf.cell(col_width, row_height, str(col), border=1)
    pdf.ln()

    pdf.set_font("Arial", size=8)
    for row in dataframe.itertuples():
        for i in range(1, len(row)):
            pdf.cell(col_width, row_height, str(row[i])[:10], border=1)
        pdf.ln()
    
    pdf.output(f"assets/relatorio.pdf")