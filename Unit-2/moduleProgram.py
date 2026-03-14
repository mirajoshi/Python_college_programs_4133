# File 2: moduleProgram (Using the module)

# Way-1 : Import entire module
import mymodule

print("=" * 45)
print("Way 1 ; import mymodule")
print("=" * 45)
print("Add : ", mymodule.add(10, 5))
print("Subtract : ", mymodule.subtract(10, 5))
print("Multiply : ", mymodule.multiply(10, 5))
print("Divide : ", mymodule.divide(10, 5))

# Way-2 : Import specific functions from the module
from mymodule import add, subtract

print("\n" + "=" * 45)
print("Way 2 : from mymodule import add, subtract")
print("=" * 45)
print("Add : ", add(20, 10))
print("Subtract : ", subtract(20,10))

# Way-3 : Import with alias
import mymodule as m

print("\n" + "=" * 45)
print("Way 3 : import mymodule as m")
print("=" * 45)
print("Multiply :", m.multiply(6, 7))
print("Divide   :", m.divide(50, 5))

#Way-4 : Import all functions
from mymodule import *

print("\n" + "=" * 45)
print("Way 4 : from mymodule import *")
print("=" * 45)
print("Add : ", add(10, 5))
print("Subtract : ", subtract(10, 5))
print("Multiply : ", multiply(10, 5))
print("Divide : ", divide(10, 5))
