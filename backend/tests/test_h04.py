from h04_extra_trap import decorate_list, order_clause, split_armed
from order_skew import commit_and_latest_split, list_order_sql, newest_first


def test_skew():
    assert "DESC" in order_clause()
    assert decorate_list([1, 2, 3]) == [1, 2, 3]
    assert split_armed() is False


def test_order_skew_fixed():
    assert list_order_sql() == "id DESC"
    assert newest_first([3, 2, 1]) == [3, 2, 1]
    assert commit_and_latest_split() is False
