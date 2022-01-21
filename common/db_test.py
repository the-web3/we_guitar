import time
import json
import logging
from functools import wraps
from django.db import connection  #type: ignore

class QueryLogger:

    def __init__(self):
        self.queries = []

    def __call__(self, execute, sql, params, many, context):
        current_query = {'sql': sql, 'params': params, 'many': many}
        start = time.monotonic()
        try:
            result = execute(sql, params, many, context)
        except Exception as e:
            current_query['status'] = 'error'
            current_query['exception'] = e
            raise
        else:
            current_query['status'] = 'ok'
            return result
        finally:
            duration = time.monotonic() - start
            current_query['duration'] = duration
            current_query['name'] = self.name
            current_query['path'] = self.path

            logger = logging.getLogger('QueryLogger')
            for key in current_query.keys():
                current_query[key] = str(current_query[key])
            logger.info(json.dumps(current_query))

def db_test(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        ql = QueryLogger()
        import os
        import inspect

        ql.path=os.path.abspath(inspect.getfile(f))
        ql.name=f.__name__
        with connection.execute_wrapper(ql):
            return f(*args, **kwargs)
    return decorated


