import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

# cursor.execute('''
#     CREATE TABLE table2 (
#         id INTEGER PRIMARY KEY,
#         completed BOOLEAN NOT NULL DEFAULT FALSE
#     );
# ''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);', { 'id': 3, 'completed': False })

# cursor.execute('drop table if exists todohehe;')

connection.commit()

cursor.close()
connection.close()



