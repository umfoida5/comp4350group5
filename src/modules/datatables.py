from sqlalchemy import or_

def dtify(query, search_filter, convert_fn, params):
    response = {'sEcho': int(params.get('sEcho', 0))}

    if search_filter is not None:
        filtered_query = query.filter(search_filter)
    else:
        filtered_query = query

    response['iTotalRecords'] = query.count()
    response['iTotalDisplayRecords'] = filtered_query.count()

    rows = filtered_query.limit(params.get('iDisplayLength', 10)).offset(params.get('iDisplayStart', 0)).all()

    aaData = []
    for row in rows:
        aaData.append(convert_fn(row))
    response['aaData'] = aaData

    return response

