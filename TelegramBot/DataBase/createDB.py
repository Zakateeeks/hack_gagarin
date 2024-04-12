import psycopg2


conn = psycopg2.connect(
    dbname="название_базы_данных",
    user="пользователь",
    password="пароль",
    host="хост",
    port="порт"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT,
        chatID INT,
    )
""")
