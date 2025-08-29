import pandas as pd

raw_data = pd.read_csv('data/HIST_PAINEL_COVIDBR_2020_Parte1_22ago2025.csv', delimiter=';')

print(raw_data.isna().sum())