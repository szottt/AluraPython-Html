from datetime import datetime

data_hoje = hoje.strftime('%d/%m/%y')  # Descobrindo a data atual para 
posteriormente comparar com a data limite

input_data_limite = input('DATA LIMITE: ') # Entrando com a data limite 

data_limite = datetime.strftime(input_data_limite, '%d/%m/%y') # deveria 
converter em datetime mas da erro

print(data_limite) 