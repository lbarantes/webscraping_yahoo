# Análise de Dados Financeiros com Web Scraping

Este projeto realiza a coleta, análise e apresentação de dados financeiros históricos de empresas listadas na bolsa de valores, com base na sigla da ação fornecida pelo usuário (exemplo: "AAPL" para Apple). O fluxo inclui raspagem de dados, processamento e geração de relatórios em diferentes formatos.  

## ⚒️ Funcionalidades  

1. **Coleta de Dados via Web Scraping**  
   - Utiliza Selenium para acessar o site do Yahoo Finance.  
   - Extrai uma tabela com as seguintes informações sobre uma ação:  
     - Data  
     - Preço de abertura  
     - Preço máximo  
     - Preço mínimo  
     - Preço de fechamento  
     - Ajuste no preço de fechamento  
     - Volume de negociações  

2. **Tratamento e Organização dos Dados**  
   - Armazena os dados em um DataFrame (Pandas).  
   - Realiza o tratamento de erros e valores ausentes.  

3. **Geração de Relatórios**  
   - **Arquivo Excel**: Tabela completa dos dados obtidos.  
   - **Gráfico**: Apresenta a evolução dos preços de fechamento das ações ao longo do período analisado.  
   - **Arquivo PDF**: Tabela formatada em PDF com os dados obtidos.

## 💻 Tecnologias Utilizadas  

- **Selenium**: Raspagem de dados.  
- **Pandas**: Tratamento e manipulação de dados, geração do arquivo Excel.  
- **Matplotlib**: Geração de gráficos.  
- **FPDF**: Criação do relatório em PDF.
