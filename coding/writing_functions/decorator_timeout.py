import signal
from functools import wraps
import time

def raise_timeout(*args,**kwargs):
    raise TimeoutError()

# When an 'alarm' signal goes off, call raise_timeout()
signal.signal(sginalnum=signal.SIGALRM, handler = raise_timeout)

# Set off an alarm in 5 seconds
signal.alarm(5)

# Cancel the alarm
signal.alarm(0)

def timeout_in_5s(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
    # Set an alarm for 5 seconds
        signal.alarm(5)
        try:
            # Call the decorated func
            return func(*args, **kwargs)
        
        finally:
            # Cancel alarm
            signal.alarm(0)
    return wrapper

@timeout_in_5s
def foo():
    time.sleep(10)
    print('foo!')

foo()

def timeout(n_seconds):
    def decorator(func):
        @wraps
        def wrapper(*args, **kwargs):
            # Set an alarm for n seconds
            signal.alarm(n_seconds)
            try:
                # Call the decorated func
                return func(*args, **kwargs)

            finally:
                # Cancel alarm
                signal.alarm(0)
        return wrapper
    return decorator

@timeout(10)
def foo():
    time.sleep(10)
    print('foo!')

foo()