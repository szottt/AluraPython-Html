import os
import shutil

caminho_original = 'C:\\Users\\607645\\Downloads\\teste2'
caminho_novo = 'C:\\Users\\607645\\Downloads\\teste3'



for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)


        if '.csv' in file:
            shutil.move(old_file_path, new_file_path)
            print(f'Arquivo copiado com sucesso!')
        
