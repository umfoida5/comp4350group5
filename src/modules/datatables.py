from sqlalchemy import or_
from jsonable import make_jsonable

def send_datatable_response(query, search_filter, request_params):
    filtered_query = query

    if search_filter is not None:
        filtered_query = query.filter(search_filter)

    rows = filtered_query.limit(
        request_params.get('iDisplayLength', 10)
    ).offset(
        request_params.get('iDisplayStart', 0)
    ).all()    

    response = {'sEcho': int(request_params.get('sEcho', 0))}
    response['iTotalRecords'] = query.count()
    response['iTotalDisplayRecords'] = filtered_query.count()
    response['aaData'] = make_jsonable(rows)

    return response