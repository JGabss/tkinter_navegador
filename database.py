import sqlite3 as S
from uuid import uuid4
from datetime import datetime

class Banco_de_Dados:
    def __init__(self):
        self.nomeBanco = "Cactus Search"
        self.b1 = S.connect(self.nomeBanco)
        self.cursor = self.b1.cursor()
        cod_sql2 = "CREATE TABLE if not exists Historico (id, historico varchar(250), PRIMARY KEY (id))"
        self.cursor.execute(cod_sql2)
        self.b1.commit()

    def inserirHistorico(self, item):
        data = datetime.now()
        formato = f"{data.day}/{data.month}/{data.year} - {data.hour}:{data.minute}"
    
        id = uuid4()
        cod_sql = f"INSERT INTO Historico (id, historico) VALUES ('{id}', '{item} - {formato}')"
        self.cursor.execute(cod_sql)
        self.b1.commit()

    def mostrarHistorico(self):
        historico = []
        cod_sql = "SELECT * FROM Historico"
        self.cursor.execute(cod_sql)
        tabela = self.cursor.fetchall()
        for a in tabela:
            historico.append(a[1])
        
        return historico

    def fechar(self):
        self.b1close()
