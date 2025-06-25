import pandas as pd # Importando a biblioteca pandas para manipulação de dados
from sqlalchemy import create_engine

class DataBase: # Classe para manipulação do DataBase
    def __init__(self) -> None: # Método construtor da classe
        host = "dpg-d16kmugdl3ps739giv5g-a.oregon-postgres.render.com"  # Endereço do servidor, pode ser um IP ou 'localhost' para o servidor local
        port = "5432"       # Porta padrão do PostgreSQL
        dbname = "tenis_de_mesa_v_2" # Nome do banco de dados
        user = "tenis_de_mesa_v_2_user" # Nome de usuário do banco de dados
        password = "4Xopur2nE4axZiWnx2YDmfIgnTDOYrBy" # Senha do usuário do banco de dados

        self.engine = create_engine(
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
        )

        try:
            with self.engine.connect() as connection:
                self.conection = True
            
        except:
            self.conection = False


    def verify_connection(self) -> bool:
        """Verifica se a conexão com o banco de dados foi bem-sucedida."""
        return self.conection


    def close(self) -> None:
        '''Fecha a conexão com o banco de dados se estiver conectada.'''
        
        if self.conection:
            self.engine.dispose()
            self.conection = False


    def update_Player(self, command: str) -> None:
        conn = self.engine.raw_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(command)
            conn.commit()
                
        finally:
            conn.close()
            cursor.close()


    def insert_Player(self, tabela_Name: str, Columns: str, datas: tuple) -> None:
        '''Insere um novo jogador no banco de dados.'''

        placeholders = ', '.join(['%s'] * len(datas))
        command = f"INSERT INTO {tabela_Name} {Columns} VALUES ({placeholders})"

        conn = self.engine.raw_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(command, datas)
            conn.commit()
                
        finally:
            conn.close()
            cursor.close()

    
    def insert_Players(self, tabela_Name: str, Columns: str, datas: list[tuple]) -> None:
        '''Insere um novo jogador no banco de dados.'''

        placeholders = ', '.join(['%s'] * len(Columns.replace('(', '').replace(')', '').replace(' ', '').split(',')))
        command = f"INSERT INTO {tabela_Name} {Columns} VALUES ({placeholders})"

        conn = self.engine.raw_connection()
        try:
            cursor = conn.cursor()
            cursor.executemany(command, datas)
            conn.commit()
                
        finally:
            conn.close()
            cursor.close()


    def get_DataBase(self, Command: str) -> pd.DataFrame:
        return pd.read_sql(Command, self.engine)
