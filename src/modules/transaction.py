from decorator import decorator
from database import db_session

@decorator
def commit_on_success(f, *args, **kw):
    try : 
        func = f(*args, **kw)
        db_session.commit()
    except : 
        db_session.rollback()
        raise

    return func    