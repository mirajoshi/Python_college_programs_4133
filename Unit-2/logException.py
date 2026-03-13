# Write a program to generate arithmetic exception and log the exception in system

import logging

logging.basicConfig(
    filename = "exception_log.txt",
    level = logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError as e:
        logging.error("ArithmeticException (ZeroDivisionError): %s | Values: a =%d, b=%d", e, a, b)
        print(f"Exception caught -> Cannot divide {a} by zero. Error logged.")

divide(10, 2)
divide(5, 0)
divide(20, 4)
divide(9, 0)
