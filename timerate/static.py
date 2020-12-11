"""
static.py
This file contains decorators intended to be used to time single functions without verbose reports
"""
try:
    from time import perf_counter_ns as perf_counter
except ImportError:
    from time import perf_counter

def timed(func):
    """
    Use to time a function;
    Returns a tuple (elapsed_time, function_returns)
    """
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        stop = perf_counter()
        elapsed = stop - start
        return elapsed, result
    return wrapper