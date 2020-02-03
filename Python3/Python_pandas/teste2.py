import pyodbc
# Função de conexao
def retornar_conexao_sql():
    server = "LSTCTX141SPODB.contax-br.contax.root"
    database = "EstudosMatheus"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    return pyodbc.connect(string_conexao)

# Variavel do Cursor
conexao = retornar_conexao_sql()
cursor = conexao.cursor()

sql = " BULK INSERT  [EstudosMatheus].[dbo].[DesafioDias] FROM '\\\CLSCTX186SPODB.contax-br.contax.root\\SQL Server (ETL Sharing - SQLDSPDEV)\\Source\\teste\\Desafio30dias.csv' WITH ( CODEPAGE ='ACP',  ROWTERMINATOR ='\\n', fieldterminator = ';', firstrow = 2)"
                    
cursor.execute(sql)
conexao.commit()
