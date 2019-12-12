import pyodbc


server = 'dbname.database.windows.net'
database = 'dbname'
username = 'username'
password = 'password'
tablename = 'test_table'
driver = '{ODBC Driver 13 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server +
                      ';PORT=1443;DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = conn.cursor()


def execute_sql_command(query, values=None, show_results=False):
    if values is None:
        cursor.execute(query)
    else:
        cursor.execute(query, values)
    print("■ Query")
    print("query : {}".format(query))
    print("values : {}".format(values))
    if show_results:
        print("■ Results")
        row = cursor.fetchone()
        while row:
            print(str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
    print("==========================================================")


# テーブル作成
query = "CREATE TABLE {}(id INT IDENTITY PRIMARY KEY, message NVARCHAR(128) NOT NULL)".format(
    tablename)
execute_sql_command(query=query)
conn.commit()

# レコード追加
messages = ["test_message" + str(i) for i in range(5)]
for message in messages:
    query = "INSERT INTO {} (message) VALUES(?)".format(tablename)
    execute_sql_command(query=query, values=(message))
conn.commit()

# レコードの表示
query = "SELECT * FROM {}".format(tablename)
execute_sql_command(query, show_results=True)

# レコードの修正
query = "UPDATE {} set message = ? where message = ?".format(tablename)
execute_sql_command(query=query, values=("message_mod", messages[1]))
conn.commit()

# レコードの表示
query = "SELECT * FROM {}".format(tablename)
execute_sql_command(query, show_results=True)

# レコードの削除
query = "DELETE FROM {} WHERE message = ? or message = ?".format(tablename)
execute_sql_command(query=query, values=(messages[2], messages[4]))
conn.commit()

# レコードの表示
query = "SELECT * FROM {}".format(tablename)
execute_sql_command(query, show_results=True)

# テーブル削除
query = "DROP TABLE {}".format(tablename)
execute_sql_command(query)
conn.commit()

conn.close()
