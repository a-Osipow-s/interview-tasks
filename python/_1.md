
import time

def timer_decorator(func):
    """Calculate the execution time of a function"""
    ...

@timer_decorator
def some_important_function(n: int) -> str:
    """Important function"""
    time.sleep(n)
    return "Ready!"


result = some_important_function(2)
print("Result:", result)