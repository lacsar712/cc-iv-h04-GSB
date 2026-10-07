"""列表顶序与“同串最近”共用的顺序定义：新扫描排最前，入队提交与最近查询不分离。"""


def list_order_sql() -> str:
    return "id DESC"


def preserve_sql_order(rows):
    return list(rows)


def commit_and_latest_split() -> bool:
    return False
