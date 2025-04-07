import gspread

URL_COMPARTILHADA_DA_PLANILHA = "https://docs.google.com/spreadsheets/d/1d6VsFORSnFrn3GY2MADbeQ2uuifv8alenn9LECDao8A/edit?gid=553150778#gid=553150778"

ABA = "Produtos"

# Acessar planilha pública
gc = gspread.service_account()
planilha = gc.open_by_url('URL_COMPARTILHADA_DA_PLANILHA')

# Restante do código igual à opção 1

# Selecionar uma aba específica
aba = planilha.worksheet(ABA)  # ou planilha.sheet1

# Ler dados
dados = aba.get_all_records()  # Retorna uma lista de dicionários
print(dados)

# Escrever dados
#aba.update('A1', 'Novo valor')  # Atualiza uma célula específica