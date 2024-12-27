import os
import utils.scraper as scraper
import utils.analizer as analizer
import utils.report as report

if not os.path.exists("assets"):
    os.makedirs("assets", exist_ok=True)

enterprise = input("Digite a sigla da ação de uma empresa (ex. AAPL): ")

if (len(enterprise) > 4):
    print("A sigla não pode ter mais que 4 letras")
    exit()

if (len(enterprise) < 4):
    print("A sigla não pode ter menos que 4 letras")
    exit()

data = scraper.scrapData(enterprise)

if data == 404:
    print("Empresa não encontrada")
    exit()

dfData = analizer.processData(data)

report.generateExcel(dfData)
report.generateGraph(dfData)
report.generatePdf(dfData)
