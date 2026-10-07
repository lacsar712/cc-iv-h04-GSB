from h04_extra_trap import decorate_list, order_clause, split_armed


def test_list_order_is_newest_first():
    assert "DESC" in order_clause()


def test_decorate_list_keeps_sql_order():
    assert decorate_list([1, 2, 3]) == [1, 2, 3]


def test_commit_and_latest_not_split():
    assert split_armed() is False
