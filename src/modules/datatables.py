from sqlalchemy import or_
from jsonable import make_jsonable

def send_datatable_response(table, request_params):
    query = table.query

    # Filtering
    search = '%%%s%%' % request_params.get('sSearch', "")
    search_cols = []
    for i in range(int(request_params.get("iColumns", 0))):
        if request_params.get("bSearchable_%s" % i) == "true":
            column = getattr(table, request_params.get("mDataProp_%s" % i))
            search_cols.append(column.ilike(search))

    if search_cols:
        query = query.filter(or_(*search_cols))

    # Sorting
    sort_col = request_params.get(
        "mDataProp_%s" % int(request_params.get("iSortCol_0", 0))
    )
    if sort_col:
        sort_direction = request_params.get("sSortDir_0", "asc")
        query = query.order_by(
            "%s %s" % (sort_col, sort_direction)
        )

    # Pagination
    rows = query.limit(
        request_params.get('iDisplayLength', 10)
    ).offset(
        request_params.get('iDisplayStart', 0)
    ).all()

    response = {
        'sEcho': int(request_params.get('sEcho', 0)),
        'iTotalRecords': query.count(),
        'iTotalDisplayRecords': query.count(),
        'aaData': make_jsonable(rows)
    }

    return response
