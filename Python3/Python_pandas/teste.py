import pyodbc
import pandas as pd 

dados = pd.read_csv(r"C:\Users\607645\Downloads\Desafio30dias.csv",sep=';')
print(dados["Semana"])
print (type(dados))

conn = pyodbc.connect('DSN=PYTHONSQL;Trusted_Connection=yes;')

cursor = conn.cursor()

#select_record = '''SELECT * FROM  [EstudosMatheus].[dbo].[CAVALEIROS_DO_PENTE] '''
#cursor.execute(select_record)
     
#for row in cursor:
#    print(row)

record_1= [dados]
    
record_list = []

record_list.append(dados["Semana"])
record_list.append(dados["ValorPoupado"])
record_list.append(dados["ValorAcumulado"]) 
record_list.append(dados["Pago"])

#print(record_list)
    
insert_records = '''INSERT INTO [EstudosMatheus].[dbo].[DesafioDias]( Semana, ValorPoupado, ValorAcumulado, Pago) VALUES(?,?,?,?)  ''' 
cursor.executemany(insert_records, record_list)
conn.commit()


#print(record_1)