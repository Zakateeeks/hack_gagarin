from .createDB import cur, conn


def get_data(table_name: str, res_column: str, asnw_column: str, answ_value: any) -> list | int | str:
    """
    Получение данных из БД в колонке res_column, где в answ_column лежит значение answ_value

    :param res_column: Название колонки, из которой мы хотим получить значение
    :param table_name: Название таблицы
    :param asnw_column: Название колонки, значение которой нам нужно сравнить
    :param answ_value: Значение для сравнения

    :return: Список полученных значений
    """

    cur.execute(f'SELECT {res_column} FROM {table_name} WHERE {asnw_column} = {answ_value}')
    return cur.fetchall()


def set_data(table_name: str, res_column: str, res_value: any, asnw_column: str, answ_value: any) -> None:
    """
    Вставляет значение res_value в колонку res_column внутри таблицы table_name, где значение колонки asnw_column
    соответсвует значению answ_value

    :param table_name: Название таблицы
    :param res_column: Название колонки в которую мы хотим внести результат
    :param res_value: Значение, которые мы хотим внести в колонку
    :param asnw_column: Название колонки, у которой мы хотим сравнить значение
    :param answ_value: Значение для сравнения

    :return: None
    """
    cur.execute(f"UPDATE {table_name} SET {res_column} = '{res_value}' WHERE {asnw_column} = {answ_value}")
    conn.commit()


def create_db_user(table_name: str, name: str, chatID: int) -> None:
    """
    Функция для внеcения базовых данных при первом использовании бота пользователем

    :param table_name:
    :param name:
    :param chatID:
    :return:
    """
    cur.execute(f"SELECT EXISTS(SELECT 1 FROM {table_name} WHERE chatID = {chatID})")
    exists = cur.fetchone()[0]

    if not exists:
        cur.execute(f"INSERT INTO {table_name} (name, chatID) VALUES ('{name}', {chatID})")
        conn.commit()
