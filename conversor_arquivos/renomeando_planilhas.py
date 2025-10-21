#pip install openpyxl

import openpyxl
import os

# Caminho do arquivo original
caminho_entrada = "C:/Users/User/Documents/planilha_original.xlsx"

# Caminho onde deseja salvar
caminho_saida = "C:/Users/User/Documents/Relatorios/planilha_renomeada.xlsx"

# Carrega o arquivo
wb = openpyxl.load_workbook(caminho_entrada)

# Renomeia a primeira aba
aba_antiga = wb.active
aba_antiga.title = "Resumo Financeiro"

# Cria a pasta de destino SE não existir
os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

# Salva no novo caminho
wb.save(caminho_saida)

print("Planilha renomeada e salva com sucesso! Caminho da planilha salva:\n", caminho_saida)