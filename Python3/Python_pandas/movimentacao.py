import os
import shutil
#from datetime import datetime


caminho_original = 'C:\\Users\\607645\\Downloads\\teste2'
caminho_original2 = 'C:\\Users\\607645\\Downloads\\teste2'
caminho_novo = 'C:\\Users\\607645\\Downloads\\teste3'
caminho_old = 'C:\\Users\\607645\\Downloads\\teste2\\old'

try:
    os.mkdir(caminho_old)
except FileExistsError as e:
    print(f'Pasta {caminho_old} ja existe')
        

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_old, file)


        if '.csv' in file:
            shutil.copy('C:\\Users\\607645\\Downloads\\teste2\\data_types.csv', 'C:\\Users\\607645\\Downloads\\teste2\\old\\data_types.csv')
            shutil.move('C:\\Users\\607645\\Downloads\\teste2\\data_types.csv', 'C:\\Users\\607645\\Downloads\\teste3\\data_types2.csv')
            print(f'Arquivo copiado com sucesso!')



'''
for root, dirs, files in os.walk(caminho_original2):
    for file in files:

        print(len(files))

        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        print(old_file_path)
        print(new_file_path)

        if '.csv' in file:
            shutil.move('C:\\Users\\607645\\Downloads\\teste2\\data_types.csv', 'C:\\Users\\607645\\Downloads\\teste3\\data_types2.csv')
            print(f'Arquivo copiado com sucesso!')
'''