import pandas as pd
import os
import glob
from faker import Faker
import random

faker = Faker("pt_BR")

departments = ["Recursos Humanos", "Financeiro", "Marketing", "TI", "Vendas", "Operações", "Jurídico", "Engenharia", "Atendimento ao Cliente", "P&D"]
reasons = ["Doença", "Problemas pessoais", "Consulta médica", "Viagem de negócios", "Outros"]

if not os.path.exists("data"):
    os.makedirs("data")

for i in range(50):
    data = {
        "Colaborador_id": [faker.unique.random_number(digits=5) for _ in range(10)],
        "Colaborador_nome": [faker.name() for _ in range(10)],
        "Departamento": [faker.random_element(elements=departments) for _ in range(10)],
        "Motivo_da_ausência": [faker.random_element(elements=reasons) for _ in range(10)],
        "Horas_de_ausência": [faker.random_int(min=1, max=8) for _ in range(10)],
        "Data_da_ausência": [faker.date_between_dates(date_start=pd.to_datetime("2023-06-01"), date_end=pd.to_datetime("2023-06-30")) for _ in range(10)],
        "Salário": [round(random.uniform(2500, 12500), 2) for _ in range(10)]
    }

    df = pd.DataFrame(data)
    df['Data_da_ausência'] = pd.to_datetime(df['Data_da_ausência'])
    
    output_path = os.path.join("data", f"absenteeism_data_{i}.xlsx")
    df.to_excel(output_path, index=False, engine='openpyxl')

if not os.path.exists("consolidado"):
    os.makedirs("consolidado")

files = glob.glob(os.path.join("data", "*.xlsx"))
all_data = [pd.read_excel(file, engine='openpyxl') for file in files]

consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)
consolidated_df.to_excel(os.path.join("consolidado", "consolidated_absenteeism_data.xlsx"), index=False, engine='openpyxl')
