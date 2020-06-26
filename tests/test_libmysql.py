import pytest


@pytest.mark.usefixtures("mysql_lib")
def test_sql_01_insert(mysql_lib):
    sql = "INSERT INTO board (name, port_count) VALUES ('{}', {})".format(
        "Testing Board LMK #1", 8
    )
    record = mysql_lib.execute(sql)
    assert record > 0

    sql = "INSERT INTO board (name, port_count) VALUES ('{}', {})".format(
        "hello", 4)
    record = mysql_lib.execute(sql)
    assert record > 0


@pytest.mark.usefixtures("mysql_lib")
def test_sql_02_update(mysql_lib):
    sql = "UPDATE board SET port_count={} WHERE name = '{}'".format(10, "hello")
    record = mysql_lib.execute(sql)
    assert record > 0


@pytest.mark.usefixtures("mysql_lib")
def test_sql_03_delete(mysql_lib):
    sql = "DELETE FROM board WHERE port_count>={}".format(10)
    record = mysql_lib.execute(sql)
    assert record > 0


@pytest.mark.usefixtures("mysql_lib")
def test_sql_04_select(mysql_lib):
    sql = "SELECT COUNT(*) as result FROM board;"
    for each in mysql_lib.select(sql):
        assert each.get("result") > 0
