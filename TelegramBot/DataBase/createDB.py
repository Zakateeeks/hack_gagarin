import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('../../data.ini')

conn = psycopg2.connect(
    dbname=config["DB"]["NAME"],
    user=config["DB"]["USER"],
    password=config["DB"]["PASSWORD"],
    host=config["DB"]["HOST"],
    port=config["DB"]["PORT"]
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT,
        chatID INT,
    )
""")
