from sqlalchemy import or_

def dtify(query, search_filter, convert_fn, params):
    response = {'sEcho': int(params.get('sEcho', 0))}

    if search_filter is not None:
        filtered_query = query.filter(search_filter)
    else:
        filtered_query = query
    
    response['iTotalRecords'] = query.count()
    response['iTotalDisplayRecords'] = filtered_query.count()

    sort_col = params.get("mDataProp_%s" % int(params.get("iSortCol_0", 0)))
    sorted_query = filtered_query
    if sort_col:
        sort_dir = params.get("sSortDir_0", "asc")
        sorted_query = sorted_query.order_by("%s %s" % (sort_col, sort_dir))

    rows = sorted_query.limit(params.get('iDisplayLength', 10)).offset(params.get('iDisplayStart', 0)).all()

    aaData = []
    for row in rows:
        aaData.append(convert_fn(row))
    response['aaData'] = aaData

    return response

