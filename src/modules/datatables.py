from sqlalchemy import or_
from jsonable import make_jsonable

def send_datatable_response(query, search_filter, request_params):
    filtered_query = query

    if search_filter is not None:
        filtered_query = query.filter(search_filter)

    sort_col = request_params.get(
        "mDataProp_%s" % int(request_params.get("iSortCol_0", 0))
    )
    if sort_col:
        sort_direction = request_params.get("sSortDir_0", "asc")
        filtered_query = filtered_query.order_by(
            "%s %s" % (sort_col, sort_direction)
        )

    rows = filtered_query.limit(
        request_params.get('iDisplayLength', 10)
    ).offset(
        request_params.get('iDisplayStart', 0)
    ).all()

    response = {
        'sEcho': int(request_params.get('sEcho', 0)),
        'iTotalRecords': query.count(),
        'iTotalDisplayRecords': filtered_query.count(),
        'aaData': make_jsonable(rows)
    }

    return response
