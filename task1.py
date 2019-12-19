import time


def function_timer(f):
    def wrapped(*args, **kwargs):
        time_f = time.time()
        result = f(*args, **kwargs)
        print('Function execution time: %f' % (time.time() - time_f))
        return result

    return wrapped


@function_timer
def function(x, y):
    return x * y


function(5, 5)
