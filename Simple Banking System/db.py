import sqlite3


def create_connection(db):
    try:
        connection = sqlite3.connect(db + '.s3db')
        # print('\nConnection to DB was succesfully established!\n')
        return connection

    except sqlite3.Error as er:
        print(f'\nSome error was occured: \n{er}\n')


def init_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute('CREATE TABLE card (id INTEGER PRIMARY KEY AUTOINCREMENT,' 
                       'number TEXT, pin TEXT,'
                       'balance INTEGER DEFAULT 0);')

        connection.commit()
        return

    except sqlite3.Error:
        return


    

if __name__ == '__main__':
    connection = create_connection('card')
    cursor = connection.cursor()
    init_table(connection)

    cursor.execute('INSERT INTO card (number, pin) VALUES (123, 321)')
    connection.commit()
