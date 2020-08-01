import sqlite3

try:
    conn = sqlite3.connect('db_pikupyhton.db')#pylint: disable=E1101
    cursor = conn.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    

except:
    print("Error while connecting to sqlite")
finally:
    if (conn):
        conn.close()
        print("The SQLite connection is closed")