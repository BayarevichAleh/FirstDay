class database:
    import psycopg2
    def __init__(self, DB_USER, DB_PASSWORD, DB_NAME, DB_ECHO=False):
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME
        self.DB_ECHO = DB_ECHO
        self.connect = self.psycopg2.connect(database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD,
                                             host='localhost')

    def create_table(self, table_name, **kwargs):
        columns = ''
        for i in enumerate(kwargs):
            columns = f"{columns} {i[1]} {kwargs[i[1]]},"

        columns = columns[0:-1:1]

        cursor = self.connect.cursor()
        cursor.execute(
            f"""
            CREATE TABLE {table_name}
                (
                {columns}
                )
            """
        )
        self.connect.commit()
        cursor.close()

    def add_item(self, table_name, name, cost=0, amount=0, commit=''):
        cursor = self.connect.cursor()
        cursor.execute(
            f"""
            INSERT INTO {table_name} (name,cost,amount,commit) values('{name}',{cost},{amount},'{commit}')
            """
        )
        self.connect.commit()
        cursor.close()
        print(f"Item added!")

    def remove_item(self, table_name, id):
        cursor = self.connect.cursor()
        cursor.execute(
            f"""
            DELETE from {table_name} where id={id}
            """
        )
        self.connect.commit()
        cursor.close()
        print(f"Id:{id} removed")

    def update_item(self, table_name, id, name=None, cost=None, amount=None, commit=None):
        args = ''
        if name != None:
            args = f"{args} name='{name}',"
        if cost != None:
            args = f"{args} cost={cost},"
        if amount != None:
            args = f"{args} amount={amount},"
        if commit != None:
            args = f"{args} commit='{commit}',"
        args = args[0:-1:1]

        cursor = self.connect.cursor()
        cursor.execute(
            f"""
            UPDATE {table_name} SET {args} where id={id}
            """
        )
        self.connect.commit()
        cursor.close()
        print(f"Next values changed in id:{id}: {args}")

    def find_item(self, table_name, column, value):
        cursor = self.connect.cursor()
        cursor.execute(
            f"""
            SELECT * FROM {table_name} WHERE {column}='{value}'
            """
        )
        view = cursor.fetchall()
        self.connect.commit()
        cursor.close()
        if view == []:
            print("Items not find!")
        else:
            for i in view:
                print(f"id: {i[0]} name: {i[1]} cost: {i[2]} amont: {i[3]} commit: {i[4]}")

    def list_items(self, table_name):
        cursor = self.connect.cursor()
        cursor.execute(
            f"""
            SELECT * FROM {table_name}
            """
        )
        view = cursor.fetchall()
        self.connect.commit()
        cursor.close()
        if view == []:
            print("Table is blank!")
        else:
            for i in view:
                print(f"id: {i[0]}  name: {i[1]}  cost: {i[2]}  amont: {i[3]}  commit: {i[4]}")

    def __del__(self):
        self.connect.close()
