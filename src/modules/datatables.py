from sqlalchemy import or_

def dtify(query, search_filter, convert_fn, params):
    response = {'sEcho': int(params['sEcho'])}

    if search_filter:
        filtered_query = query.filter(search_filter)
    else:
        filtered_query = query

    response['iTotalRecords'] = query.count()
    response['iTotalDisplayRecords'] = filtered_query.count()

    rows = filtered_query.limit(params['iDisplayLength']).offset(params['iDisplayStart']).all()

    aaData = []
    for row in rows:
        aaData.append(convert_fn(row))
    response['aaData'] = aaData

    return response

