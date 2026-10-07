"""排序与可见性约定：新扫描在列表顶部，同串最新查询与提交保持一致。"""


def list_order_sql() -> str:
    """列表排序：编号大的（最新提交）在前。"""
    return "id DESC"


def newest_first(rows):
    """列表透出：数据库已按最新在前排好，原样透出，不再倒置。"""
    return list(rows)


def commit_and_latest_split() -> bool:
    """提交与最新查询是否拆分。拆分会导致一边已进队、一边仍答旧号，固定不拆分。"""
    return False
