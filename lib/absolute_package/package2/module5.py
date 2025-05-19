# module5.py
from .subpackage1.module6 import function1  # Relative import (same package)

def do_work():
    function1()  # Output: Function 1 in module 6

if __name__ == "__main__":
    do_work()