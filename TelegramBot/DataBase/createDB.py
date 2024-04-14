import psycopg2
import configparser


def create_conn() -> None:
    """
    Тут мы создаём БД
    """
    config = configparser.ConfigParser()
    config.read('../data.ini')

    conn = psycopg2.connect(
        dbname=config["DB"]["NAME"],
        user=config["DB"]["USER"],
        password=config["DB"]["PASSWORD"],
        host=config["DB"]["HOST"],
        port=config["DB"]["PORT"]
    )
    return conn


conn = create_conn()
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT,
        chatID INT,
        login TEXT,
        pass TEXT,
        token TEXT,
        page INT,
        place_birth TEXT,
        place_die TEXT,
        child TEXT,
        spouse TEXT,
        nationally TEXT,
        study TEXT,
        job TEXT,
        award TEXT,
        epit TEXT
    )
""")

conn.commit()
