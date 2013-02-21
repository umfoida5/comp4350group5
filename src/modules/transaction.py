from decorator import decorator
import database

@decorator
def commit_on_success(f, *args, **kw):
    try : 
        func = f(*args, **kw)
        database.session.commit()
    except : 
        database.session.rollback()
        raise

    return func
    