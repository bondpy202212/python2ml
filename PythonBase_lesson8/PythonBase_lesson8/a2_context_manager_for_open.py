
# context manager - is the best way for open file

class MyManager(object):
    def __init__(self):
        self.resource = 42

    def __enter__(self):
        print('Entered context')
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Left context')
        if exc_type:
            print('(Exception occured: {})'.format(exc_type))



#with MyManager() as resource:
#    print('Some actions with resource:', resource)
#    raise ValueError



# create analog function "with" (how it's working)
# ++++++++++++++++++++++++++++++++++++++++++++++++

import sys 

def my_with(manager, context_body):
    resource = manager.__enter__()
    exc_type, exc_value, exc_traceback = None, None, None
    error = None
    try:
        context_body(resource)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        error = e
    finally:
        manager.__exit__(exc_type, exc_value, exc_traceback)
        if error:
            raise error

def context_body(resource):
    print('Some actions with resource:', resource)
    raise ValueError

my_with(MyManager(), context_body)

# ++++++++++++++++++++++++++++++++++++++++++++++++