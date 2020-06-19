import mysql.connector

conexao = mysql.connector.connect(user ='root',password = '',host = '127.0.0.1',database = 'pessoas')
cursor = conexao.cursor() #entender a conexão

insert_conta =('insert into investimento (empresa,data_invs,status_invs) values (%(empres_d)s,%(data_d)s,%(status_d)s)')

dados = {'empres_d':'IPP',                   #  Exemplo de informações para testar a ligação com o banco de dados.
         'data_d': 20200617,
         'status_d':'c'}
cursor.execute (insert_conta,dados)
conexao.commit()
conexao.close()
