"""
libmysql: Generic Low-level MySQL wrapper client to execute RAW SQL statements.
"""

from contextlib import contextmanager

import pymysql

from mAPN_service import config


def select_config_variable(for_database: str = "app"):
    """
    Collect MYSQL_* attributes as a hash/dictionary from config object.

    Arguments:
        for_database {str} - Specify which db connection should be used.
                             (Default: "app", Possible values: "app", "radius")

    Returns:
        dict - Collected attributes
    """
    mapping = {
        "DB_NAME": "db",
        "DB_HOST": "host",
        "DB_PORT": "port",
        "DB_USER": "user",
        "DB_PASSWORD": "password",
        "DB_ENCODING": "charset",
    }
    selector = lambda x: [v for k, v in mapping.items() if x.endswith(k)][-1]  # noqa
    return {
        selector(k): v
        for k, v in config.__dict__.items()
        if isinstance(k, str)
        and k.startswith("MYSQL_")
        and not k.endswith("_URI")
        and for_database in k.lower()
    }.copy()


@contextmanager
def get_connection(*args, **kwargs):
    """
    Create a MySQL db connection using PyMySQL.

    Example:
    ```
    from mAPN_service.modules.libmysql import get_connection

    # select all records
    with get_connection() as db_conn:
        cursor = db_conn.cursor()
        sql = "SELECT * FROM students ORDER BY id DESC;"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            # do with data
            row = cursor.fetchone()

    # select single record
    with get_connection().cursor() as cursor:
        sql = "SELECT * FROM students WHERE id={id}".format(id=1)
        cursor.execute(sql)
        record = cursor.fetchone()
        if not record:
            print("Record not found for ID: {id}".format(id=1)
        else:
            # do with found student info
            print(record)
    ```

    REF: https://stackoverflow.com/a/31215864/

    Arguments:
        - *args {list} - Arguments list which will be passed to pymysql.connect().
                         For more detail, please refer to https://pymysql.readthedocs.io/en/latest/user/examples.html
    Keyword Arguments:
        - **kwargs {dict} - Keyword arguments which will be passed to pymysql.connect().

    Most frequently used Keyword Arguments:
        - host {str} - Specify mysql host name (Default: "localhost")
        - port {int} - Specify mysql port (Default: 3306)
        - user {str} - Specify mysql user (Default: "root")
        - password {str} - Specify mysql password (Default: "toor")
        - db {str} - Specify Database name (Default: "test")
        - charset {str} - Specify charset (Default: "utf8mb4")
        - cursorclass {object} - Specify Cursor type (Default: pymysql.cursors.DictCursor)
        - for_database {str} - Specify which db connection should be used.
                               (Default: "app", Possible values: "app", "radius")

        NOTE: please refer to PyMySQL documentation for more parameters. (pymysq.connect).

    Yield:
        object - connection object (Ref: https://pymysql.readthedocs.io/en/latest/modules/connections.html)
    """
    for_database = kwargs.get("for_database") or "app"
    if for_database not in ["app", "radius"]:
        raise ValueError(
            "Invalid option: {option_name}".format(option_name=for_database)
        )

    print(f"DEBUG: {for_database}")
    print(select_config_variable(for_database))
    kwargs.update(select_config_variable(for_database))
    if "cursorclass" not in kwargs:
        kwargs["cursorclass"] = pymysql.cursors.DictCursor

    print(args)
    print(kwargs)
    connection = pymysql.connect(*args, **kwargs)
    try:
        yield connection
    finally:
        connection.close()


def select(statement, *args, **kwargs):
    """
    Execute SQL SELECT statement.

    E.g.
        TODO: to be described

    Arguments:
        - statement {str} - SQL SELECT statement

    Yield:
        dict - Row object as a dictionary
    """
    with get_connection() as db_conn:
        cursor = db_conn.cursor()
        cursor.execute(statement, *args, **kwargs)
        row = cursor.fetchone()
        while row:
            yield row
            row = cursor.fetchone()


def execute(statement, *args, **kwargs):
    """
    Execute generic SQL statement (It is intended for INSERT, UPDATE, DELETE but not recommended for SELECT.
    But, it is ok to use single row selection. For SELECT statement (single/multiple rows), please use
    `select()` function.

    E.g.
        TODO: to be described

    Arguments:
        - statement {str} - SQL INSERT statement

    Known keyword arguments:
        - autocommit {boolean} - Commit after INSERT, UPDATE, and DELETE is executed. (Default: True)

    Returns:
        object - Affected row
    """
    autocommit = kwargs.get("autocommit") or True
    with get_connection() as db_conn:
        cursor = db_conn.cursor()
        cursor.execute(statement, *args, **kwargs)
        if autocommit:
            db_conn.commit()
        return (
            getattr(cursor, "rowcount")
            or getattr(cursor, "lastrowid")
            or getattr(db_conn, "insert_id")()
        )
